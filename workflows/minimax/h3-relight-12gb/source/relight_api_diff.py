"""Diff the API prompt the ComfyUI frontend makes from the SAVED relight workflow (graphToPrompt export) against
build_h3_relight.py's known-good graph for the same settings (2026-11-11).

Both graphs are normalised the same way: primitives inlined, every Math Expression / String Compare / CustomCombo with
constant inputs evaluated (the clip's size = desk_talk.mp4, 1920x1088, 127 frames), every If/Else switch with a constant
switch replaced by the branch it picks (ComfyUI evaluates them lazily, the other branch never runs), model names reduced to
the file name. Then only nodes that feed an output node are kept, and each node gets a Merkle signature (class + inputs +
the signatures of what feeds it). Equal signature multisets = the same computation.

    python relight_api_diff.py
"""
import json
import math
import os
import sys
from argparse import Namespace
from collections import Counter

sys.path.insert(0, r"C:\Users\friso\Studio\OSH-test\app")
import build_h3_relight as B  # noqa: E402

CHECK = r"C:\Users\friso\Documents\ComfyUI-Portable\ComfyUI\user\default\relight_check"
PRESETS = r"C:\Users\friso\Studio\Relight-local\sirio_presets\presets.json"
CLIP = (1920, 1088, 127)      # ffprobe of input/desk_talk.mp4
OUTPUTS = {"SaveVideo", "PreviewAny"}
PRIM = {"PrimitiveInt", "PrimitiveFloat", "PrimitiveString", "PrimitiveStringMultiline", "PrimitiveBoolean"}


def is_link(v):
    return isinstance(v, list) and len(v) == 2 and isinstance(v[1], int)


def builder(short_side, upscale=None, sigmas=None):
    master = next(p["master"] for p in json.load(open(PRESETS, encoding="utf-8")) if p["id"] == "cinematic-04-blue-amber-bed")
    a = Namespace(video="desk_talk.mp4", sphere="cinematic-04-blue-amber-bed.png", master=master, direction="", seconds=0.0,
                  short_side=short_side, steps=6, seed=42, unet=B.PLAIN_H3, lora_strength=1.0, ref_size="match",
                  prefix="H3 relight/relight", upscale=upscale, refine_sigmas=sigmas or "0.909375, 0.857143, 0.666667, 0.0")
    return B.build(a)


OI = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "relight_object_info.json"), encoding="utf-8"))


def with_defaults(g):
    """Optional inputs a graph leaves out get their default (that is what the server does)."""
    for v in g.values():
        spec = OI.get(v["class_type"], {}).get("input", {})
        for name, s in {**spec.get("required", {}), **spec.get("optional", {})}.items():
            if name not in v["inputs"] and isinstance(s, list) and len(s) > 1 and isinstance(s[1], dict) and "default" in s[1]                     and not str(s[0]).startswith("COMFY_"):
                v["inputs"][name] = s[1]["default"]
    return g


def normalise(g):
    g = with_defaults({k: {"class_type": v["class_type"], "inputs": dict(v["inputs"])} for k, v in g.items()})
    # "video-preview" is a frontend-only widget value the server ignores; 1 and 1.0 are the same number to ComfyUI
    num = lambda x: float(x) if isinstance(x, (int, float)) and not isinstance(x, bool) else x  # noqa: E731
    g = {k: {"class_type": v["class_type"], "inputs": {a: num(x) for a, x in v["inputs"].items() if a != "video-preview"}}
         for k, v in g.items()}
    const = {}   # (key, slot) -> value

    def val(x):
        if is_link(x):
            return const.get((str(x[0]), x[1]), x)
        if isinstance(x, str) and x.lower().endswith((".safetensors", ".pth")):
            return x.replace("\\", "/").split("/")[-1]
        return x

    changed = True
    alias = {}   # (key, slot) -> link it is the same as (switches)
    while changed:
        changed = False
        for k, v in g.items():
            for a, x in list(v["inputs"].items()):
                if is_link(x) and (str(x[0]), x[1]) in alias:
                    v["inputs"][a] = alias[(str(x[0]), x[1])]; changed = True
                y = val(v["inputs"][a])
                if y is not v["inputs"][a] and y != v["inputs"][a]:
                    v["inputs"][a] = y; changed = True
            ct, inp = v["class_type"], v["inputs"]
            if (k, 0) in const or any((k, s) in alias for s in range(3)):
                continue
            consts = all(not is_link(x) for x in inp.values())
            if ct in PRIM and consts:
                const[(k, 0)] = num(inp["value"]); changed = True
            elif ct == "CustomCombo" and consts:
                const[(k, 0)] = inp["choice"]; const[(k, 1)] = float(inp.get("index", 0)); changed = True
            elif ct == "StringCompare" and consts:
                a_, b_ = inp["string_a"], inp["string_b"]
                if not inp.get("case_sensitive", True):
                    a_, b_ = a_.lower(), b_.lower()
                const[(k, 0)] = {"Equal": a_ == b_, "Starts With": a_.startswith(b_), "Ends With": a_.endswith(b_)}[inp["mode"]]
                changed = True
            elif ct == "ComfyMathExpression" and consts:
                names = {a.split(".")[1]: x for a, x in inp.items() if a.startswith("values.")}
                r = eval(inp["expression"], {"__builtins__": {}}, dict(names, min=min, max=max, round=round, ceil=math.ceil,
                                                                       floor=math.floor, sqrt=math.sqrt, abs=abs))
                const[(k, 0)], const[(k, 1)], const[(k, 2)] = float(r), float(int(r)), bool(r)
                changed = True
            elif ct == "ComfySwitchNode" and not is_link(inp.get("switch")):
                pick = inp.get("on_true" if inp["switch"] else "on_false")
                if is_link(pick):
                    alias[(k, 0)] = [str(pick[0]), pick[1]]
                else:
                    const[(k, 0)] = pick
                changed = True
            elif ct == "GetImageSize" and is_link(inp["image"]):
                src = g.get(str(inp["image"][0]))
                if src and src["class_type"] == "GetVideoComponents" and is_link(src["inputs"]["video"]) and \
                        g[str(src["inputs"]["video"][0])]["class_type"] == "LoadVideo":
                    const[(k, 0)], const[(k, 1)], const[(k, 2)] = map(float, CLIP); changed = True
                elif src and src["class_type"] == "GetVideoComponents" and is_link(src["inputs"]["video"]) and \
                        g[str(src["inputs"]["video"][0])]["class_type"] == "Video Slice":
                    sl = g[str(src["inputs"]["video"][0])]["inputs"]
                    if not is_link(sl["duration"]) and sl["duration"] <= 0.05 and sl["start_time"] == 0:
                        const[(k, 0)], const[(k, 1)], const[(k, 2)] = float(CLIP[0]), float(CLIP[1]), 1.0; changed = True
    # keep what feeds an output node
    keep, todo = set(), [k for k, v in g.items() if v["class_type"] in OUTPUTS]
    while todo:
        k = todo.pop()
        if k in keep:
            continue
        keep.add(k)
        todo += [str(x[0]) for x in g[k]["inputs"].values() if is_link(x)]
    return {k: g[k] for k in keep}


def signatures(g):
    memo = {}

    def sig(k):
        if k not in memo:
            v = g[k]
            parts = []
            for a in sorted(v["inputs"]):
                x = v["inputs"][a]
                parts.append(f"{a}=<{sig(str(x[0]))}#{x[1]}>" if is_link(x) else f"{a}={json.dumps(x, ensure_ascii=False)}")
            memo[k] = v["class_type"] + "(" + ",".join(parts) + ")"
        return memo[k]
    return {k: sig(k) for k in g}


def short(s, n=160):
    return s if len(s) <= n else s[:n] + "..."


def diff(name, ui, ref):
    a, b = normalise(ui), normalise(ref)
    sa, sb = signatures(a), signatures(b)
    ca, cb = Counter(sa.values()), Counter(sb.values())
    only_ui = ca - cb
    only_ref = cb - ca
    print(f"\n== {name}: UI {len(a)} live nodes, builder {len(b)} live nodes, identical {sum((ca & cb).values())}")
    print("   classes UI     :", dict(sorted(Counter(v['class_type'] for v in a.values()).items())))
    print("   classes builder:", dict(sorted(Counter(v['class_type'] for v in b.values()).items())))
    # report only the top-most differing nodes (whose inputs all match) to keep it short
    def roots(only, g, sg):
        out = []
        for k, s in sg.items():
            if only.get(s):
                feeders = [sg[str(x[0])] for x in g[k]["inputs"].values() if is_link(x)]
                if not any(only.get(f) for f in feeders):
                    out.append((g[k]["class_type"], {a: x for a, x in g[k]["inputs"].items() if not is_link(x)}))
        return out
    for side, only, g, sg in (("UI only", only_ui, a, sa), ("builder only", only_ref, b, sb)):
        for ct, consts in roots(only, g, sg):
            print(f"   {side}: {ct} {short(json.dumps(consts, ensure_ascii=False))}")
    return a, b


if __name__ == "__main__" and "--spec" not in sys.argv:
    load = lambda t: json.load(open(os.path.join(CHECK, t + ".json"), encoding="utf-8"))  # noqa: E731
    diff("480, Full HD off", load("ui_480_off"), builder(480))
    diff("736 + gentle refine (builder --upscale 1920 1088 --refine-sigmas 0.55...)", load("ui_736_gentle"),
         builder(736, (1920, 1088), "0.55, 0.4, 0.2, 0.0"))


def vs_spec():
    """The saved file's export against the intended graph (ultimate2_relight.relight_api) for every path."""
    import ultimate2_relight as R
    load = lambda t: json.load(open(os.path.join(CHECK, t + ".json"), encoding="utf-8"))  # noqa: E731
    for tag, kw in (("ui_480_off", {}), ("ui_736_gentle", {"short_side": 736, "mode": R.M_GENTLE}),
                    ("ui_736_esrgan", {"short_side": 736, "mode": R.M_ESRGAN}), ("ui_480_long10", {"long": True, "seconds": 10.0})):
        g, _ = R.relight_api(**kw)
        diff(f"{tag} vs the intended graph", load(tag), g)


if __name__ == "__main__" and "--spec" in sys.argv:
    vs_spec()

#!/usr/bin/env python3
"""
Repository consistency check (pure Python, no ComfyUI needed).

For every workflow folder:
  - every model file the workflow .json loads is in models.json and downloads.md (exact name)
  - models.json lists nothing the .json never loads (unless marked optional / manual)
  - the custom node packs the .json uses (node pack ids saved in the .json) are in models.json "nodes"
  - version: .json file name = root README table = changelog top entry; README names its .json
And with --links: every models.json download URL answers (401 = gated, needs HF_TOKEN; reported, not an error).

    python scripts/check_repo.py            # files, nodes, versions
    python scripts/check_repo.py --links    # + HEAD-request every download link
Exit code 1 if anything is wrong. Known, documented exceptions live in scripts/check_allow.json.
"""
import glob, json, os, re, sys, urllib.request, urllib.error, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EXT = (".safetensors", ".gguf", ".pt", ".pth", ".bin", ".ckpt", ".onnx")
ALLOW = json.load(open(os.path.join(HERE, "check_allow.json"), encoding="utf-8"))
problems = []


def bad(where, msg):
    problems.append(f"{where}: {msg}")


def norm_pack(s):
    s = s.split("/")[-1].lower()
    return re.sub(r"^comfyui[-_]", "", s).replace("_", "-")


def walk_json(wf):
    nodes = list(wf.get("nodes", []))
    for sg in (wf.get("definitions") or {}).get("subgraphs", []):
        nodes += sg.get("nodes", [])
    models, packs = [], set()
    for n in nodes:
        def rec(x):
            if isinstance(x, str) and x.lower().endswith(EXT):
                models.append(x.replace("\\", "/").split("/")[-1])
            elif isinstance(x, (list, tuple)):
                for y in x: rec(y)
            elif isinstance(x, dict):
                for y in x.values(): rec(y)
        rec(n.get("widgets_values"))
        p = n.get("properties") or {}
        pid = p.get("cnr_id") or p.get("aux_id")
        if pid and pid != "comfy-core":
            packs.add(pid)
    return models, packs


root = open(os.path.join(REPO, "README.md"), encoding="utf-8").read()
folders = sorted(os.path.relpath(d, os.path.join(REPO, "workflows")).replace("\\", "/")
                 for d in glob.glob(os.path.join(REPO, "workflows", "*", "*")) if os.path.isdir(d))
m = re.search(r"workflows-(\d+)-", root)
if m and int(m.group(1)) != len(folders):
    bad("README", f"badge says {m.group(1)} workflows, there are {len(folders)}")
urls = []
for f in folders:
    d = os.path.join(REPO, "workflows", f)
    allow = set(ALLOW.get("*", {})) | set(ALLOW.get(f, {}))
    jsons = sorted(glob.glob(os.path.join(d, "The_frizzy1_*.json")))
    vers = {re.search(r"_v(\d+\.\d+\.\d+)\.json$", j).group(1) for j in jsons}
    ver = max(vers, key=lambda v: tuple(map(int, v.split(".")))) if vers else "?"
    rows = [l for l in root.splitlines() if l.startswith("|") and f"(workflows/{f})" in l]
    if not rows:
        bad(f, "not in the root README tables")
    for l in rows:
        mv = re.search(r"\|\s*v(\d+\.\d+\.\d+)\s*\|", l)
        if mv and mv.group(1) != ver:
            bad(f, f"root README says v{mv.group(1)}, the .json is v{ver}")
    cl = open(os.path.join(d, "changelog.md"), encoding="utf-8").read() if os.path.exists(os.path.join(d, "changelog.md")) else ""
    mc = re.search(r"(\d+\.\d+\.\d+)", cl)
    if not mc or mc.group(1) != ver:
        bad(f, f"changelog top version {mc.group(1) if mc else '?'} != .json v{ver}")
    readme = open(os.path.join(d, "README.md"), encoding="utf-8").read()
    for j in jsons:
        if os.path.basename(j) not in readme:
            bad(f, f"README doesn't name {os.path.basename(j)}")
    mj = json.load(open(os.path.join(d, "models.json"), encoding="utf-8"))
    listed = {s["name"]: s for s in mj["files"]}
    dl = open(os.path.join(d, "downloads.md"), encoding="utf-8").read()
    used, packs = set(), set()
    for j in jsons:
        u, p = walk_json(json.load(open(j, encoding="utf-8")))
        used |= set(u); packs |= p
    for nm in sorted(used - set(listed) - allow):
        bad(f, f"the .json loads {nm} but models.json doesn't list it")
    for nm in sorted(used - allow):
        if nm not in dl:
            bad(f, f"the .json loads {nm} but downloads.md doesn't name it")
    for nm, s in listed.items():
        if nm not in used and s.get("required") and not s.get("manual"):
            bad(f, f"models.json requires {nm} but the .json never loads it")
        if s.get("url"):
            urls.append((f, nm, s["url"]))
        elif not s.get("page"):
            bad(f, f"models.json entry {nm} has neither url nor page")
    have = {norm_pack(n["name"]) for n in mj.get("nodes", [])}
    for p in sorted(packs):
        if norm_pack(p) not in have:
            bad(f, f"the .json uses node pack '{p}', models.json nodes doesn't list it")

if "--links" in sys.argv:
    def head(it):
        f, nm, u = it
        try:
            return f, nm, urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30).status
        except urllib.error.HTTPError as e:
            return f, nm, e.code
        except Exception as e:
            return f, nm, str(e)[:40]
    with cf.ThreadPoolExecutor(12) as ex:
        res = list(ex.map(head, urls))
    gated = [r for r in res if r[2] == 401]
    for f, nm, st in res:
        if st not in (200, 302, 401):
            bad(f, f"link for {nm} answers {st}")
    print(f"{len(res)} links checked, {len(gated)} gated (accept the license + HF_TOKEN)")

print(f"{len(folders)} workflows, {len(problems)} problems")
for p in problems:
    print("  -", p)
sys.exit(1 if problems else 0)

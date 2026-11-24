#!/usr/bin/env python3
"""Shared helpers: build a flat UI workflow from /object_info, and convert a flat UI workflow to an API prompt."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OI = json.load(open(os.path.join(HERE, "object_info.json")))
WIDGET_T = {"INT", "FLOAT", "STRING", "BOOLEAN", "COMBO", "COMFY_DYNAMICCOMBO_V3"}
CORE_VER = "0.45.3"


def is_widget(v):
    return isinstance(v[0], list) or v[0] in WIDGET_T


def opts_of(v):
    return v[1] if len(v) > 1 and isinstance(v[1], dict) else {}


def spec_of(info):
    return list(info["input"].get("required", {}).items()) + list(info["input"].get("optional", {}).items())


def walk_widgets(spec, vals, i=0, prefix=""):
    """Yield (full_name, spec_entry, value) for every widget in UI order, following dynamic combos. Returns via list."""
    out = []
    for k, v in spec:
        o = opts_of(v)
        if o.get("hidden") or o.get("socketless") or not is_widget(v):
            continue
        name = prefix + k
        if i < len(vals):
            val = vals[i]
        else:
            val = o.get("default", v[0][0] if isinstance(v[0], list) else (o["options"][0]["key"] if v[0] == "COMFY_DYNAMICCOMBO_V3" else None))
        i += 1
        out.append((name, v, val))
        if o.get("control_after_generate"):
            i += 1
        if v[0] == "COMFY_DYNAMICCOMBO_V3":
            opt = next(x for x in o["options"] if x["key"] == val)
            sub = list(opt["inputs"].get("required", {}).items()) + list(opt["inputs"].get("optional", {}).items())
            more, i = walk_widgets(sub, vals, i, name + ".")
            out += more
    return out, i


class Graph:
    def __init__(self, files):
        self.nodes, self.links, self.groups = [], [], []
        self.nid = self.lid = 0
        self.files = files

    def node(self, typ, pos, size, widgets=None, title=None, models=None, **inputs):
        """inputs: name=(source_node, source_slot) for every linked input; dots in names are written as __."""
        inputs = {k.replace("__", "."): v for k, v in inputs.items()}
        self.nid += 1
        n = {"id": self.nid, "type": typ, "pos": list(pos), "size": list(size), "flags": {}, "order": len(self.nodes),
             "mode": 0, "inputs": [], "outputs": [], "properties": {"Node name for S&R": typ}}
        if title:
            n["title"] = title
        if typ != "MarkdownNote":
            n["properties"].update({"cnr_id": "comfy-core", "ver": CORE_VER})
        if models:
            n["properties"]["models"] = [{"name": self.files[m][0], "url": self.files[m][1], "directory": self.files[m][2]} for m in models]
        if typ != "MarkdownNote":
            info = OI[typ]
            spec = spec_of(info)
            opt = set(info["input"].get("optional", {}))
            entries = []
            for k, v in spec:
                o = opts_of(v)
                if o.get("hidden") or o.get("socketless") or is_widget(v):
                    continue
                t = v[0]
                if t == "COMFY_AUTOGROW_V3":
                    # first slot of an autogrow input, "<input>.<first name>" (e.g. images.image1)
                    tpl = o["template"]
                    sub = {**tpl["input"].get("required", {}), **tpl["input"].get("optional", {})}
                    first = tpl["names"][0] if "names" in tpl else tpl["prefix"] + "0"
                    slots = sorted({nm.split(".", 1)[1] for nm in inputs if nm.startswith(k + ".")}) or [first]
                    for sl in slots:
                        entries.append({"localized_name": sl, "name": f"{k}.{sl}", "type": next(iter(sub.values()))[0], "shape": 7})
                    continue
                if t == "COMFY_MATCHTYPE_V3":
                    t = o.get("template", {}).get("allowed_types", "*")
                e = {"localized_name": k, "name": k, "type": t}
                if k in opt:
                    e["shape"] = 7
                entries.append(e)
            ws, _ = walk_widgets(spec, list(widgets or []))
            for name, v, _val in ws:
                e = {"localized_name": name.split(".")[-1], "name": name, "type": "COMBO" if isinstance(v[0], list) else v[0],
                     "widget": {"name": name}}
                if name in opt:
                    e["shape"] = 7
                entries.append(e)
            for e in entries:
                e["link"] = None
                if e["name"] in inputs:
                    src, slot = inputs.pop(e["name"])
                    self.lid += 1
                    e["link"] = self.lid
                    out = src["outputs"][slot]
                    out["links"] = (out["links"] or []) + [self.lid]
                    self.links.append([self.lid, src["id"], slot, n["id"], len(n["inputs"]), out["type"]])
                n["inputs"].append(e)
            assert not inputs, (typ, inputs)
            names = info.get("output_name") or info["output"]
            lists = info.get("output_is_list") or [False] * len(names)
            for t, nm, il in zip(info["output"], names, lists):
                t = t if isinstance(t, str) else "COMBO"
                if t == "COMFY_MATCHTYPE_V3":
                    t = "IMAGE" if typ == "ResizeImageMaskNode" else "*"
                o = {"localized_name": nm, "name": nm, "type": t, "links": None}
                if il:
                    o["shape"] = 6
                n["outputs"].append(o)
        if widgets is not None:
            n["widgets_values"] = widgets
        self.nodes.append(n)
        return n

    def group(self, title, bounding, color):
        self.groups.append({"id": len(self.groups) + 1, "title": title, "bounding": bounding, "color": color, "font_size": 24, "flags": {}})

    def col(self, x, y, w, items):
        """Stack nodes in a column; items = (type, height, kwargs). Returns the nodes and the bottom y."""
        out = []
        for typ, h, kw in items:
            out.append(self.node(typ, (x, y), (w, h), **kw))
            y += h + 50
        return out, y

    def dump(self, wid):
        return {"id": wid, "revision": 0, "last_node_id": self.nid, "last_link_id": self.lid, "nodes": self.nodes,
                "links": self.links, "groups": self.groups, "config": {}, "extra": {"ds": {"scale": 0.55, "offset": [760, 120]}},
                "version": 0.4}


def to_api(wf, overrides=None):
    """Flat UI workflow -> API prompt. overrides: {node title prefix: value for widget 0}."""
    overrides = overrides or {}
    links = {l[0]: l for l in wf["links"]}
    prompt = {}
    for n in wf["nodes"]:
        if n["type"] in ("MarkdownNote", "Note") or n.get("mode", 0) != 0:
            continue
        spec = spec_of(OI[n["type"]])
        vals = list(n.get("widgets_values") or [])
        for k, v in overrides.items():
            if n.get("title", "").startswith(k):
                vals[0] = type(vals[0])(v) if not isinstance(vals[0], str) else v
        ws, _ = walk_widgets(spec, vals)
        inputs = {name: val for name, _v, val in ws if val is not None}
        for e in n["inputs"]:
            if e.get("link") is not None:
                l = links[e["link"]]
                inputs[e["name"]] = [str(l[1]), l[2]]
        if n["type"] == "ImageCompare":
            # compare_view is the frontend's slider widget (socketless, required); the browser fills it in, the API needs a stand-in
            inputs["compare_view"] = {"__value__": ["", ""]}
        prompt[str(n["id"])] = {"class_type": n["type"], "inputs": inputs, "_meta": {"title": n.get("title", n["type"])}}
    return prompt

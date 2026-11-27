"""Builds the v2.0.0 edit and area-edit files from the v1.0.0 files, in the text-to-image v2.0.0 layout:
one big node (a subgraph) with every setting on it, the picture loaders on the left, the results on the right.
Inside the node nothing changes: the same nodes, links, values and groups as v1.0.0.
  python make_v2_edits.py        (run in this folder; reads ../*_v1.0.0.json, writes ../*_v2.0.0.json)
"""
import copy, json, os, uuid

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.dirname(HERE)
NS = uuid.UUID("6d1f4a52-6a3b-4c39-9a0e-3e1d2b7f0a11")
uid = lambda s: str(uuid.uuid5(NS, s))

MODELS = [("unet", "Model", 0), ("te", "Text encoder", 0), ("vae", "VAE", 0)]   # name, label, widget slot

SPECS = {
    "edit": dict(
        src="The_frizzy1_h3-image-12gb-edit_v1.0.0.json", dst="The_frizzy1_h3-image-12gb-edit_v2.0.0.json",
        title="MiniMax H3 Image (edit)",
        outside_left=[1, 3], outside_right=[19, 20],           # loaders | before/after, save
        settings=[(4, "prompt"), (2, "use_picture_2"), (5, "megapixels"), (6, "seed")],
        loaders={"unet": 7, "te": 8, "vae": 9},
        image_inputs={(1, 0): ("picture_1", "Picture 1"), (3, 0): ("picture_2", "Picture 2")},
        outputs_label={"IMAGE": ("image", "Result")},
    ),
    "area": dict(
        src="The_frizzy1_h3-image-12gb-area-edit_v1.0.0.json", dst="The_frizzy1_h3-image-12gb-area-edit_v2.0.0.json",
        title="MiniMax H3 Image (area edit)",
        outside_left=[1], outside_right=[33, 35, 36],
        settings=[(2, "prompt"), (3, "use_painted_mask"), (4, "box_left"), (5, "box_top"), (6, "box_width"),
                  (7, "box_height"), (8, "megapixels"), (9, "seed")],
        loaders={"unet": 10, "te": 11, "vae": 12},
        image_inputs={(1, 0): ("picture", "Your picture"), (1, 1): ("painted_mask", "Painted mask")},
        outputs_label={"IMAGE": ("image", "Result"), "MASK": ("area", "Area that changes")},
    ),
}

HOWTO = {
    "edit": """## How to use Â· v2.0.0

**What it does:** edits a picture from a written instruction with MiniMax H3 Image, on the 12 GB files; a second picture can be a reference (a face, an object, a style). Core ComfyUI nodes only.

**One node.** Everything you set is on the big **MiniMax H3 Image (edit)** node. The pictures go in on the left, the result comes out on the right. Double-click the node's title bar to see the inside (the same nodes as v1.0.0).

1. **Picture 1** (left): the picture to edit. Set to `example.png` (ships with ComfyUI); the default instruction is written for it, so the first Run works.
2. **Picture 2** (left): only used when **Use Picture 2** is on. Must point to a file that exists either way.
3. On the node:
   - **Edit instruction**: what to change, naming the pictures as `<Picture 1>` and `<Picture 2>`. Short and direct works; say what must stay.
   - **Use Picture 2**: off by default.
   - **Megapixels** (4): size of the result. Picture 1 is resized to this many pixels, shape kept, sides on a 32 px grid.
   - **Seed**: fixed. Type a new number for another take.
   - **Model / Text encoder / VAE**: the three files from the Downloads note.
4. Press **Run**. **Before / after** shows both; **Result** saves to `output/MiniMax-H3-Image/`.
""",
    "area": """## How to use Â· v2.0.0

**What it does:** changes only one area of a picture (a box, or a mask you paint) from a written instruction with MiniMax H3 Image, on the 12 GB files. Everything outside the area stays the original. Core ComfyUI nodes only.

**One node.** Everything you set is on the big **MiniMax H3 Image (area edit)** node. The picture goes in on the left, the result and the area come out on the right. Double-click the node's title bar to see the inside (the same nodes as v1.0.0).

1. **Your picture** (left): set to `example.png` (ships with ComfyUI); the default box and instruction are written for it, so the first Run works. To paint the area: right-click the picture â†’ **Open in MaskEditor**, paint, Save, and turn **Use my painted mask** on.
2. On the node:
   - **Edit instruction**: what goes in the area. Name the picture as `<Picture 1>`.
   - **Use my painted mask**: off = the box below.
   - **Box left / top / width / height**: in percent of the picture (default 15/0/70/45). Cover the whole old object with room around it.
   - **Megapixels for the edit** (4): the size the model works at. The result keeps your picture's own size.
   - **Seed**: fixed. Type a new number for another take.
   - **Model / Text encoder / VAE**: the three files from the Downloads note.
3. Press **Run**. **Before / after** shows both, **Area that changes** shows the mask; **Result** saves to `output/MiniMax-H3-Image/`.
""",
}


def build(kind):
    s = SPECS[kind]
    w = json.load(open(os.path.join(UP, s["src"]), encoding="utf-8-sig"))
    nodes = {n["id"]: n for n in w["nodes"]}
    notes_out = [n["id"] for n in w["nodes"] if n["type"] == "MarkdownNote" and n["pos"][0] < -100]
    outside = set(s["outside_left"]) | set(s["outside_right"]) | set(notes_out)
    inner = [copy.deepcopy(n) for n in w["nodes"] if n["id"] not in outside]
    inner_ids = {n["id"] for n in inner}
    L = [dict(zip(["id", "origin_id", "origin_slot", "target_id", "target_slot", "type"], l)) for l in w["links"]]

    sg_id = uid(kind + "-subgraph")
    sg_inputs, sg_outputs, sg_links, top_links = [], [], [], []
    host_inputs, host_outputs, host_wv = [], [], []
    lid = [0]
    def new_link():
        lid[0] += 1; return lid[0]
    for n in inner:                                  # links get rebuilt from scratch
        for i in n.get("inputs", []): i["link"] = None
        for o in n.get("outputs", []): o["links"] = []
    inn = {n["id"]: n for n in inner}

    # links fully inside stay
    for l in L:
        if l["origin_id"] in inner_ids and l["target_id"] in inner_ids:
            k = new_link()
            sg_links.append({**l, "id": k})
            inn[l["target_id"]]["inputs"][l["target_slot"]]["link"] = k
            inn[l["origin_id"]]["outputs"][l["origin_slot"]]["links"].append(k)

    HOST = 100                                       # host node id on the top level
    # 1. picture inputs: outer loader -> inner node becomes loader -> host input -> inner node
    for (src, slot), (name, label) in s["image_inputs"].items():
        typ = nodes[src]["outputs"][slot]["type"]
        idx = len(sg_inputs)
        ids = []
        for l in L:
            if l["origin_id"] == src and l["origin_slot"] == slot and l["target_id"] in inner_ids:
                k = new_link(); ids.append(k)
                sg_links.append({"id": k, "origin_id": -10, "origin_slot": idx, "target_id": l["target_id"],
                                 "target_slot": l["target_slot"], "type": typ})
                inn[l["target_id"]]["inputs"][l["target_slot"]]["link"] = k
        sg_inputs.append({"id": uid(kind + name), "name": name, "type": typ, "linkIds": ids, "label": label,
                          "localized_name": name, "pos": [0, 0]})
        host_inputs.append({"label": label, "localized_name": name, "name": name, "type": typ, "link": None})
    # 2. settings: host widget -> the primitive's value widget inside
    def widget_input(nid, slot, name, label):
        n = inn[nid]; inp = n["inputs"][slot]; typ = inp["type"]
        k = new_link(); idx = len(sg_inputs)
        sg_links.append({"id": k, "origin_id": -10, "origin_slot": idx, "target_id": nid, "target_slot": slot, "type": typ})
        inp["link"] = k
        sg_inputs.append({"id": uid(kind + name), "name": name, "type": typ, "linkIds": [k], "label": label,
                          "localized_name": name, "pos": [0, 0]})
        host_inputs.append({"label": label, "localized_name": name, "name": name, "type": typ, "link": None,
                            "widget": {"name": name}})
        host_wv.append(n["widgets_values"][slot])
    for nid, name in s["settings"]:
        n = inn[nid]
        n["inputs"][0].pop("label", None)
        widget_input(nid, 0, name, n["title"])
    for name, label, slot in MODELS:
        widget_input(s["loaders"][name], slot, name, label)

    # 3. outputs: inner -> outer becomes inner -> host output -> outer
    out_by_origin = {}
    for l in L:
        if l["origin_id"] in inner_ids and l["target_id"] in outside:
            key = (l["origin_id"], l["origin_slot"])
            if key not in out_by_origin:
                typ = l["type"]; name, label = s["outputs_label"][typ]
                if typ == "IMAGE" and nodes[l["target_id"]]["type"] != "SaveImage" and not any(
                        x["origin_id"] == l["origin_id"] and nodes.get(x["target_id"], {}).get("type") == "SaveImage" for x in L):
                    name, label = "before", "Before (Picture 1, resized)"
                k = new_link()
                sg_links.append({"id": k, "origin_id": l["origin_id"], "origin_slot": l["origin_slot"], "target_id": -20,
                                 "target_slot": len(sg_outputs), "type": typ})
                inn[l["origin_id"]]["outputs"][l["origin_slot"]]["links"].append(k)
                out_by_origin[key] = len(sg_outputs)
                sg_outputs.append({"id": uid(kind + name), "name": name, "type": typ, "linkIds": [k], "label": label,
                                   "localized_name": name, "pos": [0, 0]})
                host_outputs.append({"label": label, "localized_name": name, "name": name, "type": typ, "links": []})

    # inner layout: v1.0.0 positions; the settings group says it is shown outside
    groups = copy.deepcopy(w["groups"])
    groups[0]["title"] = "Settings (shown on the node outside)"
    x_max = max(n["pos"][0] + n["size"][0] for n in inner)
    sg = {
        "id": sg_id, "version": 1,
        "state": {"lastGroupId": len(groups), "lastNodeId": max(inner_ids), "lastLinkId": lid[0], "lastRerouteId": 0},
        "revision": 0, "config": {}, "name": s["title"],
        "inputNode": {"id": -10, "bounding": [-420, 0, 160, 60 + 26 * len(sg_inputs)]},
        "outputNode": {"id": -20, "bounding": [x_max + 80, 0, 160, 60 + 26 * len(sg_outputs)]},
        "inputs": sg_inputs, "outputs": sg_outputs, "widgets": [], "nodes": inner, "groups": groups,
        "links": sg_links, "extra": {},
    }

    # top level: loaders left, host, results right, the two notes far left
    top_nodes = []
    y = 0
    for nid in s["outside_left"]:
        n = copy.deepcopy(nodes[nid]); n["pos"] = [-600, y]; n["size"] = [520, 560]; y += 620
        for o in n["outputs"]: o["links"] = []
        top_nodes.append(n)
    tl = [0]
    def tlink(o, os_, t, ts, typ):
        tl[0] += 1; top_links.append([tl[0], o, os_, t, ts, typ]); return tl[0]
    tn = {n["id"]: n for n in top_nodes}
    for i, ((src, slot), _) in enumerate(s["image_inputs"].items()):
        k = tlink(src, slot, HOST, i, host_inputs[i]["type"])
        host_inputs[i]["link"] = k; tn[src]["outputs"][slot]["links"].append(k)
    host = {
        "id": HOST, "type": sg_id, "pos": [0, 0], "size": [560, 140 + 52 * len(host_wv) + 26 * len(s["image_inputs"])],
        "flags": {}, "order": 0, "mode": 0, "inputs": host_inputs, "outputs": host_outputs, "title": s["title"],
        "properties": {"models": next(n["properties"]["models"] for n in inner if n["type"] == "UNETLoader" and "models" in n["properties"])
                       if any("models" in n.get("properties", {}) for n in inner) else []},
        "widgets_values": host_wv, "color": "#232", "bgcolor": "#353",
    }
    all_models = [m for n in inner for m in n.get("properties", {}).get("models", [])]
    if all_models: host["properties"] = {"models": all_models}
    top_nodes.append(host)
    x = 640                                          # Result first, Before / after beside it, the area under the result
    for nid in s["outside_right"]:
        n = copy.deepcopy(nodes[nid])
        if n["type"] == "MaskPreview": n["pos"], n["size"] = [640, 700], [400, 320]
        else: n["size"] = [620, 640]; n["pos"] = [x if n["type"] == "SaveImage" else x + 680, 0]
        for i in n.get("inputs", []):
            if "widget" not in i: i["link"] = None
        tn[nid] = n; top_nodes.append(n)
    for l in L:                                      # inner -> outer links now come from the host
        if l["origin_id"] in inner_ids and l["target_id"] in outside:
            o = out_by_origin[(l["origin_id"], l["origin_slot"])]
            k = tlink(HOST, o, l["target_id"], l["target_slot"], l["type"])
            host_outputs[o]["links"].append(k); tn[l["target_id"]]["inputs"][l["target_slot"]]["link"] = k
        if l["origin_id"] in outside and l["target_id"] in outside:      # loader -> before/after stays direct
            k = tlink(l["origin_id"], l["origin_slot"], l["target_id"], l["target_slot"], l["type"])
            tn[l["origin_id"]]["outputs"][l["origin_slot"]]["links"].append(k); tn[l["target_id"]]["inputs"][l["target_slot"]]["link"] = k
    for nid in notes_out:
        n = copy.deepcopy(nodes[nid]); top_nodes.append(n)
        n["pos"] = [-1300, 0 if "How to use" in n["title"] else 920]
        if "How to use" in n["title"]:
            n["title"] = "How to use Â· v2.0.0"; n["widgets_values"] = [HOWTO[kind]]
    for o, n in enumerate(top_nodes): n["order"] = o

    hidx = {i["name"]: k for k, i in enumerate(host_inputs)}
    out = {
        "id": uid(kind + "-workflow"), "revision": 0, "last_node_id": max(n["id"] for n in top_nodes),
        "last_link_id": tl[0], "nodes": top_nodes, "links": top_links, "groups": [],
        "definitions": {"subgraphs": [sg]}, "config": {},
        "extra": {"ds": {"scale": 0.6, "offset": [900, 120]},
                  "linearData": {"inputs": [[nid, "image"] for nid in s["outside_left"]] +
                                           [[HOST, name] for nid, name in s["settings"]],
                                 "outputs": [s["outside_right"][-1]]}},
        "version": 0.4,
    }
    json.dump(out, open(os.path.join(UP, s["dst"]), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
    print(s["dst"], "inputs:", [i["name"] for i in host_inputs], "outputs:", [o["name"] for o in host_outputs],
          "inner nodes:", len(inner), "inner links:", len(sg_links), "top links:", len(top_links))

for k in SPECS: build(k)



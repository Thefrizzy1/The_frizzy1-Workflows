"""The_frizzy1 AI Influencer workflows (12 GB), MiniMax H3 Image, core nodes only, no prompt-enhancer model.

  1 character : text -> her first image.
  2 scenes    : her picture (+ an optional second picture, e.g. a frame of your video) + text -> her in a new scene.

  python build_influencer.py api   character|scenes OUT.json     -> API json (titled nodes) to load in the ComfyUI frontend
  python build_influencer.py polish character|scenes UI.json OUT.json  -> the shareable workflow (groups, notes, App mode)
"""
import json, sys, uuid

VERSION = "1.0.0"
TESTED = "RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.45.0 · Windows 11"
UNET = "minimax_h3_image_pruned_w4a8.safetensors"
CLIP = "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"
VAE = "minimax_h3_image_vae_fp16.safetensors"
C = "https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main"
LINKS = [
    ("diffusion_models", UNET, f"{C}/diffusion_models/{UNET}", "12.5 GB"),
    ("text_encoders", CLIP, f"{C}/text_encoders/{CLIP}", "15.7 GB"),
    ("vae", VAE, f"{C}/vae/{VAE}", "1.2 GB"),
]

CHARACTER_PROMPT = open(__file__.replace("build_influencer.py", "prompts/hero_v3_blue.txt"), encoding="utf-8").read().strip()
SCENE_PROMPT = ("The woman from <Picture 1>, the same person with the same face, the same hair, the same sunglasses, piercings and tattoos, "
                "now sits at a small table by the window of a cosy coffee shop in daylight. She wears an oversized cream knit sweater and holds a plain "
                "white takeaway coffee cup with both hands. Warm morning light from the window, plants and a brick wall softly out of focus behind her, "
                "a cheeky smile, looking into the camera. Candid social media photo, 35mm lens, natural skin texture.")

SPEC = {
    "character": dict(
        name="The_frizzy1 · AI Influencer 1 · Create the character · 12 GB", slug="ai-influencer-1-character-12gb", prefix="AI influencer/character",
        prompt=CHARACTER_PROMPT, aspect="3:4 (Portrait Standard)", mp=7.5, refs=0),
    "scenes": dict(
        name="The_frizzy1 · AI Influencer 2 · Same face, new scene · 12 GB", slug="ai-influencer-2-scenes-12gb", prefix="AI influencer/scene",
        prompt=SCENE_PROMPT, aspect="3:4 (Portrait Standard)", mp=7.5, refs=2),
}


def build(kind):
    s, g = SPEC[kind], {}

    def n(i, cls, title=None, **inp):
        g[str(i)] = {"class_type": cls, "inputs": inp}
        if title:
            g[str(i)]["_meta"] = {"title": title}
        return str(i)

    n(1, "PrimitiveStringMultiline", "Prompt (describe her and the scene)", value=s["prompt"])
    n(2, "ResolutionSelector", "Size (4 MP fast, 7.5 MP better face, 16 MP max)", aspect_ratio=s["aspect"], megapixels=s["mp"], multiple=32)
    n(3, "PrimitiveInt", "Seed (change it for another take)", value=7)
    n(10, "UNETLoader", "H3 Image model", unet_name=UNET, weight_dtype="default")
    n(11, "CLIPLoader", "H3 text encoder", clip_name=CLIP, type="minimax", device="default")
    n(12, "VAELoader", "H3 Image VAE", vae_name=VAE)
    cond = dict(clip=["11", 0], vae=["12", 0], prompt=["1", 0], width=["2", 0], height=["2", 1])
    if s["refs"]:
        n(4, "LoadImage", "Picture 1: her face (big and sharp)", image="her_reference.png")
        n(5, "LoadImage", "Picture 2 (optional): a frame or scene to put her in", image="your_frame.png")
        cond["images.image_1"], cond["images.image_2"] = ["4", 0], ["5", 0]
    n(20, "MiniMaxH3ImageConditioning", "Prompt + pictures", **cond)
    n(21, "ConditioningZeroOut", "Empty negative", conditioning=["20", 0])
    n(22, "KSampler", "Sampler (6 steps)", model=["10", 0], positive=["20", 0], negative=["21", 0], latent_image=["20", 1],
      seed=["3", 0], steps=6, cfg=1, sampler_name="euler", scheduler="simple", denoise=1)
    n(23, "VAEDecode", "Decode", samples=["22", 0], vae=["12", 0])
    n(24, "SaveImage", "Result", images=["23", 0], filename_prefix=s["prefix"])
    return g


HOW_TO = {
    "character": """# NAME · vVERSION

Makes the **first image of an invented person** from a text prompt. This is workflow 1 of 2: use the result as *Picture 1* in workflow 2.

## How to use (App mode)
1. **Prompt**: describe her like a photo caption: who, hair, glasses, jewellery, outfit, place, light, lens. Long prompts work best.
2. **Size**: 3:4 at 7.5 MP is what I used. 4 MP is faster. Below 4 MP the face gets soft.
3. **Seed**: same prompt + another seed = another person. Run a few and keep the one you like.
4. Press **Run**. The result lands in `output/AI influencer/`.

## Tip
For the reference you reuse later, make a **close-up with both eyes visible**. A half-body shot gives the face too few pixels.

## Speed
SPEED_LINE

## Credits
MiniMax H3 Image by MiniMax. Workflow by **The_frizzy1**: [YouTube](https://www.youtube.com/@the_frizzy1) · [workflows](https://github.com/Thefrizzy1/The_frizzy1-Workflows).
""",
    "scenes": """# NAME · vVERSION

Puts **the same person** into a **new scene, outfit or pose**. This is workflow 2 of 2: *Picture 1* is the image from workflow 1.

## How to use (App mode)
1. **Picture 1**: her reference, a sharp close-up of the face.
2. **Picture 2 (optional)**: a frame of your own video or a place. **Not needed? Bypass that node** (select it, Ctrl+B).
3. **Prompt**: start with *The woman from <Picture 1>, the same person with the same face...* and then describe the new scene and outfit.
   With Picture 2: *Replace the man in <Picture 1>...* style prompts work too, name each picture by its number.
4. **Size**: match the shape of the result you want. For a video frame pick 16:9.
5. **Seed**: change it for another take.
6. Press **Run**. The result lands in `output/AI influencer/`.

## For video
Swap her into one frame of your clip with Picture 2, then give that frame to a video model as the keyframe
(I used Viggle Remake, 124 frames at 832x480).

## Speed
SPEED_LINE

## Credits
MiniMax H3 Image by MiniMax. Workflow by **The_frizzy1**: [YouTube](https://www.youtube.com/@the_frizzy1) · [workflows](https://github.com/Thefrizzy1/The_frizzy1-Workflows).
""",
}
ROWS = chr(10).join(f"| `{d}/` | [{f}]({u}) | {z} |" for d, f, u, z in LINKS)
DOWNLOADS = f"""# Downloads · put each file in the folder shown

Inside `ComfyUI/models/`. Click a file name to download it.

| Folder | File (click = download) | Size |
|---|---|---|
{ROWS}

Total: 29.4 GB. Both AI Influencer workflows use the same three files. If you already run MiniMax H3 video, you have the text encoder.

**Custom nodes: none.** Core nodes only.

## Requirements
- **GPU:** 12 GB VRAM tested (peak about 11.6 GB).
- **RAM:** 32 GB tested (peak about 17 GB for text to image, about 21 to 22 GB with pictures).
- **ComfyUI:** 0.45.0 tested. Older versions do not have the MiniMax H3 Image node.

_Tested on: {TESTED}._

MiniMax H3 Image is released under the MiniMax-H3-Image Community License Agreement.
"""
GROUPS = {
    "character": [("1 · Your inputs (App mode shows these)", "#8A8", [[1], [2, 3]]),
                  ("2 · Models (loaded once)", "#b58b2a", [[10, 11, 12]]),
                  ("3 · Make the image", "#b06634", [[20, 21], [22], [23], [24]])],
    "scenes": [("1 · Your inputs (App mode shows these)", "#8A8", [[4], [5], [1], [2, 3]]),
               ("2 · Models (loaded once)", "#b58b2a", [[10, 11, 12]]),
               ("3 · Make the image", "#b06634", [[20, 21], [22], [23], [24]])],
}
INPUTS = {"character": [["1", "value"], ["2", "aspect_ratio"], ["2", "megapixels"], ["3", "value"]],
          "scenes": [["4", "image"], ["5", "image"], ["1", "value"], ["2", "aspect_ratio"], ["2", "megapixels"], ["3", "value"]]}
GREEN = ("#232", "#353")
TITLE_H, GAP, PAD, HEAD = 30, 70, 40, 60


def polish(kind, src, out, speed):
    s = SPEC[kind]
    w = json.load(open(src, encoding="utf-8"))
    nodes = {nd["id"]: nd for nd in w["nodes"]}
    for i in [int(a) for a, _ in INPUTS[kind]] + [24]:
        nodes[i]["color"], nodes[i]["bgcolor"] = GREEN
    for nd in nodes.values():
        for inp in nd.get("inputs", []):
            if inp.get("widget") and [str(nd["id"]), inp["name"]] in INPUTS[kind] and nd["type"] != "ResolutionSelector":
                inp["label"] = nd["title"]
    if kind == "scenes":
        nodes[5]["mode"] = 4  # Picture 2 ships bypassed: one picture is the normal case

    def note(nid, title, text, x, y, wd, ht):
        return {"id": nid, "type": "MarkdownNote", "pos": [x, y], "size": [wd, ht], "flags": {}, "order": 0, "mode": 0, "inputs": [],
                "outputs": [], "title": title, "properties": {}, "widgets_values": [text], "color": "#432", "bgcolor": "#653"}

    nid = max(nodes) + 1
    how = HOW_TO[kind].replace("NAME", s["name"]).replace("VERSION", VERSION).replace("SPEED_LINE", speed)
    notes = [note(nid, f"How to use · v{VERSION}", how, 0, 0, 620, 760), note(nid + 1, "Downloads + requirements", DOWNLOADS, 660, 0, 760, 760)]
    x, groups = 1500, []
    for title, color, cols in GROUPS[kind]:
        gx, bottom = x, 0
        for col in cols:
            y = HEAD + TITLE_H
            for i in col:
                nodes[i]["pos"] = [x + PAD, y]
                y += nodes[i]["size"][1] + TITLE_H + GAP
            bottom = max(bottom, y)
            x += max(nodes[i]["size"][0] for i in col) + GAP + 10
        groups.append({"id": len(groups) + 1, "title": title, "color": color, "font_size": 28, "flags": {},
                       "bounding": [gx, 0, x - gx + 2 * PAD - GAP, bottom + PAD]})
        x += 2 * PAD + 40
    w["nodes"] = list(nodes.values()) + notes
    w["groups"] = groups
    w["last_node_id"] = max(n["id"] for n in w["nodes"])
    w["id"] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"the_frizzy1/{s['slug']}/{VERSION}"))
    w["revision"] = 0
    w.setdefault("extra", {}).update(linearMode=True, linearData={"inputs": INPUTS[kind], "outputs": ["24"]}, ds={"scale": 0.6, "offset": [60, 80]},
                                     frizzy={"name": s["name"], "version": VERSION, "tested_on": TESTED})
    w["models"] = [{"name": f, "url": u, "directory": d} for d, f, u, _ in LINKS]
    w.setdefault("extensions", {})["models"] = w["models"]
    json.dump(w, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out, len(w["nodes"]), "nodes,", len(groups), "groups")


if __name__ == "__main__":
    mode, kind = sys.argv[1], sys.argv[2]
    if mode == "api":
        json.dump(build(kind), open(sys.argv[3], "w", encoding="utf-8"), indent=1)
        print("wrote", sys.argv[3])
    else:
        polish(kind, sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")

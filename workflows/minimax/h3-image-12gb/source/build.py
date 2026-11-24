#!/usr/bin/env python3
"""Builds the three MiniMax H3 Image · 12 GB workflows (UI format): text to image, edit, area edit.
Flat rebuilds of the built-in templates image_minimax_h3_image_t2i / image_minimax_h3_image_edit (template pack 0.11.104+),
on the 12 GB files (W4A8 model, NVFP4 text encoder), without the Qwen3.5 prompt expander.
Run: python build.py <out_dir>   (measured.json, when present, fills the notes)"""
import json, os, sys
from lib import Graph

VER = "1.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))
HF = "https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/"
FILES = {
    "unet": ("minimax_h3_image_pruned_w4a8.safetensors", HF + "diffusion_models/minimax_h3_image_pruned_w4a8.safetensors", "diffusion_models", "12.5 GB"),
    "te": ("qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", HF + "text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "text_encoders", "15.7 GB"),
    "vae": ("minimax_h3_image_vae_fp16.safetensors", HF + "vae/minimax_h3_image_vae_fp16.safetensors", "vae", "1.2 GB"),
}
C_IN, C_MODEL, C_PROMPT, C_SAMPLE, C_AREA, C_SAVE = "#8A8", "#3f789e", "#a1309b", "#b06634", "#2a7f7f", "#b58b2a"

M = {"t2i_mp": 7.5, "edit_mp": 4.0, "area_mp": 4.0,
     "t2i_expect": "Not measured yet.", "edit_expect": "Not measured yet.", "area_expect": "Not measured yet.",
     "tested": "Not measured yet.", "vram": "Not measured yet.", "ram": "Not measured yet."}
if os.path.exists(os.path.join(HERE, "measured.json")):
    M.update(json.load(open(os.path.join(HERE, "measured.json"))))

SEED = 24112026
T2I_PROMPT = ("A photograph of a small second-hand bookshop on a rainy cobbled street at dusk. Warm yellow light spills from the big "
              "shop window onto the wet stones. Behind the glass, stacks of old hardcover books, a sleeping ginger cat on a velvet "
              "cushion and a brass reading lamp. Above the door a hand-painted wooden sign in dark green with gold letters reads "
              "\"THE LAST CHAPTER\". A woman in a mustard raincoat with a black umbrella walks past on the left, slightly blurred. "
              "Reflections of the window in the puddles, soft blue evening sky, shot on a 35 mm lens at eye level, natural colours, "
              "fine detail in the wood grain and the book spines.")
EDIT_PROMPT = ("Turn <Picture 1> into a soft watercolour painting of the same girl in the same pose, with the same pink dress, "
               "on the same green hill under the same blue sky.")
AREA_PROMPT = "Put a small golden crown on the girl's head in <Picture 1>. Keep everything else the same."
AREA_BOX = (15, 0, 70, 45)  # left, top, width, height in % (fits example.png's head)

MODEL_NOTE = "**Run on ComfyUI 0.45.3.** **No custom nodes** (core nodes only; ComfyUI 0.45+ has the MiniMax H3 Image node)."
LICENCE = ("**Licence:** MiniMax-H3-Image Community License. It does **not** cover use in the EU, the UK, South Korea or the USA. "
           "Elsewhere: written permission from MiniMax above 1 million USD yearly revenue or for a hosted service, and a commercial "
           "product must show \"MiniMax-H3-Image\". Read the licence before use. Workflow: MIT.")


def dl_table():
    rows = ["| Folder | File (click = download) | Size |", "|---|---|---|"]
    for k in ("unet", "te", "vae"):
        f = FILES[k]
        rows.append(f"| `{f[2]}/` | [{f[0]}]({f[1]}) | {f[3]} |")
    return "\n".join(rows)


def label(n, name, text):
    next(i for i in n["inputs"] if i["name"] == name)["label"] = text


def models(g, x=540):
    (unet, clip, vae), y = g.col(x, 50, 460, [
        ("UNETLoader", 90, dict(widgets=[FILES["unet"][0], "default"], title="H3 Image model, W4A8 (12.5 GB)", models=["unet"])),
        ("CLIPLoader", 110, dict(widgets=[FILES["te"][0], "minimax", "default"], title="H3 text encoder, Qwen3-VL 32B NVFP4", models=["te"])),
        ("VAELoader", 60, dict(widgets=[FILES["vae"][0]], title="H3 Image VAE", models=["vae"])),
    ])
    g.group("2 · Models (loaded once)", [x - 20, -30, 500, y + 10], C_MODEL)
    return unet, clip, vae


def sampler(g, x, unet, cond, seed, latent, vae, why=True):
    neg = g.node("ConditioningZeroOut", (x, 50), (400, 60), title="Empty negative (never read at CFG 1)", conditioning=(cond, 0))
    ks = g.node("KSampler", (x, 160), (400, 270), widgets=[SEED, "fixed", 6, 1.0, "euler", "simple", 1.0],
                title="Sampler (6 steps, CFG 1, fixed by the model)", model=(unet, 0), positive=(cond, 0), negative=(neg, 0),
                latent_image=latent, seed=(seed, 0))
    dec = g.node("VAEDecode", (x, 480), (400, 60), title="Latent → picture", samples=(ks, 0), vae=(vae, 0))
    y = 590
    if why:
        g.node("MarkdownNote", (x, y), (400, 190), title="Why 6 steps and CFG 1", widgets=[
            "**Why 6 steps and CFG 1:** MiniMax distilled this checkpoint to exactly 6 steps without guidance (their own server "
            "refuses any other value). More steps or a higher CFG do not make it better. There is no negative prompt: write what "
            "you want to avoid into the prompt."])
        y = 830
    g.group("4 · Sampling", [x - 20, -30, 440, y + 10], C_SAMPLE)
    return dec


def notes(g, how, h_how, h_dl=470):
    dl = f"""## Downloads + requirements

Click the file name to download it. Put each file in the folder shown (inside `ComfyUI/models/`).

{dl_table()}

Total 29.4 GB, the same three files for all three workflows in this folder. The text encoder is the same file as for MiniMax H3 video.

**VRAM / RAM:** {M['vram']} {M['ram']}

{MODEL_NOTE}

{LICENCE}
"""
    g.node("MarkdownNote", (-800, -30), (640, h_how), widgets=[how], title=f"How to use · v{VER}")
    g.node("MarkdownNote", (-800, h_how + 10), (640, h_dl), widgets=[dl], title="Downloads + requirements")


def build_t2i():
    g = Graph(FILES)
    mp = M["t2i_mp"]
    (p_prompt, p_size, p_seed), y = g.col(-60, 50, 520, [
        ("PrimitiveStringMultiline", 300, dict(widgets=[T2I_PROMPT], title="Prompt (describe the whole picture, English)")),
        ("ResolutionSelector", 150, dict(widgets=["3:2 (Photo)", mp, 32], title=f"Shape + megapixels ({mp:g} MP = 12 GB default)")),
        ("PrimitiveInt", 90, dict(widgets=[SEED, "fixed"], title="Seed (new number = new picture)")),
    ])
    label(p_prompt, "value", "Prompt")
    label(p_size, "aspect_ratio", "Shape")
    label(p_size, "megapixels", f"Megapixels ({mp:g} = default)")
    label(p_seed, "value", "Seed")
    g.group("1 · Your inputs (App mode shows these)", [-80, -30, 560, y + 10], C_IN)
    unet, clip, vae = models(g)
    x = 1080
    cond = g.node("MiniMaxH3ImageConditioning", (x, 50), (420, 160), widgets=["", 0, 0], title="Prompt → conditioning + empty canvas",
                  clip=(clip, 0), prompt=(p_prompt, 0), width=(p_size, 0), height=(p_size, 1))
    g.group("3 · Prompt", [x - 20, -30, 460, 270], C_PROMPT)
    dec = sampler(g, 1580, unet, cond, p_seed, (cond, 1), vae)
    x2 = 2040
    save = g.node("SaveImage", (x2, 50), (420, 460), widgets=["MiniMax-H3-Image/t2i"], title="Result (saved to output/MiniMax-H3-Image)",
                  images=(dec, 0))
    g.group("5 · Save", [x2 - 20, -30, 460, 570], C_SAVE)
    how = f"""## How to use · v{VER}

**What it does:** makes a picture from a text prompt with MiniMax H3 Image, on the 12 GB files. Core ComfyUI nodes only.

1. **Your inputs** (green group):
   - **Prompt**: describe the whole picture like a photo caption: subject, place, light, lens, colours. Long, exact prompts work best. Text in quotes is drawn as text. There is no negative prompt.
   - **Shape + megapixels**: the shape, and the size in megapixels ({mp:g} MP default, {M.get('t2i_size', '3360x2240 at 3:2')}). MiniMax built the model for 4 to 20 MP (best near 16 MP); more MP = more detail and more time.
   - **Seed**: fixed at {SEED}. Type a new number for another picture; Run with nothing changed does nothing.
2. **Models**: the three loaders must show the files from the Downloads note. Nothing to change.
3. **Prompt**: nothing to change; the prompt and size come from group 1.
4. **Sampling**: 6 steps, CFG 1, euler / simple. Nothing to change.
5. Press **Run**. The **Result** node saves to `output/MiniMax-H3-Image/`.

**What to expect:** {M['t2i_expect']}

**Tested on:** {M['tested']}
"""
    notes(g, how, 720)
    wf = g.dump("6a1f3c2e-1124-4b39-9d01-a3b3c3d3e3f1")
    wf["extra"]["linearData"] = {"inputs": [[p_prompt["id"], "value"], [p_size["id"], "aspect_ratio"], [p_size["id"], "megapixels"],
                                            [p_seed["id"], "value"]], "outputs": [save["id"]]}
    return wf


def picture_canvas(g, x, pic, p_mp, clip, vae, prompt, pic2=None):
    rs = g.node("ImageScaleToTotalPixels", (x, 50), (420, 110), widgets=["lanczos", 4.0, 32],
                title="Resize to the megapixels, keep shape (x32)", image=(pic, 0), megapixels=(p_mp, 0))
    size = g.node("GetImageSize", (x, 210), (420, 100), title="Picture size → canvas size", image=(rs, 0))
    kw = dict(clip=(clip, 0), vae=(vae, 0), prompt=(prompt, 0), width=(size, 0), height=(size, 1), images__image_1=(rs, 0))
    if pic2 is not None:
        kw["images__image_2"] = pic2
    cond = g.node("MiniMaxH3ImageConditioning", (x, 360), (420, 300), widgets=["", 0, 0],
                  title="Instruction + pictures → conditioning", **kw)
    return rs, size, cond


def build_edit():
    g = Graph(FILES)
    mp = M["edit_mp"]
    (p_img, p_use2, p_img2, p_prompt, p_mp, p_seed), y = g.col(-60, 50, 520, [
        ("LoadImage", 360, dict(widgets=["example.png", "image"], title="Picture 1 (the one to edit)")),
        ("PrimitiveBoolean", 60, dict(widgets=[False], title="Use Picture 2 (off = only Picture 1)")),
        ("LoadImage", 360, dict(widgets=["example.png", "image"], title="Picture 2 (optional reference)")),
        ("PrimitiveStringMultiline", 190, dict(widgets=[EDIT_PROMPT], title="Edit instruction (say <Picture 1>, English)")),
        ("PrimitiveFloat", 60, dict(widgets=[mp], title=f"Megapixels ({mp:g} = 12 GB default)")),
        ("PrimitiveInt", 90, dict(widgets=[SEED, "fixed"], title="Seed (new number = new picture)")),
    ])
    label(p_img, "image", "Picture 1 (to edit)")
    label(p_use2, "value", "Use Picture 2")
    label(p_img2, "image", "Picture 2 (optional)")
    label(p_prompt, "value", "Edit instruction")
    label(p_mp, "value", f"Megapixels ({mp:g} = default)")
    label(p_seed, "value", "Seed")
    g.group("1 · Your inputs (App mode shows these)", [-80, -30, 560, y + 10], C_IN)
    unet, clip, vae = models(g)
    x = 1080
    sw = g.node("ComfySwitchNode", (x, 740), (420, 100), widgets=[False], title="Picture 2 on/off (from group 1)",
                switch=(p_use2, 0), on_true=(p_img2, 0))
    rs, size, cond = picture_canvas(g, x, p_img, p_mp, clip, vae, p_prompt, pic2=(sw, 0))
    g.node("MarkdownNote", (x, 890), (420, 200), title="Why Picture 2 has a switch", widgets=[
        "**Why a switch:** with **Use Picture 2** off the switch passes nothing, so the model only sees Picture 1. "
        "The Picture 2 loader still needs a picture that exists (it is set to `example.png`), because ComfyUI checks every loader. "
        "Picture 2 goes in as it is; the node scales its own copies."])
    g.group("3 · Pictures + instruction", [x - 20, -30, 460, 1150], C_PROMPT)
    dec = sampler(g, 1580, unet, cond, p_seed, (cond, 1), vae)
    x2 = 2040
    g.node("ImageCompare", (x2, 50), (420, 420), title="Before / after (drag the slider)", image_a=(rs, 0), image_b=(dec, 0))
    save = g.node("SaveImage", (x2, 520), (420, 420), widgets=["MiniMax-H3-Image/edit"], title="Result (saved to output/MiniMax-H3-Image)",
                  images=(dec, 0))
    g.group("5 · Save", [x2 - 20, -30, 460, 1000], C_SAVE)
    how = f"""## How to use · v{VER}

**What it does:** edits a picture from a written instruction with MiniMax H3 Image, on the 12 GB files; a second picture can be a reference (a face, an object, a style). Core ComfyUI nodes only.

1. **Your inputs** (green group):
   - **Picture 1**: the picture to edit. It is set to `example.png` (ships with ComfyUI), and the default instruction is written for it, so the first Run works.
   - **Use Picture 2** + **Picture 2**: off by default. Turn it on and load a second picture to use it as a reference.
   - **Edit instruction**: what to change, naming the pictures as `<Picture 1>` and `<Picture 2>` ("Put the hat from <Picture 2> on the woman in <Picture 1>"). Short and direct works; say what must stay.
   - **Megapixels** ({mp:g}): size of the result. Picture 1 is resized to this many pixels, shape kept, sides on a 32 px grid ({M.get('edit_size', 'not measured yet')}).
   - **Seed**: fixed at {SEED}. Type a new number for another take.
2. **Models**: the three loaders must show the files from the Downloads note. Nothing to change.
3. **Pictures + instruction**: nothing to change.
4. **Sampling**: 6 steps, CFG 1, euler / simple. Nothing to change.
5. Press **Run**. **Before / after** shows both; the **Result** node saves to `output/MiniMax-H3-Image/`.

**What to expect:** {M['edit_expect']}

**Tested on:** {M['tested']}
"""
    notes(g, how, 820)
    wf = g.dump("6a1f3c2e-1124-4b39-9d01-a3b3c3d3e3f2")
    wf["extra"]["linearData"] = {"inputs": [[p_img["id"], "image"], [p_use2["id"], "value"], [p_img2["id"], "image"],
                                            [p_prompt["id"], "value"], [p_mp["id"], "value"], [p_seed["id"], "value"]],
                                 "outputs": [save["id"]]}
    return wf


def build_area():
    g = Graph(FILES)
    mp = M["area_mp"]
    L, T, W, H = AREA_BOX
    (p_img, p_prompt, p_paint, p_l, p_t, p_w, p_h, p_mp, p_seed), y = g.col(-60, 50, 520, [
        ("LoadImage", 360, dict(widgets=["example.png", "image"], title="Your picture (paint a mask here, optional)")),
        ("PrimitiveStringMultiline", 150, dict(widgets=[AREA_PROMPT], title="Edit instruction (what goes in the area)")),
        ("PrimitiveBoolean", 60, dict(widgets=[False], title="Use my painted mask (off = the box below)")),
        ("PrimitiveInt", 90, dict(widgets=[L, "fixed"], title="Box left edge (% of width)")),
        ("PrimitiveInt", 90, dict(widgets=[T, "fixed"], title="Box top edge (% of height)")),
        ("PrimitiveInt", 90, dict(widgets=[W, "fixed"], title="Box width (% of width)")),
        ("PrimitiveInt", 90, dict(widgets=[H, "fixed"], title="Box height (% of height)")),
        ("PrimitiveFloat", 60, dict(widgets=[mp], title=f"Megapixels for the edit ({mp:g} = 12 GB default)")),
        ("PrimitiveInt", 90, dict(widgets=[SEED, "fixed"], title="Seed (new number = new picture)")),
    ])
    label(p_img, "image", "Your picture")
    label(p_prompt, "value", "Edit instruction")
    label(p_paint, "value", "Use my painted mask")
    label(p_l, "value", "Box left (% of width)")
    label(p_t, "value", "Box top (% of height)")
    label(p_w, "value", "Box width (%)")
    label(p_h, "value", "Box height (%)")
    label(p_mp, "value", f"Edit megapixels ({mp:g} = default)")
    label(p_seed, "value", "Seed")
    g.group("1 · Your inputs (App mode shows these)", [-80, -30, 560, y + 10], C_IN)
    unet, clip, vae = models(g)
    x = 1080
    rs, size, cond = picture_canvas(g, x, p_img, p_mp, clip, vae, p_prompt)
    g.group("3 · Picture + instruction", [x - 20, -30, 460, 740], C_PROMPT)
    dec = sampler(g, 1580, unet, cond, p_seed, (cond, 1), vae, why=False)

    # 5 · the area: box (or painted mask) → soft mask → paste the edit back into the untouched picture
    x = 2040
    osz = g.node("GetImageSize", (x, 50), (400, 100), title="Your picture's size", image=(p_img, 0))
    mx = lambda yy, expr, t, **kw: g.node("ComfyMathExpression", (x, yy), (400, 130), widgets=[expr], title=t, **kw)
    bx = mx(200, "round(a * b / 100)", "Box left in pixels", values__a=(osz, 0), values__b=(p_l, 0))
    by = mx(370, "round(a * b / 100)", "Box top in pixels", values__a=(osz, 1), values__b=(p_t, 0))
    bw = mx(540, "max(1, round(a * min(b, 100 - c) / 100))", "Box width in pixels (stops at the edge)",
            values__a=(osz, 0), values__b=(p_w, 0), values__c=(p_l, 0))
    bh = mx(710, "max(1, round(a * min(b, 100 - c) / 100))", "Box height in pixels (stops at the edge)",
            values__a=(osz, 1), values__b=(p_h, 0), values__c=(p_t, 0))
    x2 = 2500
    m0 = g.node("SolidMask", (x2, 50), (400, 110), widgets=[0.0, 512, 512], title="Empty mask, picture size",
                width=(osz, 0), height=(osz, 1))
    m1 = g.node("SolidMask", (x2, 210), (400, 110), widgets=[1.0, 512, 512], title="White box, box size",
                width=(bw, 1), height=(bh, 1))
    box = g.node("MaskComposite", (x2, 370), (400, 130), widgets=[0, 0, "add"], title="Box mask",
                 destination=(m0, 0), source=(m1, 0), x=(bx, 1), y=(by, 1))
    sw = g.node("ComfySwitchNode", (x2, 550), (400, 100), widgets=[False], title="Painted mask or box (from group 1)",
                switch=(p_paint, 0), on_true=(p_img, 1), on_false=(box, 0))
    mi = g.node("MaskToImage", (x2, 700), (400, 60), title="Mask → picture (for the blur)", mask=(sw, 0))
    bl = g.node("ImageBlur", (x2, 810), (400, 110), widgets=[31, 10.0], title="Soft edge (31 px blur)", image=(mi, 0))
    soft = g.node("ImageToMask", (x2, 970), (400, 80), widgets=["red"], title="Soft mask", image=(bl, 0))
    x3 = 2960
    back = g.node("ResizeImageMaskNode", (x3, 50), (400, 160), widgets=["scale dimensions", 512, 512, "disabled", "lanczos"],
                  title="Edit → your picture's size", input=(dec, 0), resize_type__width=(osz, 0), resize_type__height=(osz, 1))
    comp = g.node("ImageCompositeMasked", (x3, 260), (400, 160), widgets=[0, 0, False],
                  title="Paste the edit into the area only", destination=(p_img, 0), source=(back, 0), mask=(soft, 0))
    g.node("MaskPreview", (x3, 470), (400, 300), title="Area that changes (white)", mask=(soft, 0))
    g.node("MarkdownNote", (x3, 820), (400, 230), title="Why the edit is pasted back", widgets=[
        "**Why paste back:** MiniMax H3 Image has no mask input, so it edits the whole picture. This group keeps only the area "
        "(box or painted mask, with a 31 px soft edge) and puts it into your untouched picture at its own size. "
        "Outside the area every pixel stays the original."])
    g.group("5 · The area (box or painted mask → paste back)", [x - 20, -30, 1380, 1110], C_AREA)
    x4 = 3420
    g.node("ImageCompare", (x4, 50), (420, 420), title="Before / after (drag the slider)", image_a=(p_img, 0), image_b=(comp, 0))
    save = g.node("SaveImage", (x4, 520), (420, 420), widgets=["MiniMax-H3-Image/area-edit"],
                  title="Result (saved to output/MiniMax-H3-Image)", images=(comp, 0))
    g.group("6 · Save", [x4 - 20, -30, 460, 1000], C_SAVE)
    how = f"""## How to use · v{VER}

**What it does:** changes only one area of a picture (a box, or a mask you paint) from a written instruction with MiniMax H3 Image, on the 12 GB files. Everything outside the area stays pixel for pixel the original. Core ComfyUI nodes only.

1. **Your inputs** (green group):
   - **Your picture**: set to `example.png` (ships with ComfyUI); the default box and instruction are written for it, so the first Run works.
   - **Edit instruction**: what goes in the area ("Put a small golden crown on the girl's head in <Picture 1>"). Name the picture as `<Picture 1>`.
   - **The area**: by default a **box** in percent of the picture: left edge, top edge, width, height (default {L}/{T}/{W}/{H}). To paint instead: right-click the picture → **Open in MaskEditor**, paint the area, Save, and turn **Use my painted mask** on.
   - **Megapixels for the edit** ({mp:g}): the size the model works at ({M.get('area_size', 'not measured yet')}). The result keeps your picture's own size.
   - **Seed**: fixed at {SEED}. Type a new number for another take.
2. **Models**: the three loaders must show the files from the Downloads note. Nothing to change.
3. and 4. Nothing to change (6 steps, CFG 1, euler / simple, fixed by the model).
5. **The area**: makes the mask, softens its edge (31 px) and pastes the edit back. **Area that changes** shows the mask after a Run.
6. Press **Run**. **Before / after** shows both; the **Result** node saves to `output/MiniMax-H3-Image/`.

**What to expect:** {M['area_expect']}

**Tested on:** {M['tested']}
"""
    notes(g, how, 900)
    wf = g.dump("6a1f3c2e-1124-4b39-9d01-a3b3c3d3e3f3")
    wf["extra"]["linearData"] = {"inputs": [[p_img["id"], "image"], [p_prompt["id"], "value"], [p_paint["id"], "value"],
                                            [p_l["id"], "value"], [p_t["id"], "value"], [p_w["id"], "value"], [p_h["id"], "value"],
                                            [p_mp["id"], "value"], [p_seed["id"], "value"]], "outputs": [save["id"]]}
    return wf


NAMES = {"t2i": build_t2i, "edit": build_edit, "area-edit": build_area}

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for k, fn in NAMES.items():
        p = os.path.join(out, f"The_frizzy1_h3-image-12gb-{k}_v{VER}.json")
        json.dump(fn(), open(p, "w"), indent=1, ensure_ascii=False)
        print(p)

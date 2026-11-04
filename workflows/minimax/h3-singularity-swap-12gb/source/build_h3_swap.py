"""The_frizzy1 H3 Simple Swap (12 GB): video + one photo -> the same video with that person swapped in. The run-ready (API)
graph for Genjutsu Part 3. One MiniMax H3 pass over the whole clip (no clip loop), masked to one person. Qwen3-VL writes one shot line:
Singularity V2 needs it, without it the person loses the grey figure's pose and scale (tested 2026-11-04).
Mask, grey figure and prompt follow OPENjutsu's Simple mode. Settings are OPENjutsu's on the RTX 3060: 6 steps, euler / simple,
shift 12 / 2, ref2v turbo LoRA, motion reference 512 px, mask grown 4% of the long side.

  python build_h3_swap.py OUT.json [--unet FILE] [--video NAME] [--image NAME] [--short-side N] [...]   -> API json for /prompt
  python build_h3_swap.py OUT.json --polish UI.json [--speed TEXT]   -> the shareable workflow (groups, notes, App mode)
"""
import argparse, json

SINGULARITY = "Minimax-h3_Singularity_ref2va_v2_pruned_int8.safetensors"
PLAIN_H3 = "minimax_h3_ref2va_pruned_int8_convrot.safetensors"
MODELS = {
    "lora": "minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors",
    "clip": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
    "vae": "minimax_h3_video_vae_int8_convrot.safetensors",
    "audio_vae": "minimax_h3_audio_vae_fp32.safetensors",
    "sam": "sam3.1_multiplex_fp16.safetensors",
    "describer": "qwen3vl_8b_int8_convrot.safetensors",
}
MAX_FRAMES = 362  # 15 s, the top of H3's trained range

PROMPT_HEAD = """subject_definitions:
<Subject 1> is the person from <Picture 1>. """
PROMPT_BODY = """They replace the main person in <Video 1>, in every shot where that person appears. Their face, hair, body and clothing all come from <Picture 1>.
<Subject 2> is the setting, props and lighting in <Video 1>.
<Video 1> is the source footage being edited, in which the person to replace is shown as a smooth grey figure. It supplies the exact camera framing, camera movement, performance timing, body poses and interactions. The grey figure supplies movement only; face, hair, skin and clothing come from <Picture 1>.
<Audio 1> is the synchronized original soundtrack supplied with <Video 1>, reused unchanged as the complete final soundtrack.

summary:
[video editing + reference generation + audio reuse] The target video is an edited version of <Video 1>. <Subject 1> takes the place of the main person. Identity and complete outfit come from <Picture 1>. The source performance, camera, setting, props and soundtrack retain their timing and layout.

retention_analysis:
<Subject 1> (all shots): fully_preserved - the referenced facial identity, hair, skin tone and complete outfit remain consistent while poses and mouth movements follow the main person.
<Subject 2> (setting and props): fully_preserved - the location, props and lighting retain their source appearance and position.
<Video 1> (edited source): partially_preserved - the replaced person's identity and outfit change; camera movement, shot composition, actions, interaction and timing are retained.
<Audio 1>: fully_copy - the original synchronized soundtrack is the complete final audio, without additional generated vocals or sound effects.

detailed_description:
"""
PROMPT_STYLE = ("Photorealistic live-action footage in the same setting as <Video 1>, natural lighting, realistic textures, natural skin tones and the "
                "source lens perspective. The new person appears only where the person they replace is visible; the background of the picture does not enter the scene.")
PROMPT_BODY_LINE = (" Normal realistic adult body proportions with the head in natural size to the body, at the same size in the frame as the grey figure. "
                    "Any part of the body the grey figure shows but <Picture 1> does not is completed naturally, with long dark trousers and shoes. "
                    "Everything outside the grey figure stays as it is in <Video 1>.")
SHOT_PROMPT = """These four frames are from one video, in time order. The main person is: %s. In two or three sentences describe the shot for a video prompt: first the framing (wide full-body, medium or close-up shot, and how big the person is in the frame), then where the main person is on screen, then what they do with their body and hands, including anything they hold. Call the main person <Subject 1>, with they/them. Never mention gender, age, hair, skin, clothing, glasses, hats or accessories. Output only the sentences."""
PROMPT_TAIL = """
<Subject 1> performs every action of the main person: the same gestures, steps, gaze, expressions and mouth shapes at the same moments.
Throughout, the main person is always the person in <Picture 1>, regardless of screen position or size. Their outfit replaces the original clothing completely; no face, hair, skin, costume, fabric pattern or accessory of the main person remains. """
LIP_SYNC = "The visible person lip-syncs any vocals in <Audio 1> where the source person sings or speaks; the soundtrack itself is unchanged. "
NO_LIP_SYNC = ("Nobody on screen sings, speaks or lip-syncs; the music in <Audio 1> is a background track added later. "
               "Mouths stay closed or keep the source expressions such as smiles; the soundtrack itself is unchanged. ")
PROMPT_END = "Continue the original camera movement and performance through the last frame without adding transitions or changing speed."


def build(a):
    g = {}

    def n(i, cls, title=None, **inp):
        g[str(i)] = {"class_type": cls, "inputs": inp}
        if title:
            g[str(i)]["_meta"] = {"title": title}
        return str(i)

    def math(i, title, expr, **vals):
        return n(i, "ComfyMathExpression", title, expression=expr, **{f"values.{k}": v for k, v in vals.items()})

    def join(i, x, y):
        return n(i, "StringConcatenate", string_a=x, string_b=y, delimiter="")

    # inputs
    n(1, "LoadVideo", "Your video (24 fps)", file=a.video)
    n(2, "LoadImage", "Person photo (their face, big and sharp)", image=a.image)
    n(3, "PrimitiveString", "Who to replace (the biggest one is taken)", value=a.who)
    n(4, "PrimitiveStringMultiline", "Describe the new person (one line, can stay empty)", value=a.character)
    n(5, "PrimitiveStringMultiline", "Realism prompt", value=a.style)
    n(6, "PrimitiveFloat", "Seconds (0 = whole clip, 15 s at most)", value=a.seconds)
    n(7, "PrimitiveInt", "Short side (480 / 736)", value=a.short_side)
    n(8, "PrimitiveInt", "Steps", value=a.steps)
    n(9, "PrimitiveInt", "Seed", value=a.seed)
    n(10, "PrimitiveBoolean", "Lip-sync to the sound (on for talking, off for music)", value=a.lip_sync)
    n(11, "PrimitiveInt", "Motion reference size (long side)", value=a.motion)

    # models
    n(20, "UNETLoader", "H3 model", unet_name=a.unet, weight_dtype="default")
    n(21, "LoraLoaderModelOnly", "ref2v turbo LoRA", model=["20", 0], lora_name=MODELS["lora"], strength_model=a.lora_strength)
    n(22, "ModelAttentionBackend", "Comfy Kitchen attention", model=["21", 0], attention="comfy kitchen attention")
    n(23, "MiniMaxH3SigmaShift", "Sigma shift", model=["22", 0], shift_video=12, shift_audio=2)
    n(24, "CLIPLoader", "H3 text encoder", clip_name=MODELS["clip"], type="minimax", device="default")
    n(25, "VAELoader", "Video VAE", vae_name=MODELS["vae"])
    n(26, "VAELoader", "Audio VAE", vae_name=MODELS["audio_vae"])
    n(27, "CheckpointLoaderSimple", "SAM 3.1", ckpt_name=MODELS["sam"])

    # clip: 17k + 5 frames, canvas in steps of 32
    n(30, "GetVideoComponents", "Split video", video=["1", 0])
    n(31, "GetImageSize", "Clip size", image=["30", 0])
    math(32, "Frames (H3 wants 17k + 5)", f"(min(a if b <= 0 else min(a, round(b * 24)), {MAX_FRAMES}) - 5) // 17 * 17 + 5", a=["31", 2], b=["6", 0])
    math(33, "Width", "max(32, round(a * c / min(a, b) / 32) * 32)", a=["31", 0], b=["31", 1], c=["7", 0])
    math(34, "Height", "max(32, round(b * c / min(a, b) / 32) * 32)", a=["31", 0], b=["31", 1], c=["7", 0])
    math(35, "Mask grow (4% of the long side)", "round(max(a, b) * 0.04)", a=["33", 1], b=["34", 1])
    math(36, "Length in seconds", "a / 24", a=["32", 1])
    n(37, "ImageFromBatch", "Frames used", image=["30", 0], batch_index=0, length=["32", 1])
    n(38, "ImageScale", "Frames at output size", image=["37", 0], upscale_method="area", width=["33", 1], height=["34", 1], crop="center")
    n(39, "ImageScaleToMaxDimension", "Frames for SAM (its own 1008 px)", image=["37", 0], upscale_method="area", largest_size=1008)
    n(40, "ImageScaleToMaxDimension", "Frames for the motion reference", image=["37", 0], upscale_method="area", largest_size=["11", 0])

    # mask + grey figure
    n(41, "CLIPTextEncode", "SAM: who", clip=["27", 1], text=["3", 0])
    n(42, "CLIPTextEncode", "SAM: faces", clip=["27", 1], text="face")
    n(43, "SAM3_VideoTrack", "Track the person", images=["39", 0], model=["27", 0], conditioning=["41", 0],
      detection_threshold=0.35, max_objects=0, detect_interval=1)
    n(44, "SAM3_VideoTrack", "Track faces", images=["39", 0], model=["27", 0], conditioning=["42", 0],
      detection_threshold=0.2, max_objects=0, detect_interval=1)
    n(45, "H3PeopleMask", "Biggest person (+ headroom)", track_data=["43", 0], headroom=0.1, hold_frames=2, max_people=1)
    n(46, "H3PeopleMask", "Biggest person, tight", track_data=["43", 0], headroom=0.0, hold_frames=1, max_people=1)
    n(47, "H3PeopleMask", "Faces", track_data=["44", 0], headroom=0.0, hold_frames=0, max_people=0)
    n(48, "H3GreyMannequins", "Grey figure (motion reference)", images=["40", 0], mask=["46", 0], size=["46", 1], blur=0.04,
      face_blur=0.05, faces=["47", 0], face_size=["47", 1])

    # shot line: Qwen3-VL looks at four frames
    n(12, "CLIPLoader", "Describer: Qwen3-VL 8B", clip_name=MODELS["describer"], type="stable_diffusion", device="default")
    for k, (i, f) in enumerate(((13, 0), (14, 1), (15, 2))):
        math(i, f"Frame {k + 1} of 4", f"(a - 1) * {f} // 3", a=["32", 1])
        n(i + 3, "ImageFromBatch", image=["39", 0], batch_index=[str(i), 1], length=1)
    math(19, "Frame 4 of 4", "a - 1", a=["32", 1])
    n(80, "ImageFromBatch", image=["39", 0], batch_index=["19", 1], length=1)
    n(81, "BatchImagesNode", "Four frames", **{"images.image0": ["16", 0], "images.image1": ["17", 0], "images.image2": ["18", 0], "images.image3": ["80", 0]})
    n(82, "ImageScaleToMaxDimension", "Shrink for the describer", image=["81", 0], upscale_method="area", largest_size=640)
    head, tail = SHOT_PROMPT.split("%s")
    n(83, "PrimitiveStringMultiline", value=head)
    n(84, "PrimitiveStringMultiline", value=tail)
    join(85, ["83", 0], ["3", 0])
    join(86, ["85", 0], ["84", 0])
    n(87, "TextGenerate", "Write the shot line", prompt=["86", 0], max_length=200, sampling_mode="off", thinking=False,
      use_default_template=True, mtp="auto", clip=["12", 0], image=["82", 0])

    # sound: H3 hears it for lip-sync, silence otherwise; the final video always keeps the original
    n(50, "TrimAudioDuration", "Sound cut to the clip", audio=["30", 1], start_index=0.0, duration=["36", 0])
    n(51, "PrimitiveInt", value=0)
    n(52, "PrimitiveInt", value=-100)
    n(53, "ComfySwitchNode", "Sound H3 hears", switch=["10", 0], on_true=["51", 0], on_false=["52", 0])
    n(54, "AudioAdjustVolume", "H3 sound", audio=["50", 0], volume=["53", 0])

    # prompt
    n(55, "PrimitiveStringMultiline", value=LIP_SYNC)
    n(56, "PrimitiveStringMultiline", value=NO_LIP_SYNC)
    n(57, "ComfySwitchNode", "Lip-sync line", switch=["10", 0], on_true=["55", 0], on_false=["56", 0])
    n(58, "PrimitiveStringMultiline", value=PROMPT_HEAD)
    n(59, "PrimitiveStringMultiline", value=PROMPT_BODY)
    n(60, "PrimitiveStringMultiline", value=PROMPT_TAIL)
    n(61, "PrimitiveStringMultiline", value=PROMPT_END)
    join(62, ["58", 0], ["4", 0])
    join(63, ["62", 0], " ")
    join(64, ["63", 0], ["59", 0])
    join(65, ["64", 0], ["5", 0])
    n(88, "PrimitiveStringMultiline", value=PROMPT_BODY_LINE)
    join(89, ["65", 0], " ")
    join(90, ["89", 0], ["87", 0])
    join(91, ["90", 0], ["88", 0])
    join(66, ["91", 0], ["60", 0])
    join(67, ["66", 0], ["57", 0])
    join(68, ["67", 0], ["61", 0])

    # the swap
    n(70, "MiniMaxH3FantasticVideoEditLatent", "Source + mask + sound", vae=["25", 0], images=["38", 0], mask=["45", 0], grow=["35", 1],
      keep_audio=True, megapixels=0.0, audio_vae=["26", 0], audio=["54", 0])
    n(71, "MiniMaxH3ReferenceToVideo", "Photo + grey figure + prompt", clip=["24", 0], vae=["25", 0], audio_vae=["26", 0], prompt=["68", 0],
      width=["70", 1], height=["70", 2], length=["70", 3], ref_image_size=a.ref_size, **{"ref_images.ref_image_0": ["2", 0],
      "ref_videos.ref_video_0": ["48", 0], "ref_video_audios.ref_video_audio_0": ["54", 0]})
    n(72, "RandomNoise", "Seed", noise_seed=["9", 0])
    n(73, "KSamplerSelect", "Sampler", sampler_name="euler")
    n(74, "BasicScheduler", "Schedule", model=["23", 0], scheduler="simple", steps=["8", 0], denoise=1.0)
    n(75, "BasicGuider", "Guider", model=["23", 0], conditioning=["71", 0])
    n(76, "SamplerCustomAdvanced", "Sample", noise=["72", 0], guider=["75", 0], sampler=["73", 0], sigmas=["74", 0], latent_image=["70", 0])
    n(77, "VAEDecode", "Decode", samples=["76", 0], vae=["25", 0])
    n(78, "CreateVideo", "Video + original sound", images=["77", 0], fps=24.0, audio=["50", 0])
    n(79, "SaveVideo", "Result", video=["78", 0], filename_prefix=a.prefix, format="auto", codec="auto")
    return g


# ---------------------------------------------------------------------------------------------------------------------
# The shareable (UI) workflow: `--polish UI.json` takes the graph the ComfyUI frontend saved from build(), lays the nodes out
# in named groups left to right, adds the notes and opens it in App mode.
VERSION = "1.0.0"
NAME = "The_frizzy1 · H3 Singularity Swap · 12 GB"
TESTED = "RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 · Windows 11"
PACKS = ("[comfyui-h3-oneclick-swap](https://github.com/D3voz/comfyui-h3-oneclick-swap) (person mask, grey figure) and "
         "[ComfyUI-Fantastic-MiniMaxH3-PromptBuilder](https://github.com/Adudeguyman/ComfyUI-Fantastic-MiniMaxH3-PromptBuilder) (masked edit latent)")
GROUPS = [
    ("1 · Your inputs (App mode shows these)", "#8A8", [[1, 2], [3, 4, 5], [6, 7, 8, 9, 10, 11]]),
    ("2 · Models (loaded once)", "#b58b2a", [[20, 21, 22, 23], [24, 25, 26, 27], [73, 74]]),
    ("3 · Clip: length + size", "#3f789e", [[30, 31], [32, 33, 34, 35, 36], [37, 38, 39, 40, 50]]),
    ("4 · Mask + grey figure", "#a1309b", [[41, 42], [43, 44], [45, 46, 47], [48]]),
    ("5 · Shot line (Qwen3-VL writes it)", "#3f789e", [[12, 13, 14, 15, 19], [16, 17, 18, 80], [81, 82], [83, 84, 85, 86], [87]]),
    ("6 · Sound + prompt", "#88A", [[51, 52, 53, 54], [55, 56, 57], [58, 59, 60, 61, 88], [62, 63, 64, 65], [89, 90, 91], [66, 67, 68]]),
    ("7 · Swap + save", "#b06634", [[70, 71], [72, 75], [76], [77], [78], [79]]),
]
GREEN = ("#232", "#353")
INPUTS = [["1", "file"], ["2", "image"], ["3", "value"], ["4", "value"], ["6", "value"], ["7", "value"], ["10", "value"], ["9", "value"]]

HOW_TO = f"""# {NAME} · v{VERSION}

Swaps **one real person** in your video for **the person in your photo**, keeps the room, the camera and the sound.
One H3 pass over the whole clip (up to 15 s), so there are no seams.

## How to use (App mode)
1. **Your video**: a 24 fps clip with no mirrors. Longest clip: 15 s.
2. **Person photo**: one sharp photo with a big face, plain background.
3. **Who to replace**: what SAM 3.1 looks for, e.g. *person* or *bald man*. The biggest match is taken.
4. **Describe the new person**: one line (hair, beard, glasses, outfit). **Full-body clip and your photo stops at the waist? Add the trousers and shoes** (e.g. *Dark jeans and sneakers.*). Without them Singularity made the head too big in my tests.
5. **Seconds**: 0 = whole clip. Try 3 s first.
6. **Short side**: 480 for speed, 736 for close-ups.
7. **Lip-sync**: on for talking, off for music.
8. Press **Run**. The result lands in `output/H3 simple swap/`.

## How it works
SAM 3.1 tracks the person. Qwen3-VL 8B looks at four frames and writes one line about the framing and the action, which Singularity needs to keep the pose and the size right. The person is turned into a grey figure (pose, hands, mouth, no face or clothes), H3 regenerates only the masked area from your photo and the grey figure. The prompt is OPENjutsu's Simple prompt with a realism line added, which you can edit in the graph (*Realism prompt*).

## Speed
SPEED_LINE

## Credits
Mask, grey figure and prompt idea from [OPENjutsu](https://github.com/D3voz/openjutsu) by D3voz. Workflow by **The_frizzy1**: [YouTube](https://www.youtube.com/@the_frizzy1) · [workflows](https://github.com/Thefrizzy1/The_frizzy1-Workflows).
"""

C = "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main"
LINKS = [
    ("diffusion_models", SINGULARITY, f"https://huggingface.co/WarmBloodAban/Minimax-h3_Singularity/resolve/main/{SINGULARITY}", "21.0 GB"),
    ("loras", MODELS["lora"], f"{C}/loras/{MODELS['lora']}", "2.0 GB"),
    ("text_encoders", MODELS["clip"], f"{C}/text_encoders/{MODELS['clip']}", "15.7 GB"),
    ("text_encoders", MODELS["describer"], f"https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/{MODELS['describer']}", "9.4 GB"),
    ("vae", MODELS["vae"], f"{C}/vae/{MODELS['vae']}", "2.8 GB"),
    ("vae", MODELS["audio_vae"], f"{C}/vae/{MODELS['audio_vae']}", "0.6 GB"),
    ("checkpoints", MODELS["sam"], f"https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/{MODELS['sam']}", "1.7 GB"),
]
ROWS = chr(10).join(f"| `{d}/` | [{f}]({u}) | {z} |" for d, f, u, z in LINKS)
DOWNLOADS = f"""# Downloads · put each file in the folder shown

Inside `ComfyUI/models/`. Click a file name to download it.

| Folder | File (click = download) | Size |
|---|---|---|
{ROWS}

Total: 53.2 GB. If you already run H3, you only need the first file.
Plain H3 works in the same slot: `{PLAIN_H3}`.

**Custom nodes (2):** {PACKS}.

## Requirements
- **GPU:** 12 GB VRAM tested. The 21 GB model does not fit in 12 GB: ComfyUI streams the rest from system RAM.
- **RAM:** 32 GB tested.
- **ComfyUI:** 0.43.1 tested.

_Tested on: {TESTED}._

Singularity is by [WarmBloodAban](https://huggingface.co/WarmBloodAban/Minimax-h3_Singularity), built on MiniMax H3 (MiniMax H3 Community License).
"""
TITLE_H, GAP, PAD, HEAD = 30, 36, 30, 60


def polish(src, out, speed):
    import uuid
    w = json.load(open(src, encoding="utf-8"))
    nodes = {nd["id"]: nd for nd in w["nodes"]}
    for i in (1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 79):
        nodes[i]["color"], nodes[i]["bgcolor"] = GREEN
    for nd in nodes.values():  # App mode shows the input labels: keep them the same as the titles
        for inp in nd.get("inputs", []):
            if inp.get("widget") and [str(nd["id"]), inp["name"]] in INPUTS:
                inp["label"] = nd["title"]

    def note(nid, title, text, x, y, wd, ht):
        return {"id": nid, "type": "MarkdownNote", "pos": [x, y], "size": [wd, ht], "flags": {}, "order": 0, "mode": 0, "inputs": [],
                "outputs": [], "title": title, "properties": {}, "widgets_values": [text], "color": "#432", "bgcolor": "#653"}

    nid = max(nodes) + 1
    notes = [note(nid, f"How to use · v{VERSION}", HOW_TO.replace("SPEED_LINE", speed), 0, 0, 620, 760),
             note(nid + 1, "Downloads + requirements", DOWNLOADS, 660, 0, 760, 760)]
    x, groups = 1500, []
    for title, color, cols in GROUPS:
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
    nodes[1]["widgets_values"][0], nodes[2]["widgets_values"][0] = "your_video.mp4", "your_photo.png"
    nodes[1]["widgets_values_named"]["file"], nodes[2]["widgets_values_named"]["image"] = "your_video.mp4", "your_photo.png"
    w["nodes"] = list(nodes.values()) + notes
    w["groups"] = groups
    w["last_node_id"] = max(n["id"] for n in w["nodes"])
    w["id"] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"the_frizzy1/h3-singularity-swap-12gb/{VERSION}"))
    w["revision"] = 0
    w.setdefault("extra", {}).update(linearMode=True, linearData={"inputs": INPUTS, "outputs": ["79"]}, ds={"scale": 0.45, "offset": [60, 80]},
                                     frizzy={"name": NAME, "version": VERSION, "tested_on": TESTED})
    w["models"] = [{"name": f, "url": u, "directory": d} for d, f, u, _ in LINKS]
    w.setdefault("extensions", {})["models"] = w["models"]
    json.dump(w, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out, len(w["nodes"]), "nodes,", len(groups), "groups")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--polish", metavar="UI_JSON", help="make the shareable workflow from this saved UI graph")
    ap.add_argument("--speed", default="Not measured yet.")
    ap.add_argument("--unet", default=SINGULARITY)
    ap.add_argument("--video", default="clip.mp4")
    ap.add_argument("--image", default="person.png")
    ap.add_argument("--who", default="person")
    ap.add_argument("--character", default="")
    ap.add_argument("--style", default=PROMPT_STYLE)
    ap.add_argument("--seconds", type=float, default=0.0)
    ap.add_argument("--short-side", dest="short_side", type=int, default=480)
    ap.add_argument("--steps", type=int, default=6)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lip-sync", dest="lip_sync", action="store_true")
    ap.add_argument("--motion", type=int, default=512)
    ap.add_argument("--lora-strength", dest="lora_strength", type=float, default=1.0)
    ap.add_argument("--ref-size", dest="ref_size", default="match")
    ap.add_argument("--prefix", default="H3 simple swap/swap")
    a = ap.parse_args()
    if a.polish:
        return polish(a.polish, a.out, a.speed)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(build(a), f, indent=1)
    print("wrote", a.out)


if __name__ == "__main__":
    main()

"""The_frizzy1 SCAIL-2 Character Swap (12 GB): the run-ready (API) graph, built from the official SCAIL-2 int8 template's
two segments, put into ComfyUI's own Start Loop / End Loop so it does the whole clip (the way his H3 swap v1.1 does).
Settings are the Genjutsu Part 2 benchmark winners on the RTX 3060: int8, 6 steps, distill 0.8 + DPO, short side 512.

  python build_scail_swap.py OUT.json [--video NAME] [--image NAME] [--seconds S] [...]   -> API json for /prompt
  python build_scail_swap.py OUT.json --polish UI.json   -> the shareable workflow (titles, groups, notes, version)
Every loop round = one SCAIL-2 segment of 81 frames; each round after the first starts 76 frames later and gets the
previous round's frames (the last 5 overlap), then drops those 5 and colour-matches to the previous round's last frame.
"""
import argparse, json

MODELS = {
    "unet": "wan2.1_14B_SCAIL_2_int8_convrot.safetensors",
    "dpo": "wan2.1_SCAIL_2_DPO_lora_bf16.safetensors",
    "distill": "lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors",
    "clip": "umt5_xxl_fp8_e4m3fn_scaled.safetensors",
    "vae": "Wan2_1_VAE_bf16.safetensors",
    "clip_vision": "clip_vision_h.safetensors",
    "sam": "sam3.1_multiplex_fp16.safetensors",
}
SEG, OVERLAP = 81, 5
STEP = SEG - OVERLAP


def build(a):
    g = {}

    def n(i, cls, **inp):
        g[str(i)] = {"class_type": cls, "inputs": inp}
        return str(i)

    def math(i, expr, **vals):
        return n(i, "ComfyMathExpression", expression=expr, **{f"values.{k}": v for k, v in vals.items()})

    # inputs
    n(1, "LoadVideo", file=a.video)
    n(2, "LoadImage", image=a.image)
    n(3, "PrimitiveStringMultiline", value=a.prompt)
    n(4, "PrimitiveString", value=a.who)
    n(5, "PrimitiveString", value=a.character)
    n(6, "PrimitiveFloat", value=a.seconds)
    n(7, "PrimitiveInt", value=a.short_side)
    n(8, "PrimitiveInt", value=a.steps)
    n(9, "PrimitiveBoolean", value=a.distill)
    n(10, "PrimitiveBoolean", value=a.keep_sound)
    n(11, "PrimitiveInt", value=a.seed)
    n(12, "PrimitiveString", value=a.people)                       # which people: "" = all, "0" = first, "0,1" ...
    n(13, "LoadImage", image=a.image2)                             # second character (used when two_characters is on)
    n(14, "PrimitiveBoolean", value=a.two)
    # the reference: one picture, or a batch of two (SCAIL-2 colours identities in batch order)
    n(15, "ImageScale", image=["13", 0], upscale_method="lanczos", width=["16", 0], height=["16", 1], crop="center")
    n(16, "GetImageSize", image=["2", 0])
    n(17, "BatchImagesNode", **{"images.image0": ["2", 0], "images.image1": ["15", 0]})
    n(18, "ComfySwitchNode", switch=["14", 0], on_true=["17", 0], on_false=["2", 0])

    # the clip: frames, length, padding to whole segments, size
    n(20, "GetVideoComponents", video=["1", 0])
    n(21, "GetImageSize", image=["20", 0])
    math(22, "a if b <= 0 else max(9, min(a, round(b * c)))", a=["21", 2], b=["6", 0], c=["20", 2])     # frames used
    math(23, f"max(1, ceil((a - {OVERLAP}) / {STEP}))", a=["22", 1])                                      # rounds
    math(24, f"a * {STEP} + {OVERLAP}", a=["23", 1])                                                      # padded length
    math(25, f"max(1, b * {STEP} + {OVERLAP} - a)", a=["22", 1], b=["23", 1])                             # pad frames
    n(26, "ImageFromBatch", image=["20", 0], batch_index=0, length=["22", 1])
    math(27, "a - 1", a=["22", 1])
    n(28, "ImageFromBatch", image=["26", 0], batch_index=["27", 1], length=1)
    n(29, "RepeatImageBatch", image=["28", 0], amount=["25", 1])
    n(30, "BatchImagesNode", **{"images.image0": ["26", 0], "images.image1": ["29", 0]})
    n(31, "ImageFromBatch", image=["30", 0], batch_index=0, length=["24", 1])
    math(32, "c if b >= a else (c * a // b) // 32 * 32", a=["21", 0], b=["21", 1], c=["7", 0])          # width
    math(33, "(c * b // a) // 32 * 32 if b >= a else c", a=["21", 0], b=["21", 1], c=["7", 0])          # height

    # models (loaded once, outside the loop)
    n(40, "UNETLoader", unet_name=MODELS["unet"], weight_dtype="default")
    n(41, "LoraLoaderModelOnly", model=["40", 0], lora_name=MODELS["dpo"], strength_model=1.0)
    n(42, "LoraLoaderModelOnly", model=["41", 0], lora_name=MODELS["distill"], strength_model=0.8)
    n(43, "ComfySwitchNode", switch=["9", 0], on_true=["42", 0], on_false=["41", 0])
    n(44, "ModelSamplingSD3", model=["43", 0], shift=5)
    n(45, "PrimitiveFloat", value=1.0)
    n(46, "PrimitiveFloat", value=5.0)
    n(47, "ComfySwitchNode", switch=["9", 0], on_true=["45", 0], on_false=["46", 0])                     # cfg
    n(48, "CLIPLoader", clip_name=MODELS["clip"], type="wan", device="default")
    n(49, "VAELoader", vae_name=MODELS["vae"])
    n(50, "CLIPVisionLoader", clip_name=MODELS["clip_vision"])
    n(51, "CheckpointLoaderSimple", ckpt_name=MODELS["sam"])
    n(52, "CLIPTextEncode", clip=["48", 0], text=["3", 0])
    n(53, "CLIPTextEncode", clip=["48", 0], text="")
    n(54, "CLIPVisionEncode", clip_vision=["50", 0], image=["2", 0], crop="none")
    n(55, "CLIPTextEncode", clip=["51", 1], text=["4", 0])                                               # who (in the clip)
    n(56, "CLIPTextEncode", clip=["51", 1], text=["5", 0])                                               # what (in the picture)
    n(57, "SAM3_VideoTrack", images=["18", 0], model=["51", 0], conditioning=["56", 0],
      detection_threshold=0.5, max_objects=4, detect_interval=1)
    n(58, "KSamplerSelect", sampler_name="euler")
    n(59, "BasicScheduler", model=["43", 0], scheduler="simple", steps=["8", 0], denoise=1.0)

    def scail_loop(b, frames, width, height, ref, ref_track, who_cond, people):
        """One SCAIL-2 segment per round over `frames` (already padded to whole segments); node ids b .. b+18.
        Returns the node that holds every round's frames joined (still padded)."""
        n(b, "StartLoop", **{"mode": "simple", "mode.num_iterations": ["23", 1], "cache_iterations": False})
        math(b + 1, f"a * {STEP}", a=[str(b), 0])
        n(b + 2, "ImageFromBatch", image=frames, batch_index=[str(b + 1), 1], length=SEG)
        n(b + 3, "ResizeImageMaskNode", input=[str(b + 2), 0], resize_type="scale dimensions", scale_method="area",
          **{"resize_type.width": width, "resize_type.height": height, "resize_type.crop": "center"})
        n(b + 4, "GetImageSize", image=[str(b + 3), 0])
        n(b + 5, "SAM3_VideoTrack", images=[str(b + 3), 0], model=["51", 0], conditioning=who_cond,
          detection_threshold=0.5, max_objects=4, detect_interval=1)
        n(b + 6, "SCAIL2ColoredMask", driving_track_data=[str(b + 5), 0], ref_track_data=ref_track, replacement_mode=True,
          object_indices=people, sort_by=a.order)
        common = dict(positive=["52", 0], negative=["53", 0], vae=["49", 0], width=[str(b + 4), 0], height=[str(b + 4), 1],
                      length=[str(b + 4), 2], batch_size=1, pose_strength=1.0, pose_start=0.0, pose_end=1.0, video_frame_offset=0,
                      previous_frame_count=OVERLAP, replacement_mode=True, pose_video=[str(b + 3), 0],
                      pose_video_mask=[str(b + 6), 0], reference_image=ref, reference_image_mask=[str(b + 6), 1],
                      clip_vision_output=["54", 0])
        n(b + 7, "WanSCAILToVideo", **common)                                                            # first round
        n(b + 8, "WanSCAILToVideo", previous_frames=[str(b), 4], **common)                              # later rounds
        for k, slot in ((b + 9, 0), (b + 10, 1), (b + 11, 2)):
            n(k, "ComfySwitchNode", switch=[str(b), 1], on_true=[str(b + 7), slot], on_false=[str(b + 8), slot])
        n(b + 12, "SamplerCustom", model=["44", 0], add_noise=True, noise_seed=["11", 0], cfg=["47", 0],
          positive=[str(b + 9), 0], negative=[str(b + 10), 0], sampler=["58", 0], sigmas=["59", 0], latent_image=[str(b + 11), 0])
        n(b + 13, "VAEDecode", samples=[str(b + 12), 1], vae=["49", 0])
        n(b + 14, "ImageFromBatch", image=[str(b + 13), 0], batch_index=OVERLAP, length=4096)           # drop the overlap
        n(b + 15, "ImageFromBatch", image=[str(b), 4], batch_index=-1, length=1)                        # previous last frame
        n(b + 16, "ColorTransfer", image_target=[str(b + 14), 0], image_ref=[str(b + 15), 0], method="reinhard_lab",
          source_stats="per_frame", strength=1.0)
        n(b + 17, "ComfySwitchNode", switch=[str(b), 1], on_true=[str(b + 13), 0], on_false=[str(b + 16), 0])
        n(b + 18, "EndLoop", accumulate=True, output_value=[str(b + 17), 0], next_iteration_value=[str(b + 13), 0])
        return n(b + 19, "RebatchImages", images=[str(b + 18), 0], batch_size=4096)

    # the swap: one loop over the whole clip
    body = scail_loop(60, ["31", 0], ["32", 1], ["33", 1], ["18", 0], ["57", 0], ["55", 0], ["12", 0])
    n(81, "ImageFromBatch", image=[body, 0], batch_index=0, length=["22", 1])

    # face fix (switch, needs KJNodes): track the face in the result, crop it steady, run SCAIL-2 again on the crop
    # with the character's own face as reference, put it back with soft edges
    n(100, "PrimitiveBoolean", value=a.face_fix)
    n(101, "CLIPTextEncode", clip=["51", 1], text="face")
    n(102, "SAM3_VideoTrack", images=["81", 0], model=["51", 0], conditioning=["101", 0],
      detection_threshold=0.5, max_objects=4, detect_interval=1)
    n(103, "SAM3_TrackToMask", track_data=["102", 0], object_indices="0")
    n(104, "BatchCropFromMask", original_images=["81", 0], masks=["103", 0], crop_size_mult=1.6, bbox_smooth_alpha=0.5)
    n(105, "ImageFromBatch", image=["104", 1], batch_index=["27", 1], length=1)
    n(106, "RepeatImageBatch", image=["105", 0], amount=["25", 1])
    n(107, "BatchImagesNode", **{"images.image0": ["104", 1], "images.image1": ["106", 0]})
    n(108, "ImageFromBatch", image=["107", 0], batch_index=0, length=["24", 1])
    n(110, "SAM3_Detect", model=["51", 0], image=["2", 0], conditioning=["101", 0], threshold=0.5, refine_iterations=2,
      individual_masks=False)
    n(111, "ImageCropToMask", images=["2", 0], masks=["110", 0], width=512, height=512, pad_factor=1.6, grow_mask=0,
      background="#000000")
    n(112, "SAM3_VideoTrack", images=["111", 0], model=["51", 0], conditioning=["101", 0],
      detection_threshold=0.5, max_objects=4, detect_interval=1)
    n(113, "PrimitiveInt", value=512)
    face = scail_loop(200, ["108", 0], ["113", 0], ["113", 0], ["111", 0], ["112", 0], ["101", 0], "0")
    n(121, "ImageFromBatch", image=[face, 0], batch_index=0, length=["22", 1])
    n(122, "ImageScale", image=["121", 0], upscale_method="lanczos", width=["104", 3], height=["104", 4], crop="disabled")
    n(123, "BatchUncrop", original_images=["81", 0], cropped_images=["122", 0], bboxes=["104", 2], border_blending=0.25,
      crop_rescale=1.0, border_top=False, border_bottom=False, border_left=False, border_right=False)
    n(124, "ComfySwitchNode", switch=["100", 0], on_true=["123", 0], on_false=["81", 0])

    # join, cut to the clip, sound, save
    math(82, "a / b", a=["22", 1], b=["20", 2])
    n(83, "TrimAudioDuration", audio=["20", 1], start_index=0.0, duration=["82", 0])
    n(84, "ComfySwitchNode", switch=["10", 0], on_true=["83", 0])
    n(85, "CreateVideo", images=["124", 0], fps=["20", 2], audio=["84", 0])
    n(86, "SaveVideo", video=["85", 0], filename_prefix=a.prefix, format="auto", codec="auto")
    return g


# ---------------------------------------------------------------------------------------------------------------------
# The shareable (UI) workflow: `--polish UI.json` takes the graph the ComfyUI frontend saved from build() (one character,
# no face fix) and gives every node a title, puts the nodes in named, coloured groups left to right, and adds the notes.
VERSION = "1.1.0"
NAME = "The_frizzy1 · SCAIL-2 Character Swap · 12 GB"
TESTED = "RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 (frontend 1.57.4) · Windows 11"
SIZES = {  # bytes / 1e9, read from the files the test install loads
    "unet": 16.65, "dpo": 1.23, "distill": 0.74, "clip": 6.74, "vae": 0.25, "clip_vision": 1.26, "sam": 1.75}

TITLES = {
    1: "Your video", 2: "Character picture (front view)", 3: "Describe the result", 4: "Who is in the clip",
    5: "What your character is", 6: "Seconds (0 = whole clip)", 7: "Short side (512 fits 12 GB)",
    8: "Steps (6 = best value)", 9: "Speed LoRA (on = 6 steps)", 10: "Keep the original sound", 11: "Seed",
    12: "Which person (0 = left, 1 = next, empty = everyone)",
    20: "Split video (frames · sound · fps)", 21: "Clip size + frame count", 22: "Frames used (Seconds × fps)",
    23: "Rounds (81-frame segments)", 24: "Length padded to whole segments", 25: "Padding frames needed",
    26: "Frames used", 27: "Index of the last frame", 28: "Last frame", 29: "Repeat last frame (padding)",
    30: "Frames + padding", 31: "Padded clip", 32: "Output width (÷32)", 33: "Output height (÷32)",
    82: "Clip length in seconds", 83: "Sound cut to the clip", 84: "Sound on / off",
    40: "SCAIL-2 14B int8 (diffusion model)", 41: "SCAIL-2 DPO LoRA (quality, 1.0)",
    42: "lightx2v distill LoRA (speed, 0.8)", 43: "Speed LoRA on / off", 44: "Model sampling (shift 5)",
    45: "CFG with speed LoRA (1.0)", 46: "CFG without speed LoRA (5.0)", 47: "CFG on / off",
    48: "Text encoder (umt5 xxl fp8)", 49: "Wan 2.1 VAE", 50: "CLIP Vision H", 51: "SAM 3.1 (tracks people)",
    58: "Sampler (euler)", 59: "Scheduler (simple)",
    52: "Prompt", 53: "Negative prompt (empty)", 54: "Character picture → CLIP Vision", 55: "SAM text: who in the clip",
    56: "SAM text: what in the picture", 57: "Find your character in the picture",
    60: "Loop start (one round = one segment)", 61: "First frame of this round (round × 76)",
    62: "This round's 81 frames", 63: "Resize to output size", 64: "Segment size", 65: "Track people (SAM 3.1)",
    66: "SCAIL-2 coloured mask (which person)", 67: "SCAIL-2 · first round", 68: "SCAIL-2 · next rounds (5-frame overlap)",
    69: "First round? → positive", 70: "First round? → negative", 71: "First round? → latent", 72: "Sample",
    73: "Decode", 74: "Drop the 5 overlap frames", 75: "Last frame of the previous round",
    76: "Colour match (reinhard_lab)", 77: "First round? → keep every frame", 78: "Loop end (joins every round)",
    79: "All rounds as one batch", 81: "Cut the padding off", 85: "Make the video (fps + sound)", 86: "Result",
}
# (title, group colour, node ids, columns) — columns None = laid out by what feeds what
GROUPS = [
    ("1 · Your inputs (App mode shows these)", "#8A8", [1, 2, 3, 4, 5, 12, 6, 7, 8, 9, 10, 11],
     [[1, 2], [3, 4, 5, 12], [6, 7, 8, 9, 10, 11]]),
    ("2 · Models (loaded once)", "#b58b2a", [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 58, 59], None),
    ("3 · Prompt + who to swap", "#a1309b", [52, 53, 54, 55, 56, 57], None),
    ("4 · Clip: length, padding, size", "#3f789e", [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 82, 83, 84],
     None),
    ("5 · The loop: one 81-frame SCAIL-2 segment per round", "#88A", list(range(60, 80)), None),
    ("6 · Save", "#b06634", [81, 85, 86], None),
]
GREEN = ("#232", "#353")  # the nodes you touch: inputs and the result

HOW_TO = f"""# {NAME} · v{VERSION}

Swaps **one person** in your video for **your character** (a person, an animal, a cartoon) with SCAIL-2.
Core ComfyUI nodes only, no custom nodes.

## How to use (App mode)
This workflow opens in **App mode**: you only see the inputs. Switch to the graph with the toggle at the top.

1. **Your video**: the clip with the person to replace.
2. **Character picture**: your character, front view, full body if you can.
3. **Describe the result**: one sentence, e.g. *A realistic golden retriever dances in a bright room.*
4. **Who is in the clip**: what SAM 3.1 should look for in the video, e.g. *man in red t-shirt*.
5. **What your character is**: what SAM 3.1 should look for in the picture, e.g. *dog*.
6. **Which person**: `0` = the left one, `1` = the next one to the right, empty = everyone it found.
7. **Seconds**: `0` = the whole clip. Try 3 s first.
8. Press **Run**. The video lands in `output/SCAIL2 swap/`.

## Which person
SAM 3.1 finds up to 4 people that match **Who is in the clip** and sorts them **left to right**.
`0` is the left one, `1` the next one. Empty swaps all of them for the same character.
**One character per run.**

## How it works
SCAIL-2 makes 81 frames at a time. The loop (core **Start Loop / End Loop**) runs one segment per round.
Every next round starts 76 frames later, gets the last 5 frames of the round before (overlap),
drops them again and colour-matches to the previous round (**reinhard_lab**), so a long clip stays one take.
The clip is padded to whole segments and cut back at the end. The sound is kept if you want.

## Settings (tested)
int8 model · DPO LoRA 1.0 · lightx2v distill LoRA 0.8 · 6 steps · CFG 1 · shift 5 · euler / simple · short side 512.
Speed LoRA off switches CFG to 5 (two model passes per step) and needs more steps. Only the settings above were benchmarked.

## Speed
RTX 3060 12 GB: a **9.4 s** clip at **512×896** took **24:09** (whole clip, sound kept).

## Left out on purpose
Two characters in one run and a face fix pass: not reliable enough in my tests, so they are not in v{VERSION}.
"""

DOWNLOADS = f"""# Downloads · put each file in the folder shown

Inside `ComfyUI/models/`. Click a file name to download it. ComfyUI also offers these in its **Missing models** window.

| Folder | File (click = download) | Size |
|---|---|---|
| `diffusion_models/` | [wan2.1_14B_SCAIL_2_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/diffusion_models/wan2.1_14B_SCAIL_2_int8_convrot.safetensors) | {SIZES['unet']} GB |
| `loras/` | [wan2.1_SCAIL_2_DPO_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/loras/wan2.1_SCAIL_2_DPO_lora_bf16.safetensors) | {SIZES['dpo']} GB |
| `loras/` | [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) | {SIZES['distill']} GB |
| `text_encoders/` | [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | {SIZES['clip']} GB |
| `vae/` | [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) | {SIZES['vae']} GB |
| `clip_vision/` | [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) | {SIZES['clip_vision']} GB |
| `checkpoints/` | [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) | {SIZES['sam']} GB |

Total: {round(sum(SIZES.values()), 1)} GB.

## Requirements
- **GPU:** 12 GB VRAM (tested). The 16.7 GB int8 model does not fit in 12 GB: ComfyUI streams the rest from system RAM.
- **RAM:** tested with 32 GB.
- **ComfyUI:** tested on **0.43.1**. Older versions may not have Start Loop / End Loop or the SCAIL-2 nodes: update first.
- **Custom nodes:** none.

_Tested on: {TESTED}._

## Credits & licence
SCAIL-2 by [zai-org](https://huggingface.co/zai-org/SCAIL-2) (MIT), built on Wan 2.1 14B. ComfyUI files + int8 by
[Comfy-Org](https://huggingface.co/Comfy-Org/SCAIL-2). Speed LoRA by lightx2v (repack by Kijai). SAM 3.1 by Meta
([Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)). Loop + segment settings from the official ComfyUI
SCAIL-2 template. Workflow by **The_frizzy1** (MIT): [YouTube](https://www.youtube.com/@the_frizzy1) ·
[workflows](https://github.com/Thefrizzy1/The_frizzy1-Workflows).
"""

LOOP_NOTE = """**Why a loop?** SCAIL-2 makes 81 frames per go. Every round = one segment.
Round 2+ starts 76 frames later and sees the last 5 frames of the round before.
Those 5 are dropped again and the colours are matched to the previous round."""

TITLE_H, GAP, PAD, HEAD = 30, 36, 30, 60


def polish(src, out):
    import uuid
    w = json.load(open(src, encoding="utf-8"))
    nodes = {nd["id"]: nd for nd in w["nodes"]}
    missing = set(nodes) - set(TITLES)
    assert not missing, f"no title for nodes {sorted(missing)}"
    for i, nd in nodes.items():
        nd["title"] = TITLES[i]
        nd.pop("color", None), nd.pop("bgcolor", None)
    for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 86):
        nodes[i]["color"], nodes[i]["bgcolor"] = GREEN
    for nd in nodes.values():  # App mode shows the input labels: keep them the same as the titles
        for inp in nd.get("inputs", []):
            if "label" in inp and inp.get("widget"):
                inp["label"] = nd["title"]
    ups = {i: [] for i in nodes}
    for _, origin, _, target, _, _ in w["links"]:
        ups[target].append(origin)

    def note(nid, title, text, x, y, wd, ht, color=("#432", "#653")):
        return {"id": nid, "type": "MarkdownNote", "pos": [x, y], "size": [wd, ht], "flags": {}, "order": 0, "mode": 0,
                "inputs": [], "outputs": [], "title": title, "properties": {}, "widgets_values": [text],
                "color": color[0], "bgcolor": color[1]}

    nid = max(nodes) + 1
    notes = [note(nid, f"How to use · v{VERSION}", HOW_TO, 0, 0, 620, 720),
             note(nid + 1, "Downloads + requirements", DOWNLOADS, 660, 0, 760, 720)]
    x, groups, top = 1500, [], 0
    for title, color, ids, cols in GROUPS:
        if cols is None:  # column = longest path from a node outside the group
            depth = {}

            def col_of(i):
                if i not in depth:
                    depth[i] = 1 + max((col_of(u) for u in ups[i] if u in ids), default=-1)
                return depth[i]
            cols = [[] for _ in range(max(col_of(i) for i in ids) + 1)]
            for i in sorted(ids, key=lambda i: (col_of(i), i)):
                cols[col_of(i)].append(i)
        gx, bottom = x, top
        for col in cols:
            y = top + HEAD + TITLE_H
            for i in col:
                nodes[i]["pos"] = [x + PAD, y]
                y += nodes[i]["size"][1] + TITLE_H + GAP
            bottom = max(bottom, y)
            x += max(nodes[i]["size"][0] for i in col) + GAP + 10
        if title.startswith("5 ·"):  # the loop explained, under the loop's first column
            notes.append(note(nid + 2, "Why a loop?", LOOP_NOTE, gx + PAD, bottom + TITLE_H, 520, 150, ("#222", "#000")))
            bottom += TITLE_H + 150 + GAP
        groups.append({"id": len(groups) + 1, "title": title, "color": color, "font_size": 28, "flags": {},
                       "bounding": [gx, top, x - gx + 2 * PAD - GAP, bottom - top + PAD]})
        x += 2 * PAD + 40
    w["nodes"] = list(nodes.values()) + notes
    w["groups"] = groups
    w["last_node_id"] = max(n["id"] for n in w["nodes"])
    w["id"] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"the_frizzy1/scail2-character-swap-12gb/{VERSION}"))
    w["revision"] = 0
    w["extra"]["ds"] = {"scale": 0.45, "offset": [60, 80]}
    w["extra"]["frizzy"] = {"name": NAME, "version": VERSION, "tested_on": TESTED}
    json.dump(w, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out, len(w["nodes"]), "nodes,", len(groups), "groups")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--polish", metavar="UI_JSON", help="make the shareable workflow from this saved UI graph")
    ap.add_argument("--video", default="dance clip.mp4")
    ap.add_argument("--image", default="golden retriever sheet.png")
    ap.add_argument("--prompt", default="A realistic golden retriever dances in a bright room, waving its paws.")
    ap.add_argument("--who", default="man in red t-shirt")
    ap.add_argument("--character", default="dog")
    ap.add_argument("--seconds", type=float, default=0.0)
    ap.add_argument("--short_side", type=int, default=512)
    ap.add_argument("--steps", type=int, default=6)
    ap.add_argument("--distill", type=lambda s: s.lower() != "false", default=True)
    ap.add_argument("--keep_sound", type=lambda s: s.lower() != "false", default=True)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--prefix", default="scail_swap/swap")
    ap.add_argument("--people", default="")
    ap.add_argument("--order", default="left_to_right", choices=["left_to_right", "area", "none"])
    ap.add_argument("--image2", default="cartoon frizzy.png")
    ap.add_argument("--face_fix", type=lambda s: s.lower() == "true", default=False)
    ap.add_argument("--two", type=lambda s: s.lower() == "true", default=False)
    a = ap.parse_args()
    if a.polish:
        polish(a.polish, a.out)
    else:
        json.dump(build(a), open(a.out, "w", encoding="utf-8"), indent=1)
        print("wrote", a.out)

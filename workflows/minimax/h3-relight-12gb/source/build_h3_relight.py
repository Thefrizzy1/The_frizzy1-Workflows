"""The_frizzy1 H3 Relight (12 GB): video + light sphere -> the same shot in a new light. Local ComfyUI rebuild of
Sirio Berati's relight-open-source (MIT, github.com/sirioberati/relight-open-source), which targets one rented 80 GB GPU.
Same chain, all on the RTX 3060:
  1. first frame -> Qwen3-VL 8B describes the shot (Sirio's describe.md)
  2. Qwen3-VL 8B adapts the preset's lighting master prompt to this shot (Sirio's adapt.md, five sections)
  3. MiniMax H3 Ref2VA renders the clip again with <Picture 1> = the light sphere and <Video 1> = the source clip
Settings are the ones measured for the Part 3 swap on the 3060: int8 ref2va, ref2v turbo LoRA, 6 steps, euler / simple, shift 12 / 2.

  python build_h3_relight.py OUT.json --master-file M.txt [--video NAME] [--sphere NAME] [--short-side N] [--steps N] [...]
"""
import argparse, json

PLAIN_H3 = r"MiniMax-H3\minimax_h3_ref2va_pruned_int8_convrot.safetensors"
MODELS = {
    "lora": r"MiniMax-H3\minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors",
    "clip": r"MiniMax-H3\qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
    "vae": r"MiniMax-H3\minimax_h3_video_vae_int8_convrot.safetensors",
    "audio_vae": r"MiniMax-H3\minimax_h3_audio_vae_fp32.safetensors",
    "describer": r"Qwen-Image\qwen3vl_8b_int8_convrot.safetensors",
}
MAX_FRAMES = 362
UPSCALER = r"MiniMax-H3\minimax_h3_latent_upscaler_3d_conv_v1_bf16.safetensors"
REFINE_UNET = r"MiniMax-H3\minimax_h3_fl2va_pruned_int8_convrot.safetensors"
REFINE_LORA = r"MiniMax-H3\minimax_h3_open_regenerate_2k_r128_comfyui_bf16_swiglu_fixed.safetensors"

# Sirio's describe.md, with only the frame given (the sphere is not described anyway).
DESCRIBE = """You are the first step of a video relighting pipeline. You get the first frame of a video.

Write a plain, factual description of the frame, so a video model can keep everything except the light. Cover, in this order:
1. The people: hair, clothing, pose, what the hands are doing, where they look.
2. The room or place: walls, window position, furniture, objects, every visible lamp or screen and whether it is on.
3. The current light: where it comes from, its colour and hardness.
4. The camera: framing, how close, wide-angle or not, is it handheld.

Rules: describe what you see, use screen-left and screen-right as the viewer sees them, do not invent anything you cannot see, no more than 220 words, no lists in the output, just short paragraphs."""

# Sirio's adapt.md, with H3's reference tags.
ADAPT_A = """You write the final prompt for a video model that relights an existing video.

You get:
LIGHTING MASTER PROMPT (the look to apply, reusable, written without any scene):
"""
ADAPT_B = """

FRAME DESCRIPTION (what the source video shows):
"""
ADAPT_C = """

EXTRA DIRECTION FROM THE USER (may be empty):
"""
ADAPT_D = """

The video model receives two references: <Picture 1> is a light reference sphere that shows the target light, <Video 1> is the source video. Write ONE prompt, with exactly these five sections and these headings, in this order:

【Editing Goal】
Say that <Video 1> is rebuilt with only its illumination and atmosphere changed to the lighting shown in <Picture 1>, named by the preset in the master prompt.

【Role of the Source Video】
<Video 1> is the only master for identity, room, composition, performance, timing and audio. Name the people, clothing, room features and objects from the frame description so they stay the same. If a lamp or screen is visibly on, say to relight it consistently with the new palette.

【Role of the Target Material】
<Picture 1> supplies only illumination: direction, colour, contrast, softness, falloff, pattern, shadow, haze. Do not import its sphere, floor, studio, fixtures, camera or framing.

【Edit Objects and Scope】
Turn the lighting specification from the master prompt into concrete instructions for this exact scene: where the key light sits relative to the person, which surfaces get it, what stays dark, the colour of the ambient light, what happens to the window and the lamps. Keep screen-left and screen-right as the viewer sees them. Replace the existing light and recompute shadows on the original geometry.

【Camera and Framing Lock】
Keep the camera position, distance, lens, framing and crop exactly as in <Video 1>. No zoom, push-in, pan, tilt, orbit, shake, reframing or cuts. Only light, shadow and tone may change.

Output only the prompt. Plain text. No commentary, no markdown fences, no more than 450 words."""

AUDIO_LINE = ("\n\n<Audio 1> is the original soundtrack of <Video 1>, reused unchanged as the complete final soundtrack. "
              "Every mouth movement, gesture and expression happens at the same moment as in <Video 1>.")


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

    n(1, "LoadVideo", "Your video (24 fps)", file=a.video)
    n(2, "LoadImage", "Light sphere", image=a.sphere)
    n(3, "PrimitiveStringMultiline", "Lighting master prompt (from the preset)", value=a.master)
    n(4, "PrimitiveStringMultiline", "Extra direction (can stay empty)", value=a.direction)
    n(6, "PrimitiveFloat", "Seconds (0 = whole clip, 15 s at most)", value=a.seconds)
    n(7, "PrimitiveInt", "Short side (480 / 736)", value=a.short_side)
    n(8, "PrimitiveInt", "Steps", value=a.steps)
    n(9, "PrimitiveInt", "Seed", value=a.seed)

    n(20, "UNETLoader", "H3 model", unet_name=a.unet, weight_dtype="default")
    n(21, "LoraLoaderModelOnly", "ref2v turbo LoRA", model=["20", 0], lora_name=MODELS["lora"], strength_model=a.lora_strength)
    n(22, "ModelAttentionBackend", "Comfy Kitchen attention", model=["21", 0], attention="comfy kitchen attention")
    n(23, "MiniMaxH3SigmaShift", "Sigma shift", model=["22", 0], shift_video=12, shift_audio=2)
    n(24, "CLIPLoader", "H3 text encoder", clip_name=MODELS["clip"], type="minimax", device="default")
    n(25, "VAELoader", "Video VAE", vae_name=MODELS["vae"])
    n(26, "VAELoader", "Audio VAE", vae_name=MODELS["audio_vae"])

    n(30, "GetVideoComponents", "Split video", video=["1", 0])
    n(31, "GetImageSize", "Clip size", image=["30", 0])
    math(32, "Frames (H3 wants 17k + 5)", f"(min(a if b <= 0 else min(a, round(b * 24)), {MAX_FRAMES}) - 5) // 17 * 17 + 5", a=["31", 2], b=["6", 0])
    math(33, "Width", "max(32, round(a * c / min(a, b) / 32) * 32)", a=["31", 0], b=["31", 1], c=["7", 0])
    math(34, "Height", "max(32, round(b * c / min(a, b) / 32) * 32)", a=["31", 0], b=["31", 1], c=["7", 0])
    math(36, "Length in seconds", "a / 24", a=["32", 1])
    n(37, "ImageFromBatch", "Frames used", image=["30", 0], batch_index=0, length=["32", 1])
    n(38, "ImageScale", "Frames at output size", image=["37", 0], upscale_method="area", width=["33", 1], height=["34", 1], crop="center")
    n(50, "TrimAudioDuration", "Sound cut to the clip", audio=["30", 1], start_index=0.0, duration=["36", 0])

    # prompt chain: Qwen3-VL 8B describes the first frame, then adapts the master prompt to it
    n(12, "CLIPLoader", "Describer: Qwen3-VL 8B", clip_name=MODELS["describer"], type="stable_diffusion", device="default")
    n(13, "ImageFromBatch", "First frame", image=["37", 0], batch_index=0, length=1)
    n(14, "ImageScaleToMaxDimension", "Shrink for the describer", image=["13", 0], upscale_method="area", largest_size=768)
    n(15, "PrimitiveStringMultiline", value=DESCRIBE)
    n(16, "TextGenerate", "1 Describe the shot", prompt=["15", 0], max_length=400, sampling_mode="off", thinking=False,
      use_default_template=True, mtp="auto", clip=["12", 0], image=["14", 0])
    n(17, "PreviewAny", "Shot description", source=["16", 0])
    for i, t in ((40, ADAPT_A), (41, ADAPT_B), (42, ADAPT_C), (43, ADAPT_D)):
        n(i, "PrimitiveStringMultiline", value=t)
    join(44, ["40", 0], ["3", 0])
    join(45, ["44", 0], ["41", 0])
    join(46, ["45", 0], ["16", 0])
    join(47, ["46", 0], ["42", 0])
    join(48, ["47", 0], ["4", 0])
    join(49, ["48", 0], ["43", 0])
    n(51, "TextGenerate", "2 Adapt the light to the shot", prompt=["49", 0], max_length=900, sampling_mode="off", thinking=False,
      use_default_template=True, mtp="auto", clip=["12", 0], image=["14", 0])
    n(52, "PrimitiveStringMultiline", value=AUDIO_LINE)
    join(53, ["51", 0], ["52", 0])
    n(54, "PreviewAny", "Final prompt", source=["53", 0])

    n(71, "MiniMaxH3ReferenceToVideo", "Sphere + source clip + prompt", clip=["24", 0], vae=["25", 0], audio_vae=["26", 0], prompt=["53", 0],
      width=["33", 1], height=["34", 1], length=["32", 1], ref_image_size=a.ref_size,
      **{"ref_images.ref_image_0": ["2", 0], "ref_videos.ref_video_0": ["38", 0], "ref_video_audios.ref_video_audio_0": ["50", 0]})
    n(72, "RandomNoise", "Seed", noise_seed=["9", 0])
    n(73, "KSamplerSelect", "Sampler", sampler_name="euler")
    n(74, "BasicScheduler", "Schedule", model=["23", 0], scheduler="simple", steps=["8", 0], denoise=1.0)
    n(75, "BasicGuider", "Guider", model=["23", 0], conditioning=["71", 0])
    n(76, "SamplerCustomAdvanced", "Sample", noise=["72", 0], guider=["75", 0], sampler=["73", 0], sigmas=["74", 0], latent_image=["71", 1])
    n(77, "VAEDecode", "Decode", samples=["76", 0], vae=["25", 0])
    n(78, "CreateVideo", "Video + original sound", images=["77", 0], fps=24.0, audio=["50", 0])
    n(79, "SaveVideo", "Result", video=["78", 0], filename_prefix=a.prefix, format="auto", codec="auto")

    if a.upscale:
        # Full HD: NVIDIA Open-H3-Regenerate-2K recipe at 1080p instead of 1440p. Latent upscale of the draft, then three Euler
        # steps on sigmas 0.909375, 0.857143, 0.666667, 0 with the refiner LoRA on fl2va (as the ComfyUI conversion was tested), CFG 1.
        uw, uh = a.upscale
        n(90, "LatentUpscaleModelLoader", "H3 latent upscaler", model_name=UPSCALER)
        n(91, "MiniMaxH3LatentUpscaleWithModel", "Upscale the draft latent", model=["90", 0], samples=["76", 0], width=uw, height=uh)
        n(92, "UNETLoader", "H3 fl2va (refine)", unet_name=REFINE_UNET, weight_dtype="default")
        n(93, "LoraLoaderModelOnly", "Regenerate-2K refiner LoRA", model=["92", 0], lora_name=REFINE_LORA, strength_model=1.0)
        n(94, "ModelAttentionBackend", model=["93", 0], attention="comfy kitchen attention")
        n(95, "MiniMaxH3ImageToVideo", "Refine prompt (text only)", clip=["24", 0], vae=["25", 0], prompt=["53", 0], width=uw, height=uh, length=["32", 1])
        n(96, "BasicGuider", "Refine guider", model=["94", 0], conditioning=["95", 0])
        n(97, "ManualSigmas", "Refine sigmas (lower start = keeps more of the draft)", sigmas=a.refine_sigmas)
        n(98, "SamplerCustomAdvanced", "Refine at 1080p", noise=["72", 0], guider=["96", 0], sampler=["73", 0], sigmas=["97", 0], latent_image=["91", 0])
        n(99, "VAEDecode", "Decode 1080p (falls back to tiles on low VRAM)", samples=["98", 0], vae=["25", 0])
        n(100, "CreateVideo", "1080p + original sound", images=["99", 0], fps=24.0, audio=["50", 0])
        n(101, "SaveVideo", "Result 1080p", video=["100", 0], filename_prefix=a.prefix + "_1080p", format="auto", codec="auto")
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--master-file", dest="master_file", required=True)
    ap.add_argument("--direction", default="")
    ap.add_argument("--unet", default=PLAIN_H3)
    ap.add_argument("--video", default="clip.mp4")
    ap.add_argument("--sphere", default="sphere.png")
    ap.add_argument("--seconds", type=float, default=0.0)
    ap.add_argument("--short-side", dest="short_side", type=int, default=480)
    ap.add_argument("--steps", type=int, default=6)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lora-strength", dest="lora_strength", type=float, default=1.0)
    ap.add_argument("--ref-size", dest="ref_size", default="match")
    ap.add_argument("--prefix", default="H3 relight/relight")
    ap.add_argument("--upscale", type=int, nargs=2, metavar=("W", "H"), help="add the 1080p stage, e.g. --upscale 1920 1088")
    ap.add_argument("--refine-sigmas", dest="refine_sigmas", default="0.909375, 0.857143, 0.666667, 0.0",
                    help="NVIDIA's default starts at 0.909 and redraws faces; try '0.55, 0.4, 0.2, 0.0' to keep identity")
    a = ap.parse_args()
    a.master = open(a.master_file, encoding="utf-8").read()
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(build(a), f, indent=1, ensure_ascii=False)
    print("wrote", a.out)


if __name__ == "__main__":
    main()

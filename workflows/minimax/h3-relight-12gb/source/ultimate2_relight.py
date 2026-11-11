"""Spec for "The_frizzy1 Relight · 12 GB" v1.0.0 (2026-11-11): video + light sphere + the preset's light text -> the same
shot in a new light (MiniMax H3 Ref2VA). Local rebuild of Sirio Berati's relight-open-source (MIT presets). Same system
as the other Ultimates: ultimate2.py plan -> input/_sg_<NAME>.json -> buildUltimate("<NAME>") in the ComfyUI frontend.

The run graph is OSH-test/app/build_h3_relight.py (the one every RTX 3060 relight test ran), with:
  - bare model file names (the repo standard; pick the file once if yours sit in a subfolder)
  - the full-HD size from the clip (short side 1088) instead of the fixed --upscale 1920 1088
  - one Full HD dropdown: Off / Gentle H3 refine / RealESRGAN x2, picked with core lazy switches (only that path runs)
  - one Save node (the chosen path); the draft is not saved separately when a full-HD path is on

    python ultimate2_relight.py
"""
import json
import os
import sys
from argparse import Namespace

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\friso\Studio\OSH-test\app")
import ultimate2 as U  # noqa: E402
from ultimate2 import L, grp  # noqa: E402
import build_h3_relight as B  # noqa: E402

NAME = "The_frizzy1_h3-relight-12gb_v1.0.0"
U.INPUT = r"C:\Users\friso\Documents\ComfyUI-Portable\ComfyUI\input"
PRESETS = r"C:\Users\friso\Studio\Relight-local\sirio_presets\presets.json"

M_OFF = "Off (draft size)"
M_GENTLE = "Gentle H3 refine (sigma 0.55)"
M_ESRGAN = "RealESRGAN x2 (no redraw)"
FULL_HD_SHORT = 1088   # 1920x1088 for a 16:9 clip (H3 sizes are multiples of 32)
ESRGAN = "RealESRGAN_x2plus.pth"
GENTLE_SIGMAS = "0.55, 0.4, 0.2, 0.0"


def base(short_side=480, seconds=0.0, steps=6, seed=42, master=None, mode=M_OFF):
    a = Namespace(video="desk_talk.mp4", sphere="cinematic-04-blue-amber-bed.png", master=master or preset_master(),
                  direction="", seconds=seconds, short_side=short_side, steps=steps, seed=seed, unet=B.PLAIN_H3,
                  lora_strength=1.0, ref_size="match", prefix="H3 relight/relight", upscale=(1920, 1088),
                  refine_sigmas=GENTLE_SIGMAS)
    g = B.build(a)
    return a, g


def preset_master(pid="cinematic-04-blue-amber-bed"):
    return next(p["master"] for p in json.load(open(PRESETS, encoding="utf-8")) if p["id"] == pid)


def relight_api(**kw):
    mode = kw.pop("mode", M_OFF)
    long_kw = kw.pop("long", False)
    a, g = base(**kw)
    titles = {k: v["_meta"]["title"] for k, v in g.items() if "_meta" in v}
    for v in g.values():
        v.pop("_meta", None)
        for k, x in v["inputs"].items():   # bare file names: the repo standard
            if isinstance(x, str) and x.endswith(".safetensors"):
                v["inputs"][k] = x.split("\\")[-1]
    # full-HD size from the clip: short side 1088 (the builder's --upscale 1920 1088 for a 16:9 clip)
    g["fw"] = {"class_type": "ComfyMathExpression", "inputs": {"expression": f"max(32, round(a * {FULL_HD_SHORT} / min(a, b) / 32) * 32)",
                                                                "values.a": L("31", 0), "values.b": L("31", 1)}}
    g["fh"] = {"class_type": "ComfyMathExpression", "inputs": {"expression": f"max(32, round(b * {FULL_HD_SHORT} / min(a, b) / 32) * 32)",
                                                                "values.a": L("31", 0), "values.b": L("31", 1)}}
    titles.update(fw="Full HD width (short side 1088)", fh="Full HD height (short side 1088)")
    for k in ("91", "95"):
        g[k]["inputs"].update(width=L("fw", 1), height=L("fh", 1))
    # gentle refine sigmas as a setting
    g["sigmas"] = {"class_type": "PrimitiveString", "inputs": {"value": GENTLE_SIGMAS}}
    g["97"]["inputs"]["sigmas"] = L("sigmas")
    titles["sigmas"] = "Gentle refine sigmas (lower start = keeps more of the draft)"
    # RealESRGAN x2 path (build_esrgan_upscale.py, on the decoded draft instead of the saved file)
    g["esr_load"] = {"class_type": "UpscaleModelLoader", "inputs": {"model_name": ESRGAN}}
    g["esr_up"] = {"class_type": "ImageUpscaleWithModel", "inputs": {"upscale_model": L("esr_load"), "image": L("77")}}
    g["esr_size"] = {"class_type": "ImageScale", "inputs": {"image": L("esr_up"), "upscale_method": "lanczos",
                                                            "width": L("fw", 1), "height": L("fh", 1), "crop": "center"}}
    g["esr_vid"] = {"class_type": "CreateVideo", "inputs": {"images": L("esr_size"), "fps": 24.0, "audio": L("50")}}
    titles.update(esr_load="RealESRGAN x2 model", esr_up="RealESRGAN x2 (every frame)", esr_size="Lanczos to full HD",
                  esr_vid="Full HD + original sound")
    # the Full HD dropdown -> lazy switches: only the chosen path runs
    g["mode"] = {"class_type": "CustomCombo", "inputs": {"choice": mode, "index": [M_OFF, M_GENTLE, M_ESRGAN].index(mode)}}
    g["is_gentle"] = {"class_type": "StringCompare", "inputs": {"string_a": L("mode"), "string_b": M_GENTLE, "mode": "Equal", "case_sensitive": True}}
    g["is_esrgan"] = {"class_type": "StringCompare", "inputs": {"string_a": L("mode"), "string_b": M_ESRGAN, "mode": "Equal", "case_sensitive": True}}
    g["sw_esr"] = {"class_type": "ComfySwitchNode", "inputs": {"switch": L("is_esrgan"), "on_true": L("esr_vid"), "on_false": L("78")}}
    g["sw_out"] = {"class_type": "ComfySwitchNode", "inputs": {"switch": L("is_gentle"), "on_true": L("100"), "on_false": L("sw_esr")}}
    titles.update(mode="Full HD", is_gentle="Gentle refine chosen?", is_esrgan="RealESRGAN chosen?",
                  sw_esr="RealESRGAN or the draft", sw_out="Video that gets saved")
    # ---- Long clip: core Start Loop / End Loop, one 124-frame H3 pass per round (the length every test used), the same
    # sphere, prompt (describe + adapt once, from the clip's first frame) and seed in every pass. From pass 2 on,
    # MiniMaxH3AddGuide anchors the previous pass's last 22 frames at frame 0 (as in the H3 Character Swap loop) and those
    # 22 frames are dropped. Each pass decodes only its own 124-frame window (Video Slice), so a 60 s 1080p clip never
    # sits in RAM as float frames. Each pass becomes a video with its own slice of the original sound; Concatenate Video
    # joins them in order. Seconds sets the length (the clip's frame count is not known without decoding all of it).
    long = long_kw
    g["is_long"] = {"class_type": "PrimitiveBoolean", "inputs": {"value": long}}
    titles["is_long"] = "Long clip (5.2 s passes, up to 60 s)"
    # first frame without decoding the clip (long mode); the short mode keeps the builder's links
    g["ff_slice"] = {"class_type": "Video Slice", "inputs": {"video": L("1"), "start_time": 0.0, "duration": 0.05, "strict_duration": False}}
    g["ff_comp"] = {"class_type": "GetVideoComponents", "inputs": {"video": L("ff_slice")}}
    g["src_img"] = {"class_type": "ComfySwitchNode", "inputs": {"switch": L("is_long"), "on_true": L("ff_comp"), "on_false": L("30")}}
    g["31"]["inputs"]["image"] = L("src_img")
    g["src_first"] = {"class_type": "ComfySwitchNode", "inputs": {"switch": L("is_long"), "on_true": L("ff_comp"), "on_false": L("37")}}
    g["13"]["inputs"]["image"] = L("src_first")
    titles.update(ff_slice="First frame only (long clip)", ff_comp="Decode the first frame", src_img="Size from: first frame (long) / whole clip",
                  src_first="Describer frame: first frame (long) / clip")
    C, O, S = 124, 22, 102

    def m(k, e, t, **v):
        g[k] = {"class_type": "ComfyMathExpression", "inputs": {"expression": e, **{f"values.{a}": x for a, x in v.items()}}}
        titles[k] = t

    def n(k, ct, t, **inp):
        g[k] = {"class_type": ct, "inputs": inp}
        titles[k] = t

    m("lc_n", "124 if a <= 0 else max(5, min(1440, round(a * 24)))", "Frames to relight (Seconds x 24, 60 s max)", a=L("6"))
    m("lc_passes", f"max(1, ceil((a - {O} - 3) / {S}))", f"Passes ({C} frames, {O} overlap)", a=L("lc_n", 1))
    n("lc_loop", "StartLoop", "Start Loop (one 5.2 s pass per round)", **{"mode": "simple", "mode.num_iterations": L("lc_passes", 1)},
      cache_iterations=False)
    m("lc_start", f"a * {S}", "Pass start (frame)", a=L("lc_loop", 0))
    m("lc_start_s", "a / 24", "Pass start (s)", a=L("lc_start", 1))
    m("lc_wlen", f"min({C}, a - b)", "Window frames", a=L("lc_n", 1), b=L("lc_start", 1))
    m("lc_wlen_s", "a / 24", "Window (s)", a=L("lc_wlen", 1))
    n("lc_slice", "Video Slice", "This pass's window of the clip", video=L("1"), start_time=L("lc_start_s"), duration=L("lc_wlen_s"),
      strict_duration=False)
    n("lc_comp", "GetVideoComponents", "Decode the window", video=L("lc_slice"))
    n("lc_size", "GetImageSize", "Window frame count", image=L("lc_comp"))
    n("lc_scaled", "ImageScale", "Window at output size", image=L("lc_comp"), upscale_method="area", width=L("33", 1), height=L("34", 1), crop="center")
    m("lc_lastidx", "a - 1", "Last frame index", a=L("lc_size", 2))
    n("lc_last", "ImageFromBatch", "Last frame", image=L("lc_scaled"), batch_index=L("lc_lastidx", 1), length=1)
    m("lc_padn", f"max(1, {C} - a)", "Frames to pad (last pass)", a=L("lc_size", 2))
    n("lc_hold", "RepeatImageBatch", "Hold the last frame", image=L("lc_last"), amount=L("lc_padn", 1))
    n("lc_padded", "BatchImagesNode", "Window + held frames", **{"images.image0": L("lc_scaled"), "images.image1": L("lc_hold")})
    n("lc_win", "ImageFromBatch", f"{C} frames for H3", image=L("lc_padded"), batch_index=0, length=C)
    n("lc_r2v", "MiniMaxH3ReferenceToVideo", "Sphere + window + prompt", clip=L("24"), vae=L("25"), audio_vae=L("26"), prompt=L("53"),
      width=L("33", 1), height=L("34", 1), length=C, ref_image_size="match",
      **{"ref_images.ref_image_0": L("2"), "ref_videos.ref_video_0": L("lc_win"), "ref_video_audios.ref_video_audio_0": L("lc_comp", 1)})
    n("lc_guided", "MiniMaxH3AddGuide", f"Continue from the last {O} frames", positive=L("lc_r2v"), vae=L("25"), latent=L("lc_r2v", 1),
      image=L("lc_loop", 4), frame_idx=0)
    n("lc_pos", "ComfySwitchNode", "First pass? no guide", switch=L("lc_loop", 1), on_true=L("lc_r2v"), on_false=L("lc_guided"))
    n("lc_guider", "BasicGuider", "Guider", model=L("23"), conditioning=L("lc_pos"))
    n("lc_sample", "SamplerCustomAdvanced", "Sample (same seed every pass)", noise=L("72"), guider=L("lc_guider"), sampler=L("73"),
      sigmas=L("74"), latent_image=L("lc_r2v", 1))
    n("lc_dec", "VAEDecode", "Decode", samples=L("lc_sample"), vae=L("25"))
    m("lc_off", f"0 if a else {O}", f"Skip the {O} guided frames (not in pass 1)", a=L("lc_loop", 1))
    m("lc_cnt", "b - a", "New frames in this pass", a=L("lc_off", 1), b=L("lc_size", 2))
    n("lc_new", "ImageFromBatch", "New frames", image=L("lc_dec"), batch_index=L("lc_off", 1), length=L("lc_cnt", 1))
    m("lc_off_s", "a / 24", "Sound start (s)", a=L("lc_off", 1))
    m("lc_cnt_s", "a / 24", "Sound length (s)", a=L("lc_cnt", 1))
    n("lc_aud", "TrimAudioDuration", "This pass's original sound", audio=L("lc_comp", 1), start_index=L("lc_off_s"), duration=L("lc_cnt_s"))
    # codec auto = H.264 right away, so the finished passes wait in RAM as small encoded clips, not as float frames
    n("lc_pvid", "CreateVideo", "Pass video + its sound (encoded now)", images=L("lc_new"), fps=24.0, audio=L("lc_aud"), codec="auto")
    n("lc_tail", "ImageFromBatch", f"Last {O} frames -> next pass", image=L("lc_dec"), batch_index=S, length=O)
    n("lc_end", "EndLoop", "End Loop (collects every pass)", output_value=L("lc_pvid"), next_iteration_value=L("lc_tail"), accumulate=True)
    n("lc_cat", "ConcatenateVideo", "Join the passes in order", **{"videos.video0": L("lc_end")}, codec="auto")
    g["sw_long"] = {"class_type": "ComfySwitchNode", "inputs": {"switch": L("is_long"), "on_true": L("lc_cat"), "on_false": L("sw_out")}}
    titles["sw_long"] = "Long clip or one pass"
    # one Save node for the chosen path
    del g["79"], g["101"]
    g["save"] = {"class_type": "SaveVideo", "inputs": {"video": L("sw_long"), "filename_prefix": "H3 relight/relight", "format": "auto", "codec": "auto"}}
    titles.update({"save": "Result", "1": "Your video (24 fps)", "2": "Light sphere (from the preset)",
                   "3": "Light: the preset's master prompt", "4": "Extra direction (can stay empty)",
                   "6": "Seconds (0 = whole clip up to 15 s; long clip: its length, up to 60)",
                   "15": "Describe instruction (Sirio's describe.md)", "40": "Adapt instruction 1/4 (Sirio's adapt.md)",
                   "41": "Adapt instruction 2/4", "42": "Adapt instruction 3/4", "43": "Adapt instruction 4/4",
                   "44": "+ master prompt", "45": "+ 2/4", "46": "+ shot description", "47": "+ 3/4", "48": "+ extra direction",
                   "49": "+ 4/4", "52": "Sound line", "53": "Final prompt = adapted + sound line", "94": "Comfy Kitchen attention (refine)"})
    return g, titles


def how_text():
    return "\n".join([
        "## How to use - tested on RTX 3060 12 GB", "",
        "**What it does:** your video + a light sphere + the light text -> the same shot in the new light. "
        "Same people, room, camera, timing and sound. A local rebuild of Sirio Berati's open-source relight "
        "(his 67 presets are MIT).", "",
        "1. **Your video**: 24 fps, up to 15 s.",
        "2. **Light sphere**: a preset's sphere image (`spheres/` in Sirio's presets) or your own.",
        "3. **Light text**: paste that preset's master prompt (the `master` text in `presets.json`), or write your own in the same five headings.",
        "4. On the **H3 Relight** node: **Short side** 480 (fast) or 736, **Seconds** (0 = the whole clip, up to 15 s in one pass), **Full HD** and **Run**.",
        "5. **Long clip** on: the clip is relit in 5.2 s passes (core Start Loop / End Loop), up to 60 s. Set **Seconds** to the clip's length "
        "(or less; 0 = one pass). Every pass gets the same sphere, prompt and seed, continues from the last 22 frames of the pass before, "
        "and keeps its slice of the original sound. Full HD does not apply to long clips.", "",
        "| Full HD | What happens |", "|---|---|",
        f"| {M_OFF} | the H3 draft at your short side |",
        f"| {M_GENTLE} | H3 latent upscaler to 1088p + 3 Regenerate-2K steps from sigma 0.55 (keeps the face of the draft) |",
        f"| {M_ESRGAN} | RealESRGAN x2 on every draft frame, Lanczos to 1088p, no redraw |", "",
        "| Run (5.2 s desk clip, 6 steps) | RTX 3060 | Peak VRAM | Peak RAM |", "|---|---|---|---|",
        "| 480, off | 6:40 - 6:49 | 11.8 GB | 21.4 GB |",
        "| 736, off | 21:03 - 24:02 | 11.9 GB | 22.6 GB |",
        "| 736 + gentle refine to 1920x1088 | 31:48 | 11.9 GB | 22.5 GB |",
        "| RealESRGAN x2 of a finished 736 clip (its own graph) | 3:54 - 5:49 | 7.6 GB | 14.4 GB |", "",
        "Inside: Qwen3-VL 8B describes the first frame, then rewrites the light text for this shot (Sirio's describe + adapt steps). "
        "H3 renders the clip with <Picture 1> = the sphere and <Video 1> = your clip. Settings: ref2v turbo LoRA, euler / simple, shift 12 / 2.", "",
        "Double-click the node to see every step. " + U.LEGEND,
    ])


def downloads_text():
    hf = "https://huggingface.co"
    rows = [
        ("Comfy-Org/MiniMax-H3", [
            ("all", "diffusion_models", "minimax_h3_ref2va_pruned_int8_convrot.safetensors", "diffusion_models/", 21.0),
            ("all", "loras", "minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors", "loras/", 2.0),
            ("all", "text_encoders", "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "text_encoders/", 15.7),
            ("all", "vae", "minimax_h3_video_vae_int8_convrot.safetensors", "vae/", 2.8),
            ("all", "vae", "minimax_h3_audio_vae_fp32.safetensors", "vae/", 0.6),
            ("Gentle refine", "diffusion_models", "minimax_h3_fl2va_pruned_int8_convrot.safetensors", "diffusion_models/", 21.0)]),
        ("Comfy-Org/Qwen3-VL", [("all (describer)", "text_encoders", "qwen3vl_8b_int8_convrot.safetensors", "text_encoders/", 9.4)]),
        ("Efficient-Large-Model/Open-H3-Regenerate-2K", [
            ("Gentle refine", "latent_upscale_models", "minimax_h3_latent_upscaler_3d_conv_v1_bf16.safetensors", "latent_upsampler/", 0.7)]),
        ("DrakenZA/Open-H3-Regenerate-2K-ComfyUI", [
            ("Gentle refine", "loras", "minimax_h3_open_regenerate_2k_r128_comfyui_bf16_swiglu_fixed.safetensors", "", 2.0)]),
    ]
    out = ["## Downloads - put each file in the ComfyUI folder shown", "",
           "Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).", ""]
    for repo, files in rows:
        out += [f"**[{repo}]({hf}/{repo})**", "", "| For | Folder | File (click = download) | Size |", "|---|---|---|---|"]
        out += [f"| {lab} | `{fol}/` | [{f}]({hf}/{repo}/resolve/main/{sub}{f}) | {gb:.1f} GB |" for lab, fol, f, sub, gb in files]
        out.append("")
    out += ["**[xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)**", "", "| For | Folder | File (click = download) | Size |",
            "|---|---|---|---|",
            f"| RealESRGAN x2 | `upscale_models/` | [{ESRGAN}](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/{ESRGAN}) | 0.1 GB |", "",
            "_Tested on: RTX 3060 12 GB · 32 GB RAM · ComfyUI 0.44.0._", "",
            "Full HD off needs only the first five MiniMax files + Qwen3-VL 8B (51.5 GB). No custom nodes: core ComfyUI **0.44 or newer**. "
            "Light presets + spheres: [sirioberati/relight-open-source](https://github.com/sirioberati/relight-open-source) (MIT). "
            "License: MiniMax H3 Community License (H3, the turbo LoRA, the Regenerate-2K upscaler) - read it before commercial use."]
    return "\n".join(out)


def relight_spec():
    api, titles = relight_api()
    settings = ["4", "6", "7", "8", "9", "mode", "sigmas", "is_long"]
    loaders = ["20", "21", "22", "23", "24", "25", "26", "12", "90", "92", "93", "94", "esr_load"]
    clip = ["ff_slice", "ff_comp", "src_img", "30", "31", "32", "33", "34", "36", "fw", "fh", "37", "src_first", "38", "50"]
    prompt = ["13", "14", "15", "16", "17", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "52", "53", "54"]
    draft = ["71", "72", "73", "74", "75", "76", "77", "78"]
    gentle = ["91", "95", "96", "97", "98", "99", "100"]
    esr = ["esr_up", "esr_size", "esr_vid"]
    logic = ["is_gentle", "is_esrgan", "sw_esr", "sw_out", "sw_long"]
    longk = [k for k in api if k.startswith("lc_")]
    nested = [
        {"key": "p_prompt", "name": "Qwen3-VL writes the prompt", "color": ["#653", "#864"], "keys": prompt,
         "layout": {"rows": [[0, 1, 2]], "groups": [
             grp("1 Describe the first frame (Sirio's describe.md)", "input", ["13", "14", "15", "16", "17"]),
             grp("2 Adapt the light text to this shot (Sirio's adapt.md)", "prompt", ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51"]),
             grp("Final prompt + sound line", "prompt", ["52", "53", "54"])]}},
        {"key": "p_gentle", "name": "Full HD: gentle H3 refine", "color": ["#653", "#864"], "keys": gentle,
         "layout": {"rows": [[0, 1, 2]], "groups": [
             grp("H3 latent upscaler to 1088p", "sample", ["91"]),
             grp("Regenerate-2K refine: 3 steps from sigma 0.55, CFG 1", "sample", ["95", "96", "97", "98"]),
             grp("Decode + original sound", "decode", ["99", "100"])]}},
        {"key": "p_esr", "name": "Full HD: RealESRGAN x2", "color": ["#653", "#864"], "keys": esr,
         "layout": {"rows": [[0, 1]], "groups": [
             grp("RealESRGAN x2 + Lanczos to 1088p (no redraw)", "extra", ["esr_up", "esr_size"]),
             grp("Original sound", "decode", ["esr_vid"])]}},
        {"key": "p_long", "name": "Long clip: 5.2 s passes", "color": ["#653", "#864"], "keys": longk,
         "layout": {"maxh": 1300, "rows": [[0, 1, 2, 3]], "groups": [
             grp("How many passes (Seconds x 24 frames, 60 s max)", "logic", ["lc_n", "lc_passes", "lc_loop", "lc_start", "lc_start_s", "lc_wlen", "lc_wlen_s"]),
             grp("This pass's 124-frame window (only it is decoded)", "input",
                 ["lc_slice", "lc_comp", "lc_size", "lc_scaled", "lc_lastidx", "lc_last", "lc_padn", "lc_hold", "lc_padded", "lc_win"]),
             grp("Relight the window, continuing the last 22 frames", "sample", ["lc_r2v", "lc_guided", "lc_pos", "lc_guider", "lc_sample", "lc_dec"]),
             grp("New frames + their sound -> join in order", "decode",
                 ["lc_off", "lc_cnt", "lc_new", "lc_off_s", "lc_cnt_s", "lc_aud", "lc_pvid", "lc_tail", "lc_end", "lc_cat"])]}},
    ]
    P = lambda k, w, n, lab: {"key": k, "widget": w, "name": n, "label": lab}  # noqa: E731
    promote = [P("4", "value", "direction", "Extra direction (can stay empty)"),
               P("6", "value", "seconds", "Seconds (0 = whole clip up to 15 s; long clip: its length, up to 60)"),
               P("7", "value", "short_side", "Short side (480 / 736)"),
               P("8", "value", "steps", "Steps"),
               P("9", "value", "seed", "Seed"),
               P("mode", "choice", "full_hd", "Full HD (1088p)"),
               P("sigmas", "value", "refine_sigmas", "Gentle refine sigmas"),
               P("is_long", "value", "long_clip", "Long clip (5.2 s passes, up to 60 s)"),
               P("20", "unet_name", "model_file", "H3 model (ref2va)"),
               P("21", "lora_name", "turbo_lora", "Turbo LoRA"),
               P("24", "clip_name", "text_encoder", "H3 text encoder"),
               P("25", "vae_name", "video_vae", "Video VAE"),
               P("26", "vae_name", "audio_vae", "Audio VAE"),
               P("12", "clip_name", "describer", "Describer (Qwen3-VL 8B)"),
               P("90", "model_name", "latent_upscaler", "Latent upscaler (gentle)"),
               P("92", "unet_name", "refine_model", "Refine model fl2va (gentle)"),
               P("93", "lora_name", "refine_lora", "Regenerate-2K LoRA (gentle)"),
               P("esr_load", "model_name", "esrgan", "RealESRGAN model")]
    main_keys = settings + loaders + clip + draft + logic + ["p_prompt", "p_gentle", "p_esr", "p_long"]
    spec = {
        "titles": titles,
        "combos": {"mode": [M_OFF, M_GENTLE, M_ESRGAN]},
        "nested": nested,
        "main": {"name": "H3 Relight", "keys": main_keys, "promote": promote, "output_labels": {"save": "Result"},
                 "layout": {"rows": [[0, 1, 2], [3, 4, 5, 6, 7]], "groups": [
                     grp("Settings (shown on the node outside)", "settings", settings),
                     grp("Load models (only the chosen path's models load)", "models", loaders),
                     grp("Your clip -> length + size (H3 wants 17k + 5 frames)", "input", clip),
                     grp("Prompt (double-click)", "prompt", ["p_prompt"]),
                     grp("Relight: sphere + clip + prompt", "sample", draft),
                     grp("Full HD (double-click)", "extra", ["p_gentle", "p_esr"]),
                     grp("Long clip (double-click)", "sample", ["p_long"]),
                     grp("Switches: only the chosen path runs", "logic", logic)]}},
        "top": {"inputs": ["1", "2", "3"], "outputs": ["save"]},
        "notes": [{"title": "How to use", "text": how_text()}, {"title": "Downloads", "text": downloads_text()}],
    }
    return NAME, api, spec


if __name__ == "__main__":
    name, api, spec = relight_spec()
    print(U.plan(name, api, spec), "->", name)

# Compatibility Matrices

Quick cross-reference of what runs where. All rows below are derived from the actual workflow files unless
marked *Not verified*. Last checked 2026-10-15 (24 workflows).

---

## Workflow × task

| Workflow | T2V | I2V | V2V/Animate | T2I | Img edit | Audio | FFLF | Other |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| MiniMax H3 Ultimate · 12 GB | ✅ | ✅ | ✅ (pose, refs) | — | — | ✅ | ✅ | last frame · multiframe · extend |
| Viggle-Animate (H3) | — | — | ✅ | — | — | ✅ (keeps the clip's) | — | swap a person for one still |
| LTX 2.5 Ultimate · 12 GB | ✅ | ✅ | ✅ (pose IC-LoRA) | — | — | ✅ | ✅ | |
| LTX-2.3 Ultimate | ✅ | ✅ | — | — | — | ✅ | ✅ | ID LoRA |
| LTX-2 GGUF | ✅ | ✅ | — | — | — | ✅ | — | |
| Wan Animate Ultimate | — | — | ✅ | — | — | — | — | face video (GGUF mode) |
| Wan 2.2 Animate | — | — | ✅ | — | — | — | — | looping |
| Wan 2.2 GGUF Low-VRAM | ✅ | ✅ | — | — | — | — | — | |
| Wan 2.2 AIO Rapid | ✅ | ✅ | — | — | — | — | — | single file |
| Wan 2.1 GGUF Low-VRAM | ✅ | ✅ | ✅ (VACE) | — | — | — | ✅ | |
| Wan 2.1 FLF2V | — | ✅ | — | — | — | — | ✅ | |
| Hunyuan Video Low-VRAM | ✅ | ✅ | — | — | — | — | — | |
| Qwen Image 2.1 Ultimate · 12 GB | — | — | — | ✅ | ✅ | — | — | Turbo · ControlNet pose/depth/edges · remove background |
| Qwen Image 2.1 · 12 GB | — | — | — | ✅ | — | — | — | native 2K |
| Qwen Image & Edit 2509 | — | — | — | ✅ | ✅ | — | — | |
| Krea 2 Ultimate · 12 GB | — | — | — | ✅ | — | — | — | style reference · style LoRAs · Kroma |
| Ming Image 0.1 · 12 GB | — | — | — | ✅ | ✅ | — | — | real transparency (RGBA) |
| Flux Kontext GGUF | — | — | — | ✅ | ✅ | — | — | |
| Flux.2 Dev GGUF | — | — | — | ✅ | — | — | — | |
| Z-Image Turbo GGUF | — | — | — | ✅ | — | — | — | |
| Image to 3D Ultimate · 12 GB | — | — | — | — | — | — | — | image → textured .glb |
| YuE2 Music · 12 GB | — | — | — | — | — | ✅ (songs) | — | cover mode |
| AI Audio Maker | — | — | — | — | — | ✅ | — | video-sync |

## VRAM guidance

Minimum = will run (slowly, low quant). Comfortable = the creator's tested target. The **12 GB** workflows were each
tested on an RTX 3060 12 GB (times in their READMEs); some 12 GB models also run on 4 GB with a separate setup shown in
the videos (e.g. MiniMax H3 W4A8 on a 4 GB laptop) — that is not what the 12 GB workflow file loads.

| Workflow | Minimum | Comfortable | Tested hardware (from creator) |
|---|---|---|---|
| MiniMax H3 Ultimate · Viggle-Animate · LTX 2.5 Ultimate · H3 Character Swap | 12 GB | 12 GB + 32 GB RAM | RTX 3060 12 GB (H3 Ultimate also on a 4 GB laptop with the W4A8 model + Q2_K_M encoder: [benchmarks](BENCHMARKS.md)) |
| Krea 2 (Krea 2 Turbo int8 + Kroma w4a8) · Ming · YuE2 | 4 GB (16 GB RAM) | 12 GB | RTX 3060 12 GB · the same files on an RTX 3050 Ti Laptop 4 GB ([benchmarks](BENCHMARKS.md)) |
| Qwen Image 2.1 (both) | 4 GB with the w4a8 text encoder (16 GB RAM) | 12 GB | RTX 3060 12 GB · RTX 3050 Ti Laptop 4 GB ([benchmarks](BENCHMARKS.md)) |
| Image to 3D | 12 GB | 12 GB | RTX 3060 12 GB |
| Wan Animate Ultimate | 12 GB (Wan Animate 2) · lower in GGUF mode | 12 GB | RTX 3060 12 GB |
| Wan 2.1 GGUF Low-VRAM | 4 GB | 8–12 GB | RTX 3050 Laptop 4 GB |
| Wan 2.2 GGUF Low-VRAM | 4 GB (5B: 8 GB) | 12 GB | RTX 3050 Laptop 4 GB |
| Wan 2.2 Animate | 4 GB (Q4) | 12 GB (Q8) | RTX 3050 4 GB / RTX 3060 12 GB |
| Flux Kontext GGUF | 4 GB | 8 GB | 4 GB laptop |
| Qwen Image & Edit 2509 | 4 GB (Q4_K_S) | 12 GB (Q8) | 4 GB / 12 GB |
| Hunyuan Video Low-VRAM | 4 GB | 8 GB+ | RTX 3050 Laptop (slow) |
| LTX-2 GGUF | 4 GB (+Triton) | 12 GB | RTX 3060 12 GB + 48 GB RAM |
| LTX-2.3 Ultimate | 12 GB | 12 GB+ | RTX 3060 12 GB |
| Flux.2 / Z-Image / AI Audio / AIO Rapid | *Not tested here* | *Not tested here* | — |

System RAM matters as much as VRAM: the 12 GB workflows offload model parts to RAM (the H3 runs peaked at ~19 GB RAM).

## Video sizes and lengths (from ComfyUI's own nodes)

The Ultimates take **seconds + megapixels** and round for you. If you type frames / width / height yourself:

| Model | Frame count must be | e.g. | Width / height step |
|---|---|---|---|
| MiniMax H3 | 17·k + 5 | 124 frames ≈ 5.2 s at 24 fps | 32 |
| LTX (2 / 2.3 / 2.5) | 8·k + 1 | 97, 121 | 32 |
| Wan (2.1 / 2.2) | 4·k + 1 | 81 | 16 |

## Quantisation cheat-sheet (GGUF)

| Quant | Relative VRAM | Quality | Use when |
|---|---|---|---|
| Q8_0 | Highest | Best | You have the headroom |
| Q6_K / Q5_K_S / Q5_1 | Medium | Best balance | **Default recommendation** |
| Q4_K_M / Q4_K_S | Low | Good | 4 GB GPUs |
| Q3_K_M | Lower | Usable | Very tight VRAM |
| Q2_K | Lowest | Rough | Last resort / 14B on 4 GB |

The 12 GB Ultimates use **int8 convrot** `.safetensors` files (ComfyUI's own quantised format) instead of GGUF: they load
with the normal core loaders. A GGUF file needs a GGUF loader node, a `.safetensors` file the core loader — putting
one in the other is the classic "the workflow asks for gguf" error.

## Custom node packs per workflow

Read from each workflow's `.json` (node pack ids) and listed in its `models.json` — `frizzy.py nodes <workflow>`
installs them. **None** = core ComfyUI only (needs a recent ComfyUI: see the workflow's README, 0.39+ for the newest).

| Workflow | Path | Custom node packs |
|---|---|---|
| Image to 3D Ultimate · 12 GB | `3d/image-to-3d-ultimate-12gb` | **none** (core nodes) |
| AI Audio Maker | `audio/ai-audio-maker` | ComfyUI-MMAudio, ComfyUI-VideoHelperSuite |
| YuE2 Music · 12 GB | `audio/yue2-music-12gb` | **none** (core nodes) |
| Flux.2 Dev GGUF | `flux/flux2-dev` | ComfyUI-GGUF, ComfyUI-KJNodes |
| Flux Kontext GGUF | `flux/kontext` | gguf, rgthree-comfy, ComfyUI-KJNodes, ComfyUI_essentials, ComfyUI-TeaCache |
| Hunyuan Video Low-VRAM | `hunyuan/video` | gguf, ComfyUI-KJNodes, ComfyUI-VideoHelperSuite, rgthree-comfy, ComfyUI-HunyuanVideoWrapper, ComfyUI-HunyuanVideoSamplerSave |
| Krea 2 Ultimate · 12 GB | `krea/krea-2-ultimate-12gb` | **none** (core nodes) |
| LTX 2.5 Ultimate · 12 GB | `ltx/ltx-2.5-ultimate-12gb` | **none** (core nodes) |
| LTX-2.3 Ultimate | `ltx/ltx2.3-ultimate` | ComfyUI-GGUF, ComfyUI-KJNodes, ComfyUI-JakeUpgrade, ComfyUI-VideoHelperSuite, ComfyUI-Impact-Pack, ComfyUI-Easy-Use |
| LTX-2 GGUF | `ltx/ltx2` | ComfyUI-GGUF, ComfyUI-KJNodes |
| Ming Image 0.1 · 12 GB | `ming/image-0.1-design-12gb` | **none** (core nodes) |
| MiniMax H3 Ultimate · 12 GB | `minimax/h3-ultimate-12gb` | **none** (core nodes) |
| Viggle-Animate (H3) | `minimax/viggle-animate-h3` | ComfyUI-Viggle-Animate-H3 |
| Qwen Image 2.1 · 12 GB | `qwen/image-2.1-12gb` | **none** (core nodes) |
| Qwen Image 2.1 Ultimate · 12 GB | `qwen/image-2.1-ultimate-12gb` | **none** (core nodes) |
| Qwen Image & Edit 2509 | `qwen/image-edit-2509` | ComfyUI-GGUF, ComfyUI-KJNodes |
| Wan 2.1 FLF2V | `wan2.1/flf2v` | gguf, tiled_ksampler, ComfyUI-KJNodes, ComfyUI-VideoHelperSuite, rgthree-comfy, ComfyUI-Frame-Interpolation |
| Wan 2.1 GGUF Low-VRAM | `wan2.1/gguf-lowvram` | gguf, tiled_ksampler, ComfyUI-KJNodes, ComfyUI-VideoHelperSuite, rgthree-comfy, ComfyUI-Frame-Interpolation |
| Wan 2.2 AIO Rapid | `wan2.2/aio-rapid` | ComfyUI-KJNodes, ComfyUI-WanVideoWrapper, ComfyUI-VideoHelperSuite, tiled_ksampler |
| Wan Animate Ultimate | `wan2.2/animate-ultimate` | **none** in Wan Animate 2 mode · ComfyUI-GGUF in GGUF mode |
| Wan 2.2 Animate | `wan2.2/animate` | comfyui_controlnet_aux, ComfyUI-KJNodes, ComfyUI-segment-anything-2, ComfyUI-VideoHelperSuite, execution-inversion-demo-comfyui, ComfyUI_essentials, ComfyUI-Custom-Scripts, ComfyUI-Frame-Interpolation |
| Wan 2.2 GGUF Low-VRAM | `wan2.2/gguf-lowvram` | gguf, tiled_ksampler, ComfyUI-KJNodes, ComfyUI-VideoHelperSuite, ComfyUI-Frame-Interpolation, ComfyUI-tbox |
| Z-Image Turbo GGUF | `z-image/turbo` | ComfyUI-GGUF, ComfyUI-KJNodes |

`gguf` = [calcuis/gguf](https://github.com/calcuis/gguf) (its `LoaderGGUF` nodes), not the same pack as
[city96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) (`UnetLoaderGGUF`). Links for every pack are in each
workflow's `downloads.md`.

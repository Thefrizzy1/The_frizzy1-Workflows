# The_frizzy1: Wan 2.2 Animate v1.2.1

<a href="https://www.youtube.com/watch?v=rtyfdmL-wF4&list=PLRe4JVWoY_AU"><img src="https://img.youtube.com/vi/rtyfdmL-wF4/mqdefault.jpg" width="640" alt="Watch the video"></a>

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> Drive motion from a reference video onto a character image, with a looping mechanism for **unlimited-length** output. GGUF-quantised to run from **4 GB VRAM**.

| | |
|---|---|
| **Model family** | Wan 2.2 Animate (14B) |
| **Tasks** | Video-to-video character animation · looping |
| **Min VRAM** | 4 GB (Q4, 25 frames/loop) |
| **Comfortable** | 12 GB (up to Q8, 25 frames/loop) |
| **Tested on** | RTX 3050 4 GB · RTX 3060 12 GB |
| **ComfyUI** | A recent ComfyUI with subgraph support (saved with frontend 1.33.14). Checked on ComfyUI 0.45.3: the graph converts to an API prompt. Its custom packs are not installed on the 0.45.3 check server, so it was not validated there or GPU-tested on 0.45.3. |
| **CivitAI** | https://civitai.com/models/2046477 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Wan22ANIMATE |
| **YouTube explainer** | https://www.youtube.com/watch?v=rtyfdmL-wF4&list=PLRe4JVWoY_AU |
| **License** | Workflow: MIT · Apache-2.0 (Wan-AI/Wan2.2-Animate-14B) |
| **Newer** | [Wan Animate Ultimate · 12 GB](../animate-ultimate) (Wan Animate 2, core nodes; its GGUF mode replaces this workflow). |

## Overview
Wan 2.2 Animate takes a **reference image** (the character) plus an **input/driving video** (the motion) and
animates the character to match. This build wraps the 14B model in GGUF form and adds a **looping mechanism**
so you can chain segments into arbitrarily long videos on low-VRAM hardware. It is **not** a text-to-video
model. If you want to generate video from a prompt, use
[Wan 2.2 GGUF Low-VRAM](../gguf-lowvram) or [Wan 2.1](../../wan2.1/gguf-lowvram) instead
(see [the Wan lineage note](../../../docs/WAN-LINEAGE.md)).

## Capabilities
- Reference-driven character animation (video → video).
- Unlimited length via looping (25 frames per loop).
- Green/red point editing to mark what to keep vs. change in the detection subgraph.
- Optional relight LoRA for lighting consistency; lightx2v LoRA for speed.

## Hardware & VRAM
| VRAM | Recommended quant | Frames/loop |
|---|---|---|
| 4 GB | Q4_K_M (~10–12 GB with offload) | 25 |
| 12 GB | up to Q8_0 | 25 |
| 20 GB+ | Q6_K / Q8_0 | 25+ |

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor wan2.2/animate --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full verified table with links: **[downloads.md](downloads.md)**. Summary (all read from the workflow JSON):

- Diffusion: `Wan2.2-Animate-14B-Q8_0.gguf` (or `Q5_K_S` / `Q4_K_M`)
- Text encoder: `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- CLIP vision: `clip_vision_h.safetensors`
- VAE: `Wan2.1_VAE.pth` (or the same VAE as `wan_2.1_vae.safetensors`, picked in the loader)
- LoRAs: `WanAnimate_relight_lora_fp16.safetensors`; speed LoRA: the graph loads `high_noise_model(wan2.2light2xvI2v_v2.2).safetensors`, use `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` and pick it in the loader
- Frame interp: `rife49.pth` (downloaded by ComfyUI-Frame-Interpolation on first run)

## Required custom nodes
| Node | Link |
|---|---|
| comfyui_controlnet_aux | https://github.com/Fannovel16/comfyui_controlnet_aux |
| KJNodes | https://github.com/kijai/ComfyUI-KJNodes |
| segment-anything-2 | https://github.com/kijai/ComfyUI-segment-anything-2 |
| VideoHelperSuite | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| Execution Inversion Demo | https://github.com/BadCafeCode/execution-inversion-demo-comfyui |
| ComfyUI_essentials | https://github.com/cubiq/ComfyUI_essentials |
| ComfyUI-Custom-Scripts | https://github.com/pythongosssss/ComfyUI-Custom-Scripts |
| ComfyUI-Frame-Interpolation | https://github.com/Fannovel16/ComfyUI-Frame-Interpolation |

Not core in ComfyUI 0.45.3, so still needed: DWPose and PixelPerfectResolution (controlnet_aux), SAM2 (segment-anything-2), GGUFLoaderKJ / ColorMatch / PointsEditor (KJNodes), Load Video (VHS), For Loop (execution-inversion), MaskPreview+ (essentials), Math Expression (Custom-Scripts), RIFE VFI (Frame-Interpolation). Core 0.45.3 has FrameInterpolate, but this graph keeps RIFE VFI (see changelog).

## Optional custom nodes
| Node | Link | Why |
|---|---|---|
| IAMCCS-nodes | https://github.com/IAMCCS/IAMCCS-nodes | Only needed for the older v1.0 graph |

## Installation
1. Install the custom nodes above via ComfyUI Manager, then restart.
2. Download every file in [downloads.md](downloads.md) into the listed `ComfyUI/models/` folders.
3. Load `The_frizzy1_wan-2.2-animate_v1.2.1.json` in ComfyUI. The **How to use** note on the far left explains every input and setting.
4. Upload your **reference image** and **input video**.
5. In the detection subgraph, set **green points** on what to keep and **red points** on what to change.
6. Ensure **width and height are multiples of 16**.
7. Run. The output saves automatically.

## Recommended settings
| Setting | Value | Notes |
|---|---|---|
| Frames per loop | 25 | Balance of coherence and VRAM |
| Quant | Q4 (4 GB) / Q8 (12 GB) | See table above |
| Dimensions | multiples of 16 | Required or the sample will error |

## Performance
Not verified numerically. On 4 GB expect long render times; 12 GB is the comfortable target. Looping keeps
per-segment VRAM flat regardless of final length.

## Known issues
- **Non-multiple-of-16 dimensions** → sampler error. Fix: round W/H to nearest 16.
- **Wrong VAE / text encoder** (using a 2.1 or 2.2-5B file) → garbled or black frames. Use the exact files in
  [downloads.md](downloads.md).
- **Missing segment-anything-2 / controlnet_aux** → detection subgraph won't build. Install and restart.

## Changelog
See [changelog.md](changelog.md).

## Files in this folder
- `The_frizzy1_wan-2.2-animate_v1.2.1.json`: the workflow, templated name (this is the GGUF build).
- `source/`: the original files (`wan22animate-gguf.json`, `wan22animate.json`) and the previous `The_frizzy1_wan-2.2-animate_v1.2.0.json`.

## Related workflows
- [Wan 2.2 GGUF Low-VRAM](../gguf-lowvram): text/image → video.
- [Wan 2.1 GGUF Low-VRAM](../../wan2.1/gguf-lowvram): lighter, older path.
- [Wan lineage & compatibility](../../../docs/WAN-LINEAGE.md).

# The_frizzy1 — Wan 2.2 Animate v1.2.0

> Drive motion from a reference video onto a character image — with a looping mechanism for **unlimited-length** output. GGUF-quantised to run from **4 GB VRAM**.

| | |
|---|---|
| **Model family** | Wan 2.2 Animate (14B) |
| **Tasks** | Video-to-video character animation · looping |
| **Min VRAM** | 4 GB (Q4, 25 frames/loop) |
| **Comfortable** | 12 GB (up to Q8, 25 frames/loop) |
| **Tested on** | RTX 3050 4 GB · RTX 3060 12 GB |
| **CivitAI** | https://civitai.com/models/2046477 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Wan22ANIMATE |
| **YouTube explainer** | https://www.youtube.com/watch?v=rtyfdmL-wF4 |
| **License** | OpenRAIL (base model: Wan-AI/Wan2.2-Animate-14B) |

## Overview
Wan 2.2 Animate takes a **reference image** (the character) plus an **input/driving video** (the motion) and
animates the character to match. This build wraps the 14B model in GGUF form and adds a **looping mechanism**
so you can chain segments into arbitrarily long videos on low-VRAM hardware. It is **not** a text-to-video
model — if you want to generate video from a prompt, use
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

## Required models
Full verified table with links: **[downloads.md](downloads.md)**. Summary (all read from the workflow JSON):

- Diffusion: `Wan2.2-Animate-14B-Q8_0.gguf` (or `Q5_K_S` / `Q4_K_M`)
- Text encoder: `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- CLIP vision: `clip_vision_h.safetensors`
- VAE: `wan_2.1_vae.safetensors`
- LoRAs: `WanAnimate_relight_lora_fp16.safetensors`, `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
- Frame interp: `rife49.pth`

## Required custom nodes
| Node | Link |
|---|---|
| comfyui_controlnet_aux | https://github.com/Fannovel16/comfyui_controlnet_aux |
| KJNodes | https://github.com/kijai/ComfyUI-KJNodes |
| segment-anything-2 | https://github.com/kijai/ComfyUI-segment-anything-2 |
| VideoHelperSuite | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| Execution Inversion Demo | https://github.com/BadCafeCode/execution-inversion-demo-comfyui |

## Optional custom nodes
| Node | Link | Why |
|---|---|---|
| IAMCCS-nodes | https://github.com/IAMCCS/IAMCCS-nodes | Only needed for the older v1.0 graph |

## Installation
1. Install the custom nodes above via ComfyUI Manager, then restart.
2. Download every file in [downloads.md](downloads.md) into the listed `ComfyUI/models/` folders.
3. Load `The_frizzy1_wan-2.2-animate_v1.2.0.json` in ComfyUI.
4. Upload your **reference image** and **input video**.
5. In the detection subgraph, set **green points** on what to keep and **red points** on what to change.
6. Ensure **width and height are multiples of 16**.
7. Run — output saves automatically.

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
- `The_frizzy1_wan-2.2-animate_v1.2.0.json` — the workflow, templated name (this is the GGUF build).
- `source/` — the original unmodified files (`Wan2.2-Animate-GGUF.json`, `Wan2.2 Animate.json`).

## Related workflows
- [Wan 2.2 GGUF Low-VRAM](../gguf-lowvram) — text/image → video.
- [Wan 2.1 GGUF Low-VRAM](../../wan2.1/gguf-lowvram) — lighter, older path.
- [Wan lineage & compatibility](../../../docs/WAN-LINEAGE.md).

# The_frizzy1 — Wan 2.2 GGUF Low-VRAM v1.0.0

> Wan 2.2 T2V, I2V (14B dual-expert) and hybrid TI2V-5B on **4 GB VRAM** with GGUF + lightx2v LoRA.

| | |
|---|---|
| **Model family** | Wan 2.2 (A14B MoE + 5B) |
| **Tasks** | T2V · I2V · TI2V (hybrid) |
| **Min VRAM** | 4 GB (5B: 8 GB) |
| **Tested on** | RTX 3050 Laptop 4 GB |
| **CivitAI** | https://civitai.com/models/1817858 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Wan22-T2V-I2V-LORA-4GB |
| **YouTube** | https://www.youtube.com/watch?v=C7ZttV320qk |
| **License** | Apache-2.0 |

## Overview
Wan 2.2 uses a **Mixture-of-Experts** design — a *high-noise* and a *low-noise* expert — for better motion and
cinematics than 2.1. **The 14B paths load two GGUFs** (high + low). The 5B TI2V path is a single file and runs
on ~8 GB with offloading. Read [the Wan lineage note](../../../docs/WAN-LINEAGE.md) — this is the #1 source of load errors.

## Included workflows
| File | Task |
|---|---|
| `The_frizzy1_wan-2.2-t2v-14b_v1.0.0.json` | Text → Video (14B, high+low noise) |
| `The_frizzy1_wan-2.2-i2v-14b_v1.0.0.json` | Image → Video (14B, high+low noise) |
| `source/Wan2.2- 5B T2V.json` / `source/Wan2.2- 5B I2V.json` | TI2V-5B (single file) |

## Recommended settings (from creator)
- Use **14B models**; lightx2v LoRA strongly recommended.
- Without LoRA: **CFG 6, 30–60 steps**.
- Second-sampler denoise: **0.3–0.5** for 14B.

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Required custom nodes
| Node | Link |
|---|---|
| GGUF | https://github.com/calcuis/gguf |
| WanVideoWrapper | https://github.com/kijai/ComfyUI-WanVideoWrapper |
| Tiled KSampler | https://github.com/FlyingFireCo/tiled_ksampler |
| KJNodes | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| rgthree-comfy *(LoRA stacking only)* | https://github.com/rgthree/rgthree-comfy |

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Wan 2.1 GGUF Low-VRAM](../../wan2.1/gguf-lowvram) · [Wan 2.2 Animate](../animate) · [Wan 2.2 AIO Rapid](../aio-rapid)

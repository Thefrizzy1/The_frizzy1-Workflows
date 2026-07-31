# The_frizzy1 — Wan 2.1 GGUF Low-VRAM v2.0.0

> A six-in-one Wan 2.1 video pack — T2V, I2V, VACE, First/Last-Frame and experimental Fun controls — running from **4 GB VRAM** with GGUF quantisation.

| | |
|---|---|
| **Model family** | Wan 2.1 (1.3B + 14B) |
| **Tasks** | T2V · I2V · VACE · FLF · Fun Control · Fun Camera |
| **Min VRAM** | 4 GB |
| **Tested on** | RTX 3050 Laptop 4 GB |
| **CivitAI** | https://civitai.com/models/1309674 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Wan21-GGUF-4GB-Workflow |
| **YouTube** | https://www.youtube.com/watch?v=Xqjabf_eQ_U |
| **License** | Apache-2.0 |

## Overview
The lightest video path in the collection. Uses GGUF-quantised Wan 2.1 models plus Kijai's WanVideoWrapper.
On the smallest GPUs the 1.3B models are faster and lighter than any Wan 2.2 path — see
[the Wan lineage note](../../../docs/WAN-LINEAGE.md) before mixing files between 2.1 and 2.2.

## Included workflows
| File | Task |
|---|---|
| `The_frizzy1_wan-2.1-t2v_v2.0.0.json` | Text → Video (1.3B) |
| `The_frizzy1_wan-2.1-i2v_v2.0.0.json` | Image → Video (14B 480p) |
| `source/Wan2.1-Vace.json` | VACE (1.3B) |
| `source/Wan2.1-FirstFrameLastFrame.json` | First → Last frame |
| `source/Wan2.1-FunControl (experimental).json` | Fun Control |
| `source/Wan2.1-CameraImage (experimental).json` | Fun Camera |

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

## Quantisation guide
| Level | VRAM | Quality |
|---|---|---|
| Q5 | Medium | Best balance |
| Q3_K_M | Low | Good |
| Q2_K | Lowest | Usable |
| 14B (F16) | High | Best quality |

## Performance tips
Enable **Xformers**, **Sage Attention** or **Triton** for extra speed.
Triton/Sage guide: https://www.patreon.com/posts/easy-guide-sage-124253103

## Known issues & helpful links
- Common errors: https://civitai.com/articles/17240
- Prompting tips: https://www.reddit.com/r/StableDiffusion/comments/1j1r791/wan_21_comfyui_prompting_tips
- CFG & shift values: https://www.reddit.com/r/StableDiffusion/comments/1j2q0xw/dont_overlook_the_values_of_shift_and_cfg_on_wan

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Wan 2.2 GGUF Low-VRAM](../../wan2.2/gguf-lowvram) · [Wan 2.2 Animate](../../wan2.2/animate) · [Wan 2.1 FLF2V](../flf2v)

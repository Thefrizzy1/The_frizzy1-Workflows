# The_frizzy1 — LTX-2 GGUF v2.0.0
> Simple color-coded LTXV-2 workflow (I2V + T2V, audio-aware). Lightweight; runs from **4 GB** with Triton, comfortable at 12 GB.

| | |
|---|---|
| **Model family** | LTXV-2 (19B) |
| **Tasks** | Text → Video · Image → Video · Audio |
| **Workflow file** | `The_frizzy1_ltx2-i2v_v2.0.0.json` · `The_frizzy1_ltx2-t2v_v2.0.0.json` |
| **Min VRAM** | 4 GB (+Triton) |
| **Tested on** | RTX 3060 12GB + 48GB RAM · RTX 3050 4GB (Triton) |
| **CivitAI** | https://civitai.com/models/2339823 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/LTX2-GGUF-workflow |
| **YouTube** | https://www.youtube.com/watch?v=nnHUBMgdJac |
| **License** | Workflow: MIT · LTX-2 Community License Agreement · Gemma 3 text encoder: Gemma Terms of Use |
| **Newer** | [LTX 2.5 Ultimate](../../ltx/ltx-2.5-ultimate-12gb) (12 GB). |

## Common issues
- `LTXVEmptyLatentAudio – AttributeError` → update **KJNodes to v1.2.8+**.
- Checkerboard noise → update all nodes + ComfyUI.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor ltx/ltx2 --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required custom nodes
| Node | Link |
|---|---|
| ComfyUI-GGUF | https://github.com/city96/ComfyUI-GGUF |
| KJNodes *(keep updated!)* | https://github.com/kijai/ComfyUI-KJNodes |

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [LTX-2.3 Ultimate](../ltx2.3-ultimate) — newer 22B generation.

# The_frizzy1 — Wan 2.2 AIO Rapid v1.0.0

> All-in-one Wan 2.2 T2V + I2V from a **single** "mega AIO" GGUF file. 4–12 GB VRAM. The simplest 2.2 path.

| | |
|---|---|
| **Model family** | Wan 2.2 (rapid mega AIO) |
| **Tasks** | Text → Video · Image → Video |
| **Min VRAM** | 4–12 GB |
| **CivitAI** | https://civitai.com/models/2522688 |
| **YouTube** | https://www.youtube.com/watch?v=RdsyWkvG1nE |
| **License** | Apache-2.0 |

## Overview
Unlike the standard [Wan 2.2 pack](../gguf-lowvram) — which loads separate high-noise and low-noise
experts — this uses a **single merged "rapid mega AIO" GGUF** for both T2V and I2V. Fewer downloads, faster
setup, at some quality/flexibility cost. Models verified from the workflow JSON.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor wan2.2/aio-rapid --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Wan 2.2 GGUF Low-VRAM](../gguf-lowvram) (dual-expert) · [Wan lineage note](../../../docs/WAN-LINEAGE.md)

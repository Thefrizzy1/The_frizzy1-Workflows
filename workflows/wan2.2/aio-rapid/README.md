# The_frizzy1 — Wan 2.2 AIO Rapid v1.0.0

<a href="https://www.youtube.com/watch?v=RdsyWkvG1nE&list=PLRe4JVWoY_AU"><img src="https://img.youtube.com/vi/RdsyWkvG1nE/mqdefault.jpg" width="640" alt="Watch the video"></a>

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> All-in-one Wan 2.2 T2V + I2V from a **single** "mega AIO" GGUF file. 4–12 GB VRAM. The simplest 2.2 path.

| | |
|---|---|
| **Model family** | Wan 2.2 (rapid mega AIO) |
| **Tasks** | Text → Video · Image → Video |
| **Workflow file** | `The_frizzy1_wan-2.2-aio-rapid_v1.0.0.json` |
| **Min VRAM** | 4–12 GB |
| **CivitAI** | https://civitai.com/models/2522688 |
| **YouTube** | https://www.youtube.com/watch?v=RdsyWkvG1nE&list=PLRe4JVWoY_AU |
| **License** | Apache-2.0 |
| **Newer** | [MiniMax H3 Ultimate](../../minimax/h3-ultimate-12gb) · [LTX 2.5 Ultimate](../../ltx/ltx-2.5-ultimate-12gb) (12 GB). |

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

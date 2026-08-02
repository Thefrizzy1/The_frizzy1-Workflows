# The_frizzy1 — Flux.2 Dev GGUF v1.0.0

> The newest Flux image model (Flux.2 Dev), GGUF-quantised for low VRAM. Simple, single-pass generation.

| | |
|---|---|
| **Model family** | Flux.2 Dev |
| **Tasks** | Text → Image |
| **Min VRAM** | 6 GB (estimate — verify on your card) |
| **CivitAI** | https://civitai.com/models/2508110 |
| **YouTube** | https://www.youtube.com/watch?v=dcekWAbgDXg |
| **License** | FLUX.2 [dev] (Black Forest Labs) — check model card |


## Preview

<p align="center">
  <img src="samples/sample-1.webp" width="46%" alt="Flux.2 Dev sample 1">
  <img src="samples/sample-2.webp" width="46%" alt="Flux.2 Dev sample 2">
</p>

<sub>Example outputs from this workflow.</sub>

## Overview
A minimal, beginner-friendly Flux.2 Dev workflow. Uses a Mistral-based text encoder (new in Flux.2) and the
Flux.2 VAE. Models verified from the workflow JSON.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor flux/flux2-dev --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Flux Kontext GGUF](../kontext)

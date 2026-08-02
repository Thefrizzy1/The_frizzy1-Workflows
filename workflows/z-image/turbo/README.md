# The_frizzy1 — Z-Image Turbo GGUF v1.0.0

> Fast, tiny text-to-image with Z-Image Turbo, GGUF-quantised for **4 GB VRAM**. Beginner friendly.

| | |
|---|---|
| **Model family** | Z-Image Turbo |
| **Tasks** | Text → Image (few-step turbo) |
| **Min VRAM** | 4 GB |
| **CivitAI** | https://civitai.com/models/2561639 |
| **License** | Check Z-Image model card |


## Preview

<p align="center">
  <img src="samples/sample-1.webp" width="30%" alt="Z-Image Turbo sample 1">
  <img src="samples/sample-2.webp" width="30%" alt="Z-Image Turbo sample 2">
  <img src="samples/sample-3.webp" width="30%" alt="Z-Image Turbo sample 3">
</p>

<sub>Example outputs from this workflow.</sub>

## Overview
A lightweight turbo image workflow. Uses a Qwen-3 4B text encoder and the Flux-style `ae` VAE.
Models verified from the workflow JSON.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor z-image/turbo --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Qwen Image & Edit 2509](../../qwen/image-edit-2509) · [Flux Kontext GGUF](../../flux/kontext)

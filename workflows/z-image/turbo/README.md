# The_frizzy1 - Z-Image Turbo GGUF v1.0.1

> Fast, tiny text-to-image with Z-Image Turbo, GGUF-quantised for **4 GB VRAM**. Beginner friendly.

| | |
|---|---|
| **Model family** | Z-Image Turbo |
| **Tasks** | Text → Image (few-step turbo) |
| **Workflow file** | `The_frizzy1_z-image-turbo-gguf_v1.0.1.json` |
| **Needs** | ComfyUI with subgraph support (made on ComfyUI 0.3.73, frontend 1.42.11) · custom nodes: ComfyUI-GGUF, ComfyUI-KJNodes |
| **Nodes** | Core: CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, ModelSamplingAuraFlow, KSampler, VAEDecode, SaveImage · KJNodes: GGUFLoaderKJ (GGUF loading is not core) |
| **Checked on** | ComfyUI 0.45.3: v1.0.1 converts and validates (notes only changed since v1.0.0) |
| **Also run on** | v1.0.0 on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, sage attention: 1088x1920, 8 steps, about 24 s per image warm, 19.0 to 19.4 GB peak VRAM (24 GB server runs, `report/results.json`) |
| **Min VRAM** | 4 GB |
| **CivitAI** | https://civitai.com/models/2561639 |
| **License** | Workflow: MIT · Apache-2.0 (Tongyi-MAI/Z-Image-Turbo) |


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

In ComfyUI: a **How to use** note and a **Downloads** note sit left of the graph. Every setting is on the **Text to Image (Z-Image-Turbo)** node (prompt, width, height, text encoder, VAE, steps); the GGUF loader is inside it.

Faster attention: start ComfyUI with `--use-sage-attention` (less VRAM). `--use-ck-attention` changes the image for the same seed.

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

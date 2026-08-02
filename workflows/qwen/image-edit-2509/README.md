# The_frizzy1 — Qwen Image & Edit 2509 GGUF v1.0.0

> Beginner-friendly Qwen Image generation **and editing** on low/mid hardware. GGUF + optional Lightning LoRAs.

| | |
|---|---|
| **Model family** | Qwen Image |
| **Tasks** | Text → Image · Image editing (2509) |
| **Min VRAM** | 4 GB (Q4_K_S) / 12 GB (Q8) |
| **CivitAI** | https://civitai.com/models/2229874 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Qwen-Image-Edit-2509-GGUF |
| **YouTube** | https://www.youtube.com/watch?v=NPni2ulov34 |
| **License** | Apache-2.0 |


## Preview

<p align="center">
  <img src="samples/sample-1.webp" width="46%" alt="Qwen Image & Edit sample 1">
  <img src="samples/sample-2.webp" width="46%" alt="Qwen Image & Edit sample 2">
</p>

<sub>Example outputs from this workflow.</sub>

## Usage
- **Generation:** connect EmptyLatent → K-Sampler.
- **Editing:** activate all nodes except unused image inputs, connect latent → K-Sampler.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor qwen/image-edit-2509 --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## File placement
```
ComfyUI/models/
├── diffusion_models/   ← Qwen GGUF
├── loras/              ← Lightning LoRAs
├── vae/                ← qwen_image_vae.safetensors
└── text_encoders/      ← qwen_2.5_vl_7b_fp8_scaled.safetensors
```

## Required custom nodes
| Node | Link |
|---|---|
| KJNodes | https://github.com/kijai/ComfyUI-KJNodes |

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Flux Kontext GGUF](../../flux/kontext) · [Z-Image Turbo](../../z-image/turbo)

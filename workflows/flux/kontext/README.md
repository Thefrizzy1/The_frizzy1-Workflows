# The_frizzy1 — Flux Kontext GGUF v2.2.0

> Realistic, cinematic image generation **and editing** with Flux Dev / Schnell / Kontext on **4 GB VRAM**. Two-pass sampling + Torch TeaCache for speed.

| | |
|---|---|
| **Model family** | Flux (Dev · Schnell · Kontext) |
| **Tasks** | Text → Image · Image editing |
| **Min VRAM** | 4 GB |
| **CivitAI** | https://civitai.com/models/1311703 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Flux-Kontext-GGUF-4GB |
| **YouTube** | https://www.youtube.com/watch?v=4C0RJ01yRok |
| **License** | FLUX.1 [dev] Non-Commercial (Black Forest Labs) |


## Preview

<p align="center">
  <img src="samples/sample-1.webp" width="46%" alt="Flux Kontext sample 1">
  <img src="samples/sample-2.webp" width="46%" alt="Flux Kontext sample 2">
</p>

<sub>Example outputs from this workflow.</sub>

## Overview
Semi-realistic results in ~30 steps on a 4 GB laptop. Two samplers plus Torch TeaCache. **Kontext** adds
image editing on top of generation. Three optional style LoRAs ship referenced in the graph.

## Model guide
| Model | Best for |
|---|---|
| Kontext | Quality + image editing |
| Dev | Quality generation |
| Schnell | Speed, fewer steps |
| PixelWave | Best realism |

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor flux/kontext --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Quantisation
| Quant | Notes |
|---|---|
| q8 | Best quality |
| q5 | Best quality/speed balance |
| < q5 | Less VRAM, lower quality |

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [Flux.2 Dev GGUF](../flux2-dev) · [Qwen Image & Edit 2509](../../qwen/image-edit-2509)

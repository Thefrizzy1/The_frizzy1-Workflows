# The_frizzy1 - Flux Kontext GGUF v2.3.0

<a href="https://www.youtube.com/watch?v=4C0RJ01yRok&list=PLG_da2oqTx7k"><img src="https://img.youtube.com/vi/4C0RJ01yRok/mqdefault.jpg" width="640" alt="Watch the video"></a>

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> Realistic, cinematic image generation **and editing** with Flux Dev / Schnell / Kontext on **4 GB VRAM**. Two-pass sampling + core EasyCache for speed.

| | |
|---|---|
| **Model family** | Flux (Dev · Schnell · Kontext) |
| **Tasks** | Text → Image · Image editing |
| **Workflow file** | `The_frizzy1_flux-kontext-gguf_v2.3.0.json` |
| **Min VRAM** | 4 GB |
| **CivitAI** | https://civitai.com/models/1311703 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/Flux-Kontext-GGUF-4GB |
| **YouTube** | https://www.youtube.com/watch?v=4C0RJ01yRok&list=PLG_da2oqTx7k |
| **License** | FLUX.1 [dev] Non-Commercial (Black Forest Labs) |
| **Newer** | [Qwen Image 2.1 Ultimate](../../qwen/image-2.1-ultimate-12gb) (12 GB: edit + Turbo + ControlNet). On 4 GB: Qwen Image & Edit 2509. |


## Preview

<p align="center">
  <img src="samples/sample-1.webp" width="46%" alt="Flux Kontext sample 1">
  <img src="samples/sample-2.webp" width="46%" alt="Flux Kontext sample 2">
</p>

<sub>Example outputs from this workflow.</sub>

## Overview
Semi-realistic results in ~30 steps on a 4 GB laptop. Two samplers plus core EasyCache. **Kontext** adds
image editing on top of generation. Three optional style LoRAs ship referenced in the graph.
Note: the shipped graph has no image input (no ReferenceLatent), so as shipped it does text to image only.

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

## ComfyUI version and nodes
In-graph notes: **How to use** and **Downloads** (left of the graph).

Core nodes (ComfyUI 0.45+ for EasyCache): DualCLIPLoader, VAELoader, EasyCache, CLIPTextEncode, EmptyLatentImage, VAEDecode, UpscaleModelLoader,
ImageUpscaleWithModel, ImageScale, SaveImage, MarkdownNote.

Custom nodes: LoaderGGUF ([gguf](https://github.com/calcuis/gguf)), Lora Loader Stack ([rgthree-comfy](https://github.com/rgthree/rgthree-comfy)),
TorchCompileModelFluxAdvancedV2 ([ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)),
FluxSamplerParams+ ([ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)). ComfyUI-TeaCache is no longer needed.

Run on ComfyUI 0.45.3 (RTX PRO 4000 24 GB, 64 GB RAM, sage attention), seed 42, the 3 style LoRAs set to None (not on the test server): 83 s first run with EasyCache, 134 s with EasyCache set to never reuse. The 35-step pass: 1.34 s/it with EasyCache, 3.21 s/it without (2.4x faster); same scene, pose and light, small details differ. Not run on a 4 GB card with v2.3.0.

Faster attention: start ComfyUI with --use-sage-attention (less VRAM). --use-ck-attention changes the image for the same seed.

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

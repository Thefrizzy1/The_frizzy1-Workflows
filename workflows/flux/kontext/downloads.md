# Downloads — Flux Kontext GGUF v2.2.0

Verified from the workflow JSON. Diffusion → `diffusion_models/` (or `unet/`), VAE → `vae/`, encoders → `text_encoders/`.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `flux1-kontext-dev-Q5_1.gguf` | [QuantStack/FLUX.1-Kontext-dev-GGUF](https://huggingface.co/QuantStack/FLUX.1-Kontext-dev-GGUF) | JSON |
| Diffusion (alt) | FLUX.1 Dev / Schnell / PixelWave GGUF | [city96/FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf) · [schnell](https://huggingface.co/city96/FLUX.1-schnell-gguf) · [PixelWave](https://huggingface.co/mikeyandfriends/PixelWave_FLUX.1-dev_03) | README |
| VAE | `ae.safetensors` | [ffxvs/vae-flux](https://huggingface.co/ffxvs/vae-flux/blob/main/ae.safetensors) | JSON |
| CLIP | `clip_l.safetensors` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) | JSON |
| Text encoder | `t5xxl_fp8_e4m3fn.safetensors` | comfyanonymous/flux_text_encoders (or [t5 gguf](https://huggingface.co/city96/t5-v1_1-xxl-encoder-gguf)) | JSON |
| Style LoRA (opt) | `FC Flux Perfect Busts.safetensors` | CivitAI | JSON |
| Style LoRA (opt) | `FLUX_Polyhedron_all_Kohya_ss-000001.safetensors` | CivitAI | JSON |
| Style LoRA (opt) | `FluxDFaeTasticDetails.safetensors` | CivitAI | JSON |
| Upscale | `RealESRGAN_x4.pth` | RealESRGAN | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `flux1-kontext-dev-Q5_1.gguf` | [download](https://huggingface.co/QuantStack/FLUX.1-Kontext-dev-GGUF/resolve/main/flux1-kontext-dev-Q5_1.gguf) | Pick your quant from the repo. |
| required | `vae/` | `ae.safetensors` | [download](https://huggingface.co/ffxvs/vae-flux/resolve/main/ae.safetensors) |  |
| required | `text_encoders/` | `clip_l.safetensors` | [download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |  |
| required | `text_encoders/` | `t5xxl_fp8_e4m3fn.safetensors` | [download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors) |  |
| required | `upscale_models/` | `RealESRGAN_x4.pth` | [download](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | Upscaler, 0.07 GB |
| optional | `loras/` | `FC Flux Perfect Busts.safetensors` | [page](https://civitai.com/models) (by hand) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |
| optional | `loras/` | `FLUX_Polyhedron_all_Kohya_ss-000001.safetensors` | [page](https://civitai.com/models) (by hand) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |
| optional | `loras/` | `FluxDFaeTasticDetails.safetensors` | [page](https://civitai.com/models) (by hand) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |

**Custom node packs this workflow uses:** [gguf](https://github.com/calcuis/gguf), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials), [ComfyUI-TeaCache](https://github.com/welltop-cn/ComfyUI-TeaCache).

One command: `python scripts/frizzy.py doctor flux/kontext` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

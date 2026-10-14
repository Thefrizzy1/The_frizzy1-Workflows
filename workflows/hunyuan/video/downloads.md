# Downloads — Hunyuan Video Low-VRAM v1.1.1

Verified from the workflow JSON (with the v1.1.1 diffusion-model correction noted).

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion (recommended) | `fast-hunyuan-video-t2v-720p-Q5_K_M.gguf` | [city96/FastHunyuan-gguf](https://huggingface.co/city96/FastHunyuan-gguf) | JSON (v1.1.1) |
| Diffusion (standard alt) | HunyuanVideo GGUF | [city96/HunyuanVideo-gguf](https://huggingface.co/city96/HunyuanVideo-gguf) | README |
| VAE | `kijai_hunyuan_video_vae_bf16.safetensors` | [calcuis/hunyuan-gguf](https://huggingface.co/calcuis/hunyuan-gguf) | JSON |
| Text encoder | `llava_llama3_fp8_scaled.safetensors` | calcuis/hunyuan-gguf | JSON |
| CLIP | `clip_l.safetensors` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | JSON |
| Upscale | `4x-AnimeSharp.pth` | 4x-AnimeSharp | JSON |

> ⚠️ The original file referenced `flux1-dev-Q5_K_S.gguf` in the diffusion loader — that was a leftover, not a
> real dependency. v1.1.1 points at the Fast Hunyuan GGUF instead.

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `fast-hunyuan-video-t2v-720p-Q5_K_M.gguf` | [download](https://huggingface.co/city96/FastHunyuan-gguf/resolve/main/fast-hunyuan-video-t2v-720p-Q5_K_M.gguf) | Fast Hunyuan, recommended. |
| required | `text_encoders/` | `llava_llama3_fp8_scaled.safetensors` | [download](https://huggingface.co/calcuis/hunyuan-gguf/resolve/main/llava_llama3_fp8_scaled.safetensors) |  |
| required | `text_encoders/` | `clip_l.safetensors` | [download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |  |
| required | `vae/` | `kijai_hunyuan_video_vae_bf16.safetensors` | [download](https://huggingface.co/Kijai/HunyuanVideo_comfy/resolve/main/hunyuan_video_vae_bf16.safetensors) | Downloads Kijai/HunyuanVideo_comfy hunyuan_video_vae_bf16.safetensors and saves it under the name the workflow loads. 0.5 GB |
| required | `upscale_models/` | `4x-AnimeSharp.pth` | [download](https://huggingface.co/Kim2091/AnimeSharp/resolve/main/4x-AnimeSharp.pth) | Upscaler, 0.07 GB |

**Custom node packs this workflow uses:** [gguf](https://github.com/calcuis/gguf), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-HunyuanVideoWrapper](https://github.com/kijai/ComfyUI-HunyuanVideoWrapper), [ComfyUI-HunyuanVideoSamplerSave](https://github.com/ShmuelRonen/ComfyUI-HunyuanVideoSamplerSave).

One command: `python scripts/frizzy.py doctor hunyuan/video` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

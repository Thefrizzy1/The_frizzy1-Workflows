# Downloads - Qwen-Image-Layered v1.0.0

Verified from the workflow JSON. The three files the workflow loads were downloaded on 2026-11-24 and their size and SHA-256 matched the Hugging Face listings.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (fp8mixed) | `qwen_image_layered_fp8mixed.safetensors` | `diffusion_models/` | 20.5 GB | [Comfy-Org/Qwen-Image-Layered](https://huggingface.co/Comfy-Org/Qwen-Image-Layered/resolve/main/split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors) | JSON |
| Text encoder (Qwen2.5-VL 7B, fp8) | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.38 GB | [Comfy-Org/Qwen-Image](https://huggingface.co/Comfy-Org/Qwen-Image/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| VAE (layered, RGBA) | `qwen_image_layered_vae.safetensors` | `vae/` | 0.25 GB | [Comfy-Org/Qwen-Image-Layered](https://huggingface.co/Comfy-Org/Qwen-Image-Layered/resolve/main/split_files/vae/qwen_image_layered_vae.safetensors) | JSON |
| Diffusion model, bf16 (optional swap) | `qwen_image_layered_bf16.safetensors` | `diffusion_models/` | 40.9 GB | [Comfy-Org/Qwen-Image-Layered](https://huggingface.co/Comfy-Org/Qwen-Image-Layered/resolve/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors) | not in the JSON |

**What the workflow needs:** the first three files, about 30.2 GB. If you already run Qwen-Image or HunyuanVideo 1.5, you have the text encoder (same file, same SHA-256) and the new download is about 20.8 GB.

- The repo was called `Comfy-Org/Qwen-Image-Layered_ComfyUI` (the name the built-in template links); Hugging Face now redirects it to `Comfy-Org/Qwen-Image-Layered`.
- The text encoder link points to `Comfy-Org/Qwen-Image` (formerly `Comfy-Org/Qwen-Image_ComfyUI`); size and SHA-256 match the file tested here (checked 2026-11-24). The same file is also in `Comfy-Org/Hunyuan-Video-1.5`.
- The Comfy-Org repo listing (checked 2026-11-24) has the diffusion model as bf16 (40.9 GB) and fp8mixed (20.5 GB) only. There is no GGUF or int8 file in that repo, and core ComfyUI has no GGUF loader.
- The built-in template loads the bf16 file; its note points to fp8mixed for lower VRAM. This workflow loads fp8mixed. The bf16 file was not run.
- The VAE is not the normal Qwen-Image VAE: it decodes four channels (colour + transparency).

# Downloads - LongCat-Image · 12 GB v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-25 and its SHA-256 and size matched the Hugging Face file listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| LongCat-Image, text to image file | `longcat_image_bf16.safetensors` | `diffusion_models/` | 12.54 GB | [Comfy-Org/LongCat-Image](https://huggingface.co/Comfy-Org/LongCat-Image/resolve/main/split_files/diffusion_models/longcat_image_bf16.safetensors) | JSON |
| LongCat-Image-Edit-Turbo, edit file | `longcat_image_edit_turbo_bf16.safetensors` | `diffusion_models/` | 12.54 GB | [Comfy-Org/LongCat-Image](https://huggingface.co/Comfy-Org/LongCat-Image/resolve/main/split_files/diffusion_models/longcat_image_edit_turbo_bf16.safetensors) | JSON |
| Text encoder, both files | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.38 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| VAE, both files | `ae.safetensors` | `vae/` | 0.34 GB | [Comfy-Org/Z-Image-Turbo](https://huggingface.co/Comfy-Org/Z-Image-Turbo/resolve/main/split_files/vae/ae.safetensors) | JSON |

Each workflow needs one LongCat model plus the text encoder and VAE, about 22.3 GB; both need 34.8 GB.

- The templates link `Comfy-Org/HunyuanVideo_1.5_repackaged` and `Comfy-Org/z_image_turbo`; those repos now redirect to the names above.
- The Comfy-Org repo also has `longcat_image_edit_bf16.safetensors` (12.54 GB, the 50-step Edit model). Not used and not run here.

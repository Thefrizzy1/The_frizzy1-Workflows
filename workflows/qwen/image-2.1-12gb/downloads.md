# Downloads — Qwen Image 2.1 · 12 GB v1.0.0

Verified from the workflow JSON. File names and sizes checked on Hugging Face.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion | `qwen_image_2.1_int8_convrot.safetensors` | `diffusion_models/` | 7.3 GB | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | JSON |
| Text encoder | `qwen3vl_8b_int8_convrot.safetensors` | `text_encoders/` | 9.4 GB | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | JSON |
| VAE | `qwen_image_2.1_vae_bf16.safetensors` | `vae/` | 0.68 GB | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) | JSON |
| Turbo LoRA (TURBO only) | `Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256.safetensors` | `loras/` | 1.4 GB | [Viggle/Qwen-Image-2.1-viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256.safetensors) | JSON |

**Optional swaps (same repos, not in the JSON):**
- `qwen_image_2.1_bf16.safetensors` (14.2 GB) — the bigger diffusion model; ~1.6× slower on 12 GB, offloads to RAM.
- `qwen3vl_8b_w4a8.safetensors` (6.3 GB) — smaller text encoder, same speed, changes the picture with the same seed.

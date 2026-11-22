# Downloads - Anima v1.0.0

Verified from the workflow JSON file. Every file was downloaded on 2026-11-22 and its SHA-256 matched Hugging Face.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model | `anima-base-v1.0.safetensors` | `diffusion_models/` | 4.2 GB | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) | JSON |
| Text encoder | `qwen_3_06b_base.safetensors` | `text_encoders/` | 1.2 GB | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) | JSON |
| VAE | `qwen_image_vae.safetensors` | `vae/` | 0.25 GB | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) | JSON |
| Turbo LoRA (needed even with Turbo off) | `anima-turbo-lora-v0.2.safetensors` | `loras/` | 0.15 GB | [circlestone-labs/Anima-Official-LoRAs](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) | JSON |
| Diffusion model · Aesthetic (optional swap) | `anima-aesthetic-v1.1.safetensors` | `diffusion_models/` | 4.2 GB | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-aesthetic-v1.1.safetensors) | not in the JSON |
| Diffusion model · Turbo (optional swap) | `anima-turbo-v1.1.safetensors` | `diffusion_models/` | 4.2 GB | [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-turbo-v1.1.safetensors) | not in the JSON |

**What the workflow needs:** the first four files, about 5.8 GB. `qwen_image_vae.safetensors` is the Qwen Image VAE: if you already have that file, skip it.

**Why the LoRA is required:** ComfyUI checks that every file named in the graph exists before it runs. With a LoRA name that does not exist and Turbo off, the run was refused.

No Comfy-Org repackaged, fp8 or int8 Anima Base files were found on Hugging Face (2026-11-22), and the model is small (4.2 GB), so the workflow loads the authors' files, as the built-in template does. Community GGUF files exist; they were not tested.

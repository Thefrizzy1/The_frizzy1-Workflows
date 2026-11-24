# Downloads - ACE-Step 1.5 XL Music v1.1.0

Verified from the workflow JSON. The four required files were downloaded on 2026-11-22 and their SHA-256 matched Hugging Face. Sizes are decimal GB, as Hugging Face shows them.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (XL base, bf16) | `acestep_v1.5_xl_base_bf16.safetensors` | `diffusion_models/` | 9.97 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/diffusion_models/acestep_v1.5_xl_base_bf16.safetensors) | JSON |
| Text encoder (style and lyrics) | `qwen_0.6b_ace15.safetensors` | `text_encoders/` | 1.19 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) | JSON |
| Song planner, 4B | `qwen_4b_ace15.safetensors` | `text_encoders/` | 8.38 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) | JSON |
| VAE | `ace_1.5_vae.safetensors` | `vae/` | 0.34 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/vae/ace_1.5_vae.safetensors) | JSON |
| Song planner, 1.7B (turbo workflow; optional swap in the base one) | `qwen_1.7b_ace15.safetensors` | `text_encoders/` | 3.71 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/text_encoders/qwen_1.7b_ace15.safetensors) | turbo JSON |
| Diffusion model (XL turbo, bf16) | `acestep_v1.5_xl_turbo_bf16.safetensors` | `diffusion_models/` | 9.97 GB | [Comfy-Org/ACE-Step-1.5](https://huggingface.co/Comfy-Org/ACE-Step-1.5/resolve/main/split_files/diffusion_models/acestep_v1.5_xl_turbo_bf16.safetensors) | turbo JSON, SHA-256 matched 2026-11-24 |

**What the workflows need:**
- Base (v1.0.0): the first four files, about 19.9 GB.
- XL turbo 12 GB (v1.1.0): `acestep_v1.5_xl_turbo_bf16`, `qwen_0.6b_ace15`, `qwen_1.7b_ace15` and `ace_1.5_vae`, about 15.2 GB.

- These are the files the built-in ComfyUI template loads. The template's own links point at `Comfy-Org/ace_step_1.5_ComfyUI_files`, which Hugging Face redirects to `Comfy-Org/ACE-Step-1.5`.
- That repo has no fp8, int8 or GGUF version of the XL model (checked 2026-11-22). Setting the loader's `weight_dtype` to `fp8_e4m3fn` was tried once without a VRAM limit: 60 s instead of 56 s, and not the same waveform as the default (signal-to-noise 5 dB), so the loader stays on `default`.
- The 1.7B song planner goes in the second slot of the text encoder loader in place of the 4B file. It was run once, earlier the same day, without a VRAM limit: 48 s instead of 56 s for the default song. That download was not hash-checked in this session.

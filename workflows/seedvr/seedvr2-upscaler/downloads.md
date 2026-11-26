# Downloads - SeedVR2 Upscaler v1.0.0

Verified from the workflow JSON files. File names, sizes and SHA-256 checked against Hugging Face on 2026-11-26 (local SHA-256 equal to the Hub listing).

| Role | Filename | Folder | Size | Source | Used by | Verified? |
|---|---|---|---|---|---|---|
| Diffusion (7B) | `seedvr2_7b_int8_convrot.safetensors` | `diffusion_models/` | 8.3 GB | [Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_7b_int8_convrot.safetensors) | picture | JSON |
| Diffusion (3B) | `seedvr2_3b_int8_convrot.safetensors` | `diffusion_models/` | 3.5 GB | [Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) | video | JSON |
| VAE | `seedvr2_ema_vae_fp16.safetensors` | `vae/` | 0.5 GB | [Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) | both | JSON |

Total: 12.3 GB for both workflows, 8.8 GB for pictures only, 4.0 GB for video only.

Licence: Apache-2.0 (Comfy-Org/SeedVR2 repack of ByteDance-Seed/SeedVR2-3B and SeedVR2-7B, both Apache-2.0).

**Other files in the same repo (not in the JSON, not run here unless stated):**
- `seedvr2_7b_sharp_int8_convrot.safetensors` (8.3 GB): the "sharp" 7B variant. Not run.
- fp16, fp8_e4m3fn, mxfp8 and nvfp4 versions of 3B, 7B and 7B sharp. Not run.
- `vae/ema_vae_fp16.safetensors`: the same VAE under another name (same SHA-256).

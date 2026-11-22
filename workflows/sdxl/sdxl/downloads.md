# Downloads - SDXL v1.0.0

Verified from the workflow JSON file. The file was downloaded on 2026-11-22 and its SHA-256 and size matched the Hugging Face listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Checkpoint (model + text encoders + VAE) | `sd_xl_base_1.0.safetensors` | `checkpoints/` | 6.94 GB | [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) | JSON |

**What the workflow needs:** this one file, 6.94 GB (6,938,078,334 bytes). The repo is not gated; no login is needed.

SHA-256: `31e35c80fc4829d14f90153f4c74cd59c90b779f6afe05a74cd6120b893f7e5b`

The workflow loads the authors' checkpoint, the same file as the built-in template. A search of the Comfy-Org account on Hugging Face for "xl" returned no repos (2026-11-22), so no repackaged, fp8 or int8 file was used. The same repo also holds `sd_xl_base_1.0_0.9vae.safetensors` (same size, older VAE); it was not tested.

The SDXL refiner is not used and not needed.

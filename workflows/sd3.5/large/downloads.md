# Downloads - Stable Diffusion 3.5 Large v1.0.0

Verified from the workflow JSON file. The file was downloaded on 2026-11-24 and its SHA-256 and size matched the Hugging Face listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Checkpoint (model + CLIP-L + CLIP-G + T5-XXL fp8 + VAE) | `sd3.5_large_fp8_scaled.safetensors` | `checkpoints/` | 14.93 GB | [Comfy-Org/stable-diffusion-3.5](https://huggingface.co/Comfy-Org/stable-diffusion-3.5/resolve/main/sd3.5_large_fp8_scaled.safetensors) | JSON |

**What the workflow needs:** this one file, 14.93 GB (14,934,922,866 bytes). The Comfy-Org repo is not gated; no login is needed.

SHA-256: `5ad94d6f951556b1ab6b75930fd4effbafaf3130fe9df440e7f2d05a220dd1be`

The template links the old repo name `Comfy-Org/stable-diffusion-3.5-fp8`; Hugging Face now redirects it (HTTP 307) to `Comfy-Org/stable-diffusion-3.5`, which is the link used here.

The same repo also holds `sd3.5_medium_incl_clips_t5xxlfp8scaled.safetensors` (11.64 GB) and separate text encoder files (`clip_g`, `clip_l`, `t5xxl_*`). They are not used by this workflow and were not tested. The authors' full-precision files (`stabilityai/stable-diffusion-3.5-large`, 16.46 GB without text encoders) are gated behind a licence click-through and were not tested.

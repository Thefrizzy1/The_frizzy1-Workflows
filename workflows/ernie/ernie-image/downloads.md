# Downloads - ERNIE-Image Turbo v1.0.0

Verified from the workflow JSON file. The files were downloaded on 2026-11-24 and their SHA-256 and size matched the Hugging Face listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (bf16) | `ernie-image-turbo.safetensors` | `diffusion_models/` | 16.07 GB | [Comfy-Org/ERNIE-Image](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/diffusion_models/ernie-image-turbo.safetensors) | JSON |
| Text encoder (Ministral 3B) | `ministral-3-3b.safetensors` | `text_encoders/` | 7.72 GB | [Comfy-Org/ERNIE-Image](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ministral-3-3b.safetensors) | JSON |
| Prompt enhancer LLM | `ernie-image-prompt-enhancer.safetensors` | `text_encoders/` | 6.88 GB | [Comfy-Org/ERNIE-Image](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ernie-image-prompt-enhancer.safetensors) | JSON |
| VAE (Flux.2) | `flux2-vae.safetensors` | `vae/` | 0.34 GB | [Comfy-Org/ERNIE-Image](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/vae/flux2-vae.safetensors) | JSON |

**What the workflow needs:** all four files, 31.0 GB together (16,067,025,480 + 7,717,637,511 + 6,877,439,999 + 336,213,556 bytes). The prompt enhancer file is needed even with the enhancer switched off, because ComfyUI checks every loader before a run. The repo is not gated; no login is needed.

SHA-256:
- `ernie-image-turbo.safetensors`: `741a4cc0467d4b9f04490d7faa9a5869ff4aa97eb2914927a1df9abb070e8e52`
- `ministral-3-3b.safetensors`: `49a750a128863854eac7d85e1a277a7b44bf6ec3646405b84686dfeeca3708ca`
- `ernie-image-prompt-enhancer.safetensors`: `e823e002626858be92e6600609f72fde33c5f21d3c6574721ce9f41bf1c50771`
- `flux2-vae.safetensors`: `d64f3a68e1cc4f9f4e29b6e0da38a0204fe9a49f2d4053f0ec1fa1ca02f9c4b5`

The Comfy-Org repo holds only bf16 files (listing of 2026-11-24): the Turbo model above, the 50-step base model `ernie-image.safetensors` (same size, not used here), the two text encoders and the VAE.

## Optional: faster fp8 model (community)

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (fp8 e4m3) | `ernie-image-turbo-fp8.safetensors` | `diffusion_models/` | 8.22 GB | [Bedovyy/ERNIE-Image-Quantized](https://huggingface.co/Bedovyy/ERNIE-Image-Quantized/resolve/main/ernie-image-turbo-fp8.safetensors) | Run on the two samples |

Not in the workflow by default; pick it in the "ERNIE-Image Turbo model" loader. SHA-256 `9cc5c947f934cb1948e1afd9bdda3e9e8efac98306a3e0ca9feb0cb3b2cc93a5` (matched the listing). In a 12 GiB budget it took 24 s and 10 s instead of 29 s and 14 s for the two samples, with the same composition and text and small differences in detail. It is a community quantisation (Apache 2.0 tag), not a Comfy-Org file. The same repo's `int8rowwise` file needs a custom node and was not used.

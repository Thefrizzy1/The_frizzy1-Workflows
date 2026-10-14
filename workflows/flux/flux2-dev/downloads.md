# Downloads — Flux.2 Dev GGUF v1.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `flux2-dev-Q5_K_M.gguf` | Flux.2 Dev GGUF (search QuantStack / city96 for `FLUX.2-dev-GGUF`) | JSON |
| Text encoder | `mistral_3_small_flux2_fp4_mixed.safetensors` | Comfy-Org Flux.2 repackaged | JSON |
| VAE | `flux2-vae.safetensors` | Comfy-Org Flux.2 repackaged | JSON |

> Exact source repos to be confirmed against the model card — filenames themselves are verified from the JSON.

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `flux2-dev-Q5_K_M.gguf` | [download](https://huggingface.co/city96/FLUX.2-dev-gguf/resolve/main/flux2-dev-Q5_K_M.gguf) | Pick your quant from the repo. |
| required | `text_encoders/` | `mistral_3_small_flux2_fp4_mixed.safetensors` | [download](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_fp4_mixed.safetensors) | 12.3 GB |
| required | `vae/` | `flux2-vae.safetensors` | [download](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) | 0.3 GB |

**Custom node packs this workflow uses:** [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

One command: `python scripts/frizzy.py doctor flux/flux2-dev` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

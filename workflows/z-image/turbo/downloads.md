# Downloads — Z-Image Turbo GGUF v1.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `z-image-turbo-q8_0.gguf` | Z-Image Turbo GGUF (search HF for `Z-Image-Turbo-GGUF`) | JSON |
| Text encoder | `qwen_3_4b.safetensors` | Qwen-3 4B (ComfyUI text encoder) | JSON |
| VAE | `ae.safetensors` | [ffxvs/vae-flux](https://huggingface.co/ffxvs/vae-flux/blob/main/ae.safetensors) | JSON |

> Source repos to be confirmed against the model card — filenames themselves are verified from the JSON.

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `vae/` | `ae.safetensors` | [download](https://huggingface.co/ffxvs/vae-flux/resolve/main/ae.safetensors) |  |
| required | `diffusion_models/` | `z-image-turbo-q8_0.gguf` | [download](https://huggingface.co/unsloth/Z-Image-Turbo-GGUF/resolve/main/z-image-turbo-Q8_0.gguf) | Downloads unsloth/Z-Image-Turbo-GGUF z-image-turbo-Q8_0.gguf and saves it under the name the workflow loads. 7.2 GB |
| required | `text_encoders/` | `qwen_3_4b.safetensors` | [download](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) | 8.0 GB |

**Custom node packs this workflow uses:** [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

One command: `python scripts/frizzy.py doctor z-image/turbo` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

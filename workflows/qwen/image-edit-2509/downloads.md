# Downloads — Qwen Image & Edit 2509 GGUF v1.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `Qwen_Image-Q8_0.gguf` | [QuantStack/Qwen-Image-GGUF](https://huggingface.co/QuantStack/Qwen-Image-GGUF) · [Edit-2509](https://huggingface.co/QuantStack/Qwen-Image-Edit-2509-GGUF) | JSON |
| Speed LoRA | `Qwen-Image-Lightning-8steps-V2.0.safetensors` | [lightx2v/Qwen-Image-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Lightning) (4-step also available) | JSON |
| Text encoder | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| VAE | `qwen_image_vae.safetensors` | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `Qwen_Image-Q8_0.gguf` | [download](https://huggingface.co/QuantStack/Qwen-Image-GGUF/resolve/main/Qwen_Image-Q8_0.gguf) | Generation. For editing use QuantStack/Qwen-Image-Edit-2509-GGUF. |
| optional | `loras/` | `Qwen-Image-Lightning-8steps-V2.0.safetensors` | [download](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V2.0.safetensors) | Speed LoRA. |
| required | `text_encoders/` | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | [download](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |  |
| required | `vae/` | `qwen_image_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |  |

**Custom node packs this workflow uses:** [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

One command: `python scripts/frizzy.py doctor qwen/image-edit-2509` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

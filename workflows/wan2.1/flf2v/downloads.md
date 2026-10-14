# Downloads — Wan 2.1 FLF2V v2.0.0

Verified from the FLF2V workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `wan2.1-flf2v-720p-14b-q2_k.gguf` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | JSON |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | JSON |
| VAE | `wan_2.1_vae.safetensors` | Comfy-Org repackaged | JSON |
| CLIP vision | `clip_vision_h_fp8_e4m3fn.safetensors` | Comfy-Org repackaged | JSON |
| Frame interp / upscale | `rife49.pth` · `RealESRGAN_x4.pth` | RIFE · RealESRGAN | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `wan2.1-flf2v-720p-14b-q2_k.gguf` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/wan2.1-flf2v-720p-14b-q2_k.gguf) | Pick your quant from the repo. |
| required | `vae/` | `wan_2.1_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |  |
| required | `text_encoders/` | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | 6.7 GB |
| required | `clip_vision/` | `clip_vision_h_fp8_e4m3fn.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/clip_vision_h_fp8_e4m3fn.safetensors) | 0.6 GB |
| required | `upscale_models/` | `RealESRGAN_x4.pth` | [download](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | Upscaler, 0.07 GB |

**Custom node packs this workflow uses:** [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

**Downloaded by the node packs themselves on first run:** `rife49.pth` (ComfyUI-Frame-Interpolation).

One command: `python scripts/frizzy.py doctor wan2.1/flf2v` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

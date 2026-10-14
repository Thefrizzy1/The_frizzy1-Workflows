# Downloads — Wan 2.1 GGUF Low-VRAM v2.0.0

All filenames read directly from the workflow JSONs (verified). Diffusion models → `diffusion_models/`.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion (I2V 14B) | `wan2.1-i2v-14b-480p-Q3_K_M.gguf` | [city96/Wan2.1-I2V-14B-480P-gguf](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf) | JSON |
| Diffusion (T2V 1.3B) | `Wan2.1-T2V-1.3B-F16.gguf` | [calcuis/wan-1.3b-gguf](https://huggingface.co/calcuis/wan-1.3b-gguf) | JSON |
| Diffusion (FLF 14B) | `wan2.1-flf2v-720p-14b-q2_k.gguf` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | JSON |
| Diffusion (VACE 1.3B) | `wan2.1-vace-1.3b-f16.gguf` | [QuantStack/Wan2.1_14B_VACE-GGUF](https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF) | JSON |
| Diffusion (Fun Control) | `wan2.1-fun-control-1.3b-q8_0.gguf` | [city96/Wan2.1-Fun-14B-Control-gguf](https://huggingface.co/city96/Wan2.1-Fun-14B-Control-gguf) | JSON |
| Diffusion (Fun Camera) | `Wan2.1-Fun-V1.1-14B-Control-Camera-Q3_K_M.gguf` | [QuantStack/…Camera-GGUF](https://huggingface.co/QuantStack/Wan2.1-Fun-V1.1-14B-Control-Camera-GGUF) | JSON |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | JSON |
| VAE | `wan_2.1_vae.safetensors` (+ `_fp8_e4m3fn`) | Comfy-Org repackaged | JSON |
| CLIP vision | `clip_vision_h_fp8_e4m3fn.safetensors` | Comfy-Org repackaged | JSON |
| Frame interp | `rife49.pth` | RIFE (ComfyUI-Frame-Interpolation) | JSON |
| Upscale | `RealESRGAN_x4.pth` | RealESRGAN | JSON |
| Depth (Fun) | `depth_anything_vitl14.pth` | Depth-Anything | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `wan2.1-i2v-14b-480p-Q3_K_M.gguf` | [download](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf/resolve/main/wan2.1-i2v-14b-480p-Q3_K_M.gguf) | I2V. Pick your quant from the repo. |
| optional | `diffusion_models/` | `Wan2.1-T2V-1.3B-F16.gguf` | [download](https://huggingface.co/calcuis/wan-1.3b-gguf/resolve/main/wan2.1_t2v_1.3b-f16.gguf) | T2V 1.3B, the lightest option. Downloads calcuis' wan2.1_t2v_1.3b-f16.gguf (renamed on the repo) and saves it under the name the workflow loads. 2.9 GB |
| required | `vae/` | `wan_2.1_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |  |
| required | `text_encoders/` | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | 6.7 GB |
| required | `clip_vision/` | `clip_vision_h_fp8_e4m3fn.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/clip_vision_h_fp8_e4m3fn.safetensors) | 0.6 GB |
| required | `upscale_models/` | `RealESRGAN_x4.pth` | [download](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | Upscaler, 0.07 GB |
| required | `vae/` | `wan_2.1_vae_fp8_e4m3fn.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/wan_2.1_vae_fp8_e4m3fn.safetensors) | 0.1 GB |

**Custom node packs this workflow uses:** [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

**Downloaded by the node packs themselves on first run:** `rife49.pth` (ComfyUI-Frame-Interpolation).

One command: `python scripts/frizzy.py doctor wan2.1/gguf-lowvram` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

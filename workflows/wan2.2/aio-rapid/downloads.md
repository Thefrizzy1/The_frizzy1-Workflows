# Downloads — Wan 2.2 AIO Rapid v1.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion (single AIO) | `wan2.2-rapid-mega-aio-v12-Q4_K.gguf` | Phr00t "Wan2.2 Rapid Mega AIO" (search HF/CivitAI for the mega-aio GGUF) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files) | JSON |
| VAE | `wan_2.1_vae.safetensors` | Comfy-Org repackaged | JSON |

> The single-file design bakes the experts + LoRA into one GGUF, so no separate high/low-noise or lightx2v downloads are needed.

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |  |
| required | `vae/` | `wan_2.1_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |  |
| required | `diffusion_models/` | `wan2.2-rapid-mega-aio-v12-Q4_K.gguf` | [download](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/Mega-v12/wan2.2-rapid-mega-aio-v12-Q4_K.gguf) | Single all-in-one file. 11.6 GB |

**Custom node packs this workflow uses:** [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler).

One command: `python scripts/frizzy.py doctor wan2.2/aio-rapid` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

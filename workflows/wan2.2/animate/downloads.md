# Downloads — Wan 2.2 Animate v1.2.0

> **Newer:** [Wan Animate Ultimate](../animate-ultimate) rebuilds this with native nodes (only ComfyUI-GGUF needed), adds Wan Animate 2 and a face video that makes the mouth move. Tested on an RTX 3060.

All filenames were read directly from the workflow `.json` (verified). Place each file in the folder shown.

| Role | Filename (loader expects this) | Folder | Source | Verified? |
|---|---|---|---|---|
| Diffusion | `Wan2.2-Animate-14B-Q8_0.gguf` (or `Q5_K_S`, `Q4_K_M`) | `diffusion_models/` | [Q8_0](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q8_0.gguf) · [Q5_K_S](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q5_K_S.gguf) · [Q4_K_M](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q4_K_M.gguf) | JSON |
| Relight LoRA | `WanAnimate_relight_lora_fp16.safetensors` | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) | JSON |
| Speed LoRA | JSON loads `high_noise_model(wan2.2light2xvI2v_v2.2).safetensors` - a renamed file with no public source. Use [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) and pick it in the LoRA loader (tested in [animate-ultimate](../animate-ultimate)) | `loras/` | fixed 2026-09-29 |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | JSON |
| CLIP vision | `clip_vision_h.safetensors` | `clip_vision/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) | JSON |
| VAE | JSON loads `Wan2.1_VAE.pth`; the same VAE as [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (pick it in the VAE loader) | `vae/` | fixed 2026-09-29 |
| Frame interp | `rife49.pth` | `rife/` (ComfyUI-Frame-Interpolation) | RIFE | JSON |

## Quant → VRAM (diffusion)

| Quant | Approx VRAM |
|---|---|
| Q4_K_M | not measured |
| Q5_K_S | not measured |
| Q6_K | not measured |

> The `Q8_0` variant appears in the GGUF workflow, `Q5_K_S` in the non-GGUF variant — both are valid; pick by VRAM.


Custom packs this v1.2.0 JSON also uses (not listed before): ComfyUI-Custom-Scripts (`MathExpression|pysssss`), ComfyUI-Frame-Interpolation (`RIFE VFI`).

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `Wan2.2-Animate-14B-Q8_0.gguf` | [download](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q8_0.gguf) | 12GB target. Use Q4_K_M for 4GB. |
| required | `loras/` | `WanAnimate_relight_lora_fp16.safetensors` | [download](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) |  |
| optional | `loras/` | `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | [download](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) | Speed LoRA. |
| required | `text_encoders/` | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |  |
| required | `clip_vision/` | `clip_vision_h.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |  |
| required | `vae/` | `Wan2.1_VAE.pth` | [download](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B/resolve/main/Wan2.1_VAE.pth) | 0.5 GB |

**Custom node packs this workflow uses:** [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [execution-inversion-demo-comfyui](https://github.com/BadCafeCode/execution-inversion-demo-comfyui), [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials), [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

**Downloaded by the node packs themselves on first run:** `rife49.pth` (ComfyUI-Frame-Interpolation), `yolox_l.onnx` + `dw-ll_ucoco_384_bs5.torchscript.pt` (comfyui_controlnet_aux, DWPose), `sam2_hiera_base_plus.safetensors` (ComfyUI-segment-anything-2).

One command: `python scripts/frizzy.py doctor wan2.2/animate` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

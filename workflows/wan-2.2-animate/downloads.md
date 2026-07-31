# Downloads — Wan 2.2 Animate v1.2.0

All filenames were read directly from the workflow `.json` (verified). Place each file in the folder shown.

| Role | Filename (loader expects this) | Folder | Source | Verified? |
|---|---|---|---|---|
| Diffusion | `Wan2.2-Animate-14B-Q8_0.gguf` (or `Q5_K_S`, `Q4_K_M`) | `diffusion_models/` | [QuantStack/Wan2.2-Animate-14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF) | JSON |
| Relight LoRA | `WanAnimate_relight_lora_fp16.safetensors` | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) | JSON |
| Speed LoRA | `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | JSON |
| CLIP vision | `clip_vision_h.safetensors` | `clip_vision/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) | JSON |
| VAE | `wan_2.1_vae.safetensors` | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | JSON |
| Frame interp | `rife49.pth` | `rife/` (ComfyUI-Frame-Interpolation) | RIFE | JSON |

## Quant → VRAM (diffusion)

| Quant | Approx VRAM |
|---|---|
| Q4_K_M | ~10–12 GB |
| Q5_K_S | ~14–16 GB |
| Q6_K | ~20 GB+ |

> The `Q8_0` variant appears in the GGUF workflow, `Q5_K_S` in the non-GGUF variant — both are valid; pick by VRAM.

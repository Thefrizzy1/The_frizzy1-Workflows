# Downloads — Wan 2.2 GGUF Low-VRAM v1.0.0

Verified from the workflow JSONs. **14B paths need BOTH the high-noise and low-noise GGUF.**

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion T2V 14B (high) | `wan2.2_t2v_high_noise_14B_Q2_K.gguf` | [QuantStack/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF) | JSON |
| Diffusion T2V 14B (low) | `wan2.2_t2v_low_noise_14B_Q2_K.gguf` | QuantStack (above) | JSON |
| Diffusion I2V 14B (high/low) | `Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf` · `…-LowNoise-Q2_K.gguf` | [bullerwins/Wan2.2-I2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF) | JSON |
| Diffusion TI2V 5B | `Wan2.2-TI2V-5B-Q5_1.gguf` | [QuantStack/Wan2.2-TI2V-5B-GGUF](https://huggingface.co/QuantStack/Wan2.2-TI2V-5B-GGUF) | JSON |
| Speed LoRA (T2V) | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | JSON |
| Speed LoRA (I2V) | `Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_fixed.safetensors` | Kijai/WanVideo_comfy | JSON |
| VAE (5B) | `Wan2.2_VAE.safetensors` | Comfy-Org Wan 2.2 repackaged | JSON |
| VAE (14B) | `wan_2.1_vae.safetensors` | Comfy-Org repackaged | JSON |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files) | JSON |
| Frame interp / upscale | `rife49.pth` · `RealESRGAN_x2.pth` | RIFE · RealESRGAN | JSON |

> ⚠️ **VAE trap:** 5B uses `Wan2.2_VAE`; 14B uses `wan_2.1_vae`. Swapping them = black/garbled frames.

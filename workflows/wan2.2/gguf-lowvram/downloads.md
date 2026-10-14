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

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| optional | `diffusion_models/` | `Wan2.2-TI2V-5B-Q5_1.gguf` | [download](https://huggingface.co/QuantStack/Wan2.2-TI2V-5B-GGUF/resolve/main/Wan2.2-TI2V-5B-Q5_1.gguf) | TI2V-5B single-file alternative (neither .json loads it; swap it into the loader). |
| optional | `loras/` | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors` | [download](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors) | Speed LoRA for T2V. |
| required | `vae/` | `wan_2.1_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |  |
| optional | `vae/` | `wan2.2_vae.safetensors` | [download](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors) | VAE for the TI2V-5B alternative only. |
| required | `diffusion_models/` | `wan2.2_t2v_high_noise_14B_Q2_K.gguf` | [download](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF/resolve/main/wan2.2_t2v_high_noise_14B_Q2_K.gguf) | T2V 14B high-noise expert (you need both). 5.3 GB |
| required | `diffusion_models/` | `wan2.2_t2v_low_noise_14B_Q2_K.gguf` | [download](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF/resolve/main/wan2.2_t2v_low_noise_14B_Q2_K.gguf) | T2V 14B low-noise expert. 5.3 GB |
| required | `diffusion_models/` | `Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf` | [download](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/HighNoise/Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf) | I2V 14B high-noise expert. 5.3 GB |
| required | `diffusion_models/` | `Wan2.2-I2V-A14B-LowNoise-Q2_K.gguf` | [download](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/LowNoise/Wan2.2-I2V-A14B-LowNoise-Q2_K.gguf) | I2V 14B low-noise expert. 5.3 GB |
| required | `text_encoders/` | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [download](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | 6.7 GB |
| required | `upscale_models/` | `RealESRGAN_x2.pth` | [download](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x2.pth) | Upscaler, 0.07 GB |
| optional | `loras/` | `Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_fixed.safetensors` | [page](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (by hand) | I2V speed LoRA: this name is no longer published. Use Kijai's lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors and pick it in the LoRA loader. |

**Custom node packs this workflow uses:** [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation), [ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox).

**Downloaded by the node packs themselves on first run:** `rife49.pth` (ComfyUI-Frame-Interpolation).

One command: `python scripts/frizzy.py doctor wan2.2/gguf-lowvram` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

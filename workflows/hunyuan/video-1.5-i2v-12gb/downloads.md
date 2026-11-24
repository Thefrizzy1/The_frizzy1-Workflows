# Downloads - Hunyuan Video 1.5 I2V · 12 GB v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-24 and its size and SHA-256 matched Hugging Face.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Video model, 480p image-to-video, step-distilled (fp8 scaled) | `hunyuanvideo1.5_480p_i2v_step_distilled_fp8_scaled.safetensors` | `diffusion_models/` | 8.34 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_480p_i2v_step_distilled_fp8_scaled.safetensors) | JSON |
| Text encoder 1 (Qwen 2.5 VL 7B, fp8 scaled) | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.38 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| Text encoder 2 (ByT5 small) | `byt5_small_glyphxl_fp16.safetensors` | `text_encoders/` | 0.44 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) | JSON |
| VAE | `hunyuanvideo15_vae_fp16.safetensors` | `vae/` | 2.52 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) | JSON |
| Picture encoder (SigCLIP vision 384) | `sigclip_vision_patch14_384.safetensors` | `clip_vision/` | 0.86 GB | [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) | JSON |
| Group 6 only: 480p → 720p super-resolution model, step-distilled (fp8 scaled) | `hunyuanvideo1.5_720p_sr_distilled_fp8_scaled.safetensors` | `diffusion_models/` | 8.34 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_sr_distilled_fp8_scaled.safetensors) | JSON (bypassed group) |
| Group 6 only: 720p latent upsampler | `hunyuanvideo15_latent_upsampler_720p.safetensors` | `latent_upscale_models/` | 0.09 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/latent_upscale_models/hunyuanvideo15_latent_upsampler_720p.safetensors) | JSON (bypassed group) |

**What the workflow needs:** the first five files, about 21.5 GB. Group 6 (upscale to 720p) is bypassed in the shipped file, and a bypassed node is not sent to ComfyUI, so its two files (8.43 GB) are only needed once you switch the group on.

- The Comfy-Org repo listing (checked 2026-11-24, saved with the run) has the 480p I2V step-distilled model as fp16 (16.7 GB) and fp8 scaled (8.34 GB). There is no GGUF in that repo, and core ComfyUI has no GGUF loader. The fp16 file was not run.
- The built-in template loads `hunyuanvideo1.5_720p_i2v_fp16.safetensors` (16.7 GB, 20 steps, CFG 6). It was not run here. `hunyuanvideo1.5_720p_i2v_cfg_distilled_fp8_scaled.safetensors` (8.33 GB) was downloaded but not run: the authors say the cfg-distilled models need 50 steps, which at 720p would be far slower than this workflow on a 12 GB card.
- The template's 1080p upscale files (`hunyuanvideo1.5_1080p_sr_distilled_*`, `hunyuanvideo15_latent_upsampler_1080p.safetensors`) are not used: this workflow upscales 480p to 720p, the pairing the authors list for the 480p step-distilled model.

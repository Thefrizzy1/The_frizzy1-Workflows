# Downloads - InfiniteTalk Talking Video v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-24 and its SHA-256 and size matched the Hugging Face listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (Wan 2.1 I2V 14B 480p, fp8 scaled) | `wan2.1_i2v_480p_14B_fp8_scaled.safetensors` | `diffusion_models/` | 16.4 GB | [Comfy-Org/Wan-2.1](https://huggingface.co/Comfy-Org/Wan-2.1/resolve/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_fp8_scaled.safetensors) | JSON |
| Speed LoRA (lightx2v, 6 steps, CFG 1) | `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras/` | 0.74 GB | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) | JSON |
| InfiniteTalk patch (single speaker) | `wan2.1_infiniteTalk_single_fp16.safetensors` | `model_patches/` | 5.13 GB | [Comfy-Org/Wan-2.1](https://huggingface.co/Comfy-Org/Wan-2.1/resolve/main/split_files/model_patches/wan2.1_infiniteTalk_single_fp16.safetensors) | JSON |
| Speech encoder (wav2vec2) | `wav2vec2-chinese-base_fp16.safetensors` | `audio_encoders/` | 0.19 GB | [Kijai/wav2vec2_safetensors](https://huggingface.co/Kijai/wav2vec2_safetensors/resolve/main/wav2vec2-chinese-base_fp16.safetensors) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders/` | 6.74 GB | [Comfy-Org/Wan-2.1](https://huggingface.co/Comfy-Org/Wan-2.1/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | JSON |
| VAE | `wan_2.1_vae.safetensors` | `vae/` | 0.25 GB | [Comfy-Org/Wan-2.1](https://huggingface.co/Comfy-Org/Wan-2.1/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | JSON |

**What the workflow needs:** all six files, about 29.5 GB. The text encoder and the VAE are the usual Wan 2.1 / Wan 2.2 files; if you have them, the new download is about 22.5 GB.

- The Comfy-Org repo used to be called `Comfy-Org/Wan_2.1_ComfyUI_repackaged`; the old links now redirect to `Comfy-Org/Wan-2.1`.
- The built-in template loads Kijai's `Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors` and `Wan2_1_VAE_bf16.safetensors`. This workflow uses the Comfy-Org copies above and did not run the Kijai files.
- The Comfy-Org repo listing (checked 2026-11-24) has the I2V 14B 480p model as bf16 / fp16 (32.8 GB) and fp8 e4m3fn / fp8 scaled (16.4 GB). It has no int8 or GGUF copy of the diffusion model; core ComfyUI has no GGUF loader. The text encoder also comes as `umt5_xxl_int8_convrot.safetensors` (5.69 GB); not run here.
- `wan2.1_infiniteTalk_multi_fp16.safetensors` (two speakers, 5.12 GB) is for the template's two-speaker mode. This workflow does not use it.
- The speed LoRA and the speech encoder are not in a Comfy-Org repo; the links are Kijai's, the same files the template links.

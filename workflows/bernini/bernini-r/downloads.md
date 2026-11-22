# Downloads - Bernini-R Image Edit v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-22 and its SHA-256 matched Hugging Face.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model, high noise (int8 convrot) | `wan2.2_bernini_r_high_noise_int8_convrot.safetensors` | `diffusion_models/` | 14.5 GB | [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors) | JSON |
| Diffusion model, low noise (int8 convrot) | `wan2.2_bernini_r_low_noise_int8_convrot.safetensors` | `diffusion_models/` | 14.5 GB | [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders/` | 6.7 GB | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | JSON |
| VAE | `wan_2.1_vae.safetensors` | `vae/` | 0.25 GB | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | JSON |
| Turbo LoRA (lightx2v, loaded twice) | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` | `loras/` | 0.63 GB | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors) | JSON |
| Diffusion model, high noise, fp8 (optional swap) | `wan2.2_bernini_r_high_noise_fp8_scaled.safetensors` | `diffusion_models/` | 15.6 GB | [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_high_noise_fp8_scaled.safetensors) | not in the JSON |
| Diffusion model, low noise, fp8 (optional swap) | `wan2.2_bernini_r_low_noise_fp8_scaled.safetensors` | `diffusion_models/` | 15.6 GB | [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_low_noise_fp8_scaled.safetensors) | not in the JSON |

**What the workflow needs:** the first five files, about 36.7 GB. The text encoder and the VAE are the Wan 2.1 / Wan 2.2 files; if you have them, the new download is about 29.7 GB.

- The Turbo LoRA is required even with Turbo off: ComfyUI checks that every file named in the graph exists.
- The Comfy-Org repo listing (checked 2026-11-22) has the 14B pair as fp16 (28.6 GB each), fp8 scaled (15.6 GB), mxfp8 (15.0 GB) and int8 convrot (14.5 GB), plus a 1.3B fp16 file. There is no GGUF in that repo. The mxfp8, fp16 and 1.3B files were not run.
- The fp8 files are the ones the built-in template loads. Five Turbo runs with them (hat picture, two seeds; winter forest, three seeds) took 20 to 26 s and looked the same to the eye as the int8 results.
- The built-in template takes the VAE from Kijai (`Wan2_1_VAE_bf16.safetensors`); this workflow uses the Comfy-Org file and did not run the other one.
- The Comfy-Org Wan 2.2 lightx2v LoRA pair (`wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise` / `_low_noise`) was tried in place of the template's LoRA and is not used: it did not remove the mesh pattern described in the README.

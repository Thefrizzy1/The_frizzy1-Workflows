# Downloads - Kandinsky 5.0 Lite v1.0.0

Verified from the workflow JSON files. Every file was downloaded on 2026-11-21 and its SHA-256 matched Hugging Face.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion · text to image | `kandinsky5lite_t2i.safetensors` | `diffusion_models/` | 12.0 GB | [kandinskylab/Kandinsky-5.0-T2I-Lite](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite/resolve/main/model/kandinsky5lite_t2i.safetensors) | JSON |
| Diffusion · text to video (16-step, default) | `kandinsky5lite_t2v_distilled16steps_5s.safetensors` | `diffusion_models/` | 4.6 GB | [kandinskylab/Kandinsky-5.0-T2V-Lite-distilled16steps-5s](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2V-Lite-distilled16steps-5s/resolve/main/model/kandinsky5lite_t2v_distilled16steps_5s.safetensors) | JSON |
| Diffusion · image to video | `kandinsky5lite_i2v_5s.safetensors` | `diffusion_models/` | 4.6 GB | [kandinskylab/Kandinsky-5.0-I2V-Lite-5s](https://huggingface.co/kandinskylab/Kandinsky-5.0-I2V-Lite-5s/resolve/main/model/kandinsky5lite_i2v_5s.safetensors) | JSON |
| Text encoder (all three) | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.4 GB | [Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| Text encoder (all three) | `clip_l.safetensors` | `text_encoders/` | 0.25 GB | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) | JSON |
| VAE · text to image | `ae.safetensors` | `vae/` | 0.34 GB | [Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) | JSON |
| VAE · both video workflows | `hunyuan_video_vae_bf16.safetensors` | `vae/` | 0.49 GB | [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy/resolve/main/hunyuan_video_vae_bf16.safetensors) | JSON |
| Diffusion · text to video, best quality (optional swap) | `kandinsky5lite_t2v_sft_5s.safetensors` | `diffusion_models/` | 4.6 GB | [kandinskylab/Kandinsky-5.0-T2V-Lite-sft-5s](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2V-Lite-sft-5s/resolve/main/model/kandinsky5lite_t2v_sft_5s.safetensors) | not in the JSON |

**What each workflow needs:**
- Text to image: `kandinsky5lite_t2i` + both text encoders + `ae` = about 22 GB.
- Text to video: `kandinsky5lite_t2v_distilled16steps_5s` + both text encoders + `hunyuan_video_vae_bf16` = about 14.7 GB.
- Image to video: `kandinsky5lite_i2v_5s` + both text encoders + `hunyuan_video_vae_bf16` = about 14.7 GB.
- All three: about 31.6 GB (the text encoders are shared).

There are no Comfy-Org repackaged or quantised Kandinsky 5 files; these are the original bf16 files the built-in ComfyUI templates use.

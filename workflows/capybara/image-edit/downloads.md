# Downloads - Capybara Image Edit v1.0.0

Verified from the workflow JSON. Every required file was downloaded on 2026-11-24 and its SHA-256 and size matched the Hugging Face file listing.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model | `capybara_v0.1.safetensors` | `diffusion_models/` | 16.65 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/diffusion_models/capybara_v0.1.safetensors) | JSON |
| Text encoder 1 (fp8) | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.38 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| Text encoder 2 | `byt5_small_glyphxl_fp16.safetensors` | `text_encoders/` | 0.44 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) | JSON |
| VAE | `hunyuanvideo15_vae_fp16.safetensors` | `vae/` | 2.52 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) | JSON |
| Vision encoder | `sigclip_vision_patch14_384.safetensors` | `clip_vision/` | 0.86 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/clip_vision/sigclip_vision_patch14_384.safetensors) | JSON |
| Text encoder 1, bf16 (optional swap) | `qwen_2.5_vl_7b.safetensors` | `text_encoders/` | 16.58 GB | [Comfy-Org/Hunyuan-Video-1.5](https://huggingface.co/Comfy-Org/Hunyuan-Video-1.5/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b.safetensors) | not in the JSON, not run |

**What the workflow needs:** the first five files, about 29.9 GB. The VAE, vision encoder and text encoders are the Hunyuan Video 1.5 files, so if you have that model the new download is the 16.65 GB Capybara file.

- The built-in template links `Comfy-Org/HunyuanVideo_1.5_repackaged`; that repo now redirects to `Comfy-Org/Hunyuan-Video-1.5`, which the links above use.
- There is no fp8, int8 or GGUF copy of Capybara in the Comfy-Org repo (file listing checked 2026-11-24). The authors' fp8 option is a torchao switch in their own code and custom nodes, not a file.
- The fp8 text encoder is used instead of the template's bf16 one to save 7.2 GB of download. The two were not compared.

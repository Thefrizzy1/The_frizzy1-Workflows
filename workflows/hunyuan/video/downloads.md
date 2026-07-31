# Downloads — Hunyuan Video Low-VRAM v1.1.1

Verified from the workflow JSON (with the v1.1.1 diffusion-model correction noted).

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion (recommended) | `fast-hunyuan-video-t2v-720p-Q5_K_M.gguf` | [city96/FastHunyuan-gguf](https://huggingface.co/city96/FastHunyuan-gguf) | JSON (v1.1.1) |
| Diffusion (standard alt) | HunyuanVideo GGUF | [city96/HunyuanVideo-gguf](https://huggingface.co/city96/HunyuanVideo-gguf) | README |
| VAE | `kijai_hunyuan_video_vae_bf16.safetensors` | [calcuis/hunyuan-gguf](https://huggingface.co/calcuis/hunyuan-gguf) | JSON |
| Text encoder | `llava_llama3_fp8_scaled.safetensors` | calcuis/hunyuan-gguf | JSON |
| CLIP | `clip_l.safetensors` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | JSON |
| Upscale | `4x-AnimeSharp.pth` | 4x-AnimeSharp | JSON |

> ⚠️ The original file referenced `flux1-dev-Q5_K_S.gguf` in the diffusion loader — that was a leftover, not a
> real dependency. v1.1.1 points at the Fast Hunyuan GGUF instead.

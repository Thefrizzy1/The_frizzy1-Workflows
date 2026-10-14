# Downloads — LTX-2 GGUF v1.5.0

Verified from the workflow JSONs (I2V + T2V).

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `ltx-2-19b-distilled_Q4_K_M.gguf` (or `_Q8_0`) | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy/tree/main/diffusion_models) | JSON |
| Text encoder | `gemma_3_12B_it_fp8_e4m3fn.safetensors` | [Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders) | JSON |
| Connector | `ltx-2-19b-embeddings_connector_dev_bf16.safetensors` | Kijai/LTXV2_comfy | JSON |
| VAE (video) | `LTX2_video_vae_bf16.safetensors` | [Kijai/LTXV2_comfy/VAE](https://huggingface.co/Kijai/LTXV2_comfy/tree/main/VAE) | JSON |
| VAE (audio) | `LTX2_audio_vae_bf16.safetensors` | Kijai/LTXV2_comfy/VAE | JSON |
| Upscaler | `ltx-2-spatial-upscaler-x2-1.0.safetensors` | [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2) | JSON |
| Distill LoRA | `ltx-2-19b-distilled-lora-384.safetensors` | Kijai/LTXV2_comfy / Lightricks/LTX-2 | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `vae/` | `LTX2_video_vae_bf16.safetensors` | [download](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_video_vae_bf16.safetensors) |  |
| required | `vae/` | `LTX2_audio_vae_bf16.safetensors` | [download](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_audio_vae_bf16.safetensors) |  |
| required | `text_encoders/` | `ltx-2-19b-embeddings_connector_dev_bf16.safetensors` | [download](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/text_encoders/ltx-2-19b-embeddings_connector_dev_bf16.safetensors) |  |
| required | `diffusion_models/` | `ltx-2-19b-distilled_Q4_K_M.gguf` | [download](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/diffusion_models/ltx-2-19b-distilled_Q4_K_M.gguf) | The distilled model both .json files load. 12.7 GB |
| required | `text_encoders/` | `gemma_3_12B_it_fp8_e4m3fn.safetensors` | [download](https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/resolve/main/gemma_3_12B_it_fp8_e4m3fn.safetensors) | Gemma 3 12B text encoder. 13.2 GB |
| required | `latent_upscale_models/` | `ltx-2-spatial-upscaler-x2-1.0.safetensors` | [download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) | 2x latent upscaler. 1.0 GB |
| optional | `loras/` | `ltx-2-19b-distilled-lora-384.safetensors` | [download](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) | Its loader ships bypassed. 7.7 GB |

**Custom node packs this workflow uses:** [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

One command: `python scripts/frizzy.py doctor ltx/ltx2` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

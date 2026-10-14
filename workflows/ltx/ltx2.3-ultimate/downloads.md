# Downloads — LTX-2.3 Ultimate v3.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `ltx-2.3-22b-dev-Q5_K_M.gguf` (Q4_K_M for less VRAM) | [unsloth/LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF) | JSON |
| Text encoder | `gemma_3_12B_it_fp4_mixed.safetensors` | [Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders) | JSON |
| Text projection (required) | `ltx-2.3_text_projection_bf16.safetensors` | [Kijai/LTX2.3_comfy](https://huggingface.co/Kijai/LTX2.3_comfy) | JSON |
| VAE (video) | `ltx-2.3-22b-dev_video_vae.safetensors` | unsloth/LTX-2.3-GGUF | JSON |
| VAE (audio) | `ltx-2.3-22b-dev_audio_vae.safetensors` | unsloth/LTX-2.3-GGUF | JSON |
| Distill LoRA (required) | `ltx-2.3-22b-distilled-lora-384-1.1.safetensors` | Kijai/LTX2.3_comfy | JSON |
| ID LoRA | `ltx-2.3-id-lora-talkvid-3k.safetensors` | [AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K](https://huggingface.co/AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K) (`lora_weights.safetensors`, saved under this name) | JSON |
| Upscaler | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2) | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `diffusion_models/` | `ltx-2.3-22b-dev-Q5_K_M.gguf` | [download](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/ltx-2.3-22b-dev-Q5_K_M.gguf) | Use Q4_K_M for lower VRAM. |
| required | `vae/` | `ltx-2.3-22b-dev_video_vae.safetensors` | [download](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/vae/ltx-2.3-22b-dev_video_vae.safetensors) | 1.5 GB |
| required | `vae/` | `ltx-2.3-22b-dev_audio_vae.safetensors` | [download](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/vae/ltx-2.3-22b-dev_audio_vae.safetensors) | The audio VAE from this repo (static / no sound = wrong audio VAE). 0.4 GB |
| required | `loras/` | `ltx-2.3-22b-distilled-lora-384-1.1.safetensors` | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384-1.1.safetensors) | Distilled LoRA. 7.6 GB |
| required | `text_encoders/` | `ltx-2.3_text_projection_bf16.safetensors` | [download](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | Text projection connector. 2.3 GB |
| required | `text_encoders/` | `gemma_3_12B_it_fp4_mixed.safetensors` | [download](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) | Gemma 3 12B text encoder. 9.5 GB |
| required | `latent_upscale_models/` | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | [download](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | 2x latent upscaler. 1.0 GB |
| required | `loras/` | `ltx-2.3-id-lora-talkvid-3k.safetensors` | [download](https://huggingface.co/AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K/resolve/main/lora_weights.safetensors) | ID LoRA. Downloads AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K lora_weights.safetensors and saves it under the name the workflow loads. 1.2 GB |

**Custom node packs this workflow uses:** [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack), [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use).

One command: `python scripts/frizzy.py doctor ltx/ltx2.3-ultimate` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->

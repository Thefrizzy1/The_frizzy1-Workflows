# Downloads - FireRed Image Edit 1.1 v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-22 and its SHA-256 matched Hugging Face (the two optional files in an earlier session the same day).

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (int8 convrot, default) | `FireRed-ImageEdit-1.1_int8_convrot_WT.safetensors` | `diffusion_models/` | 20.6 GB | [TheWirableTortoise/FireRed-Image-Edit-v1.1-INT8-ConvRot](https://huggingface.co/TheWirableTortoise/FireRed-Image-Edit-v1.1-INT8-ConvRot/resolve/main/FireRed-ImageEdit-1.1_int8_convrot_WT.safetensors) | JSON |
| Text encoder | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders/` | 9.4 GB | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | JSON |
| VAE | `qwen_image_vae.safetensors` | `vae/` | 0.25 GB | [FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI/resolve/main/qwen_image_vae.safetensors) | JSON |
| Lightning LoRA (8 steps, the template's) | `FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors` | `loras/` | 0.85 GB | [FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI/resolve/main/FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors) | JSON |
| Diffusion model, fp8 (optional swap) | `firered_image_edit_1.1_fp8_scaled_e4m3fn.safetensors` | `diffusion_models/` | 20.4 GB | [drbaph/FireRed-Image-Edit-1.1_ComfyUI_Quants](https://huggingface.co/drbaph/FireRed-Image-Edit-1.1_ComfyUI_Quants/resolve/main/firered_image_edit_1.1_fp8_scaled_e4m3fn.safetensors) | not in the JSON |
| Diffusion model, authors' full file (optional swap) | `FireRed-Image-Edit-1.1-transformer.safetensors` | `diffusion_models/` | 40.9 GB | [FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI/resolve/main/FireRed-Image-Edit-1.1-transformer.safetensors) | not in the JSON |

**What the workflow needs:** the first four files, about 31.0 GB. The text encoder and the VAE are the Qwen Image files; if you have them, the new download is about 21.4 GB.

- The Lightning LoRA is required even with Lightning off: ComfyUI checks that every file named in the graph exists.
- There is no Comfy-Org repackaged FireRed file. The default is a community int8 convrot conversion by TheWirableTortoise; the fp8 file is a community conversion by drbaph. Both were compared with the authors' 40.9 GB file earlier the same day, with the newer 1.1 Lightning LoRA: on the flat-background hat picture (2 seeds) no difference was seen, and on the forest pictures all three files showed the same woven pattern, so the int8 file was not its cause. The two optional files were not run again with the LoRA this workflow loads.
- The built-in ComfyUI template loads the 40.9 GB file and the same Lightning LoRA as this workflow. The authors also publish `FireRed-Image-Edit-1.1-Lightning-8steps-v1.2.safetensors`; it is not used here because it put a woven pattern over foliage in the tests (see Known issues in the README).

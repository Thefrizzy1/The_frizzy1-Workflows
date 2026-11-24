# Downloads · Fibo 2.0 Edit + Text to Image · 12 GB

Every file name below was read from the two workflow `.json` files.

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| edit | `diffusion_models/` | [fibo2_edit_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_edit_turbo_int8_convrot.safetensors) | 8.41 GB |
| text to image | `diffusion_models/` | [fibo2_dev_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_dev_int8_convrot.safetensors) | 8.41 GB |
| both (same file as FLUX 3 Klein) | `text_encoders/` | [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | 4.86 GB |
| both: prompt enhancer | `text_encoders/` | [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | 9.35 GB |
| both (same file as FLUX 3 Klein) | `vae/` | [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/vae/flux2-vae.safetensors) | 0.34 GB |
| text to image, optional Turbo LoRA (node is bypassed) | `loras/` | [fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/loras/fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors) | 1.99 GB |

Edit only: 23.0 GB. Text to image only: 23.0 GB (+1.99 GB with the Turbo LoRA). Both: 31.4 GB (+1.99 GB).
The text-to-image files were checked against the Hugging Face SHA-256 on 2026-11-24.

_Edit tested on: RTX 3060 12 GB · ComfyUI 0.43.1 (v1.0.0). Text to image tested on: RTX PRO 4000 Blackwell 24 GB in a 10.5 GiB
VRAM budget · ComfyUI 0.45.3; not verified on a 12 GB card._

No custom nodes. Fibo 2.0: CC BY-NC 4.0 (non-commercial only). Qwen3-VL: Apache-2.0. Workflow: MIT.

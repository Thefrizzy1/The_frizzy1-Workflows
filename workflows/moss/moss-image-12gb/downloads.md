# Downloads · MOSS-Image · 12 GB

Every file name below was read from the workflow `.json`.

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| all | `diffusion_models/` | [moss_image_sft_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) | 5.41 GB |
| all | `text_encoders/` | [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) | 7.34 GB |
| all | `vae/` | [flux2-vae_small.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) | 0.25 GB |
| text to image (Turbo) | `loras/` | [moss_sft_4step_rank_64_lora_comfyui.safetensors](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA/resolve/main/moss_sft_4step_rank_64_lora_comfyui.safetensors) | 0.59 GB |
| edit | `loras/` | [moss_image_edit_lora_rank_64_bf16.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_edit_lora_rank_64_bf16.safetensors) | 0.30 GB |
| control | `loras/` | [moss_image_color_depth_control.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_color_depth_control.safetensors) | 0.31 GB |
| control | `geometry_estimation/` | [moge_3_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitl_fp16.safetensors) | 0.74 GB |

_Text to image v2.0.0 run on RTX 3060 12 GB, ComfyUI 0.45.3. The other files: v1.0.2 run on ComfyUI 0.45.3 (lab server, 24 GB card, 10 GiB budget). v1.0.1 tested on RTX 3060 12 GB, ComfyUI 0.43.1._

Every file was checked against the Hugging Face SHA-256 on 2026-11-24. `geometry_estimation/` is the folder ComfyUI uses for MoGe.

Total 15.0 GB (layout: the first three, 13.0 GB; text to image: the first four, 13.6 GB). No custom nodes: core ComfyUI **0.45.3**.
MOSS-Image: Apache-2.0. Turbo LoRA ([lvladikov/MOSS-SFT-Distill-4step-LoRA](https://huggingface.co/lvladikov/MOSS-SFT-Distill-4step-LoRA)): Apache-2.0. MoGe repackage: MIT. The edit and control LoRAs state no licence. Workflow: MIT.

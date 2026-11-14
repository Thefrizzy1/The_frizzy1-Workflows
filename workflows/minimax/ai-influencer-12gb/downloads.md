# Downloads — AI Influencer · 12 GB

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| workflows 1 + 2 | `diffusion_models/` | [minimax_h3_image_pruned_w4a8.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_w4a8.safetensors) | 12.5 GB |
| workflows 1 + 2 | `text_encoders/` | [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | 15.7 GB |
| workflows 1 + 2 | `vae/` | [minimax_h3_image_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) | 1.2 GB |
| video: Viggle Remake swap | `diffusion_models/` | [viggle_remake_swap_pruned_int8_convrot.safetensors](https://huggingface.co/Viggle/Viggle-Remake/resolve/main/int8/viggle_remake_swap_pruned_int8_convrot.safetensors) | 21.0 GB |
| video: Viggle Remake swap | `vae/` | [minimax_h3_video_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) | 5.2 GB |
| video: both | `vae/` | [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | 0.6 GB |
| video: MiniMax H3 image to video | `diffusion_models/` | [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | 21.0 GB |
| video: MiniMax H3 image to video | `vae/` | [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | 2.8 GB |
| video: MiniMax H3 image to video | `loras/` | [minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) | 2.0 GB |

**Workflows 1 and 2 need the first three files (29.4 GB).** Both use the same three. If you already run MiniMax H3 video, you have
the text encoder: it is the same file.

Everything marked *video* is optional, only for steps 6 and 7 of the guide:
- **Viggle Remake swap** (step 7) also needs Viggle's node pack: copy the folder `comfyui/ComfyUI-Viggle-Remake` from
  [Viggle/Viggle-Remake](https://huggingface.co/Viggle/Viggle-Remake/tree/main/comfyui) into `ComfyUI/custom_nodes/`. Their own
  workflow is `comfyui/workflows/remake_swap_ui.json` in the same repository. The file names for the video VAE are the ones my run
  used on the RTX 3060.
- **MiniMax H3 image to video** (step 6): the full list for every mode is in [h3-ultimate-12gb/downloads.md](../h3-ultimate-12gb/downloads.md).

Custom nodes: none for workflows 1 and 2 (core ComfyUI 0.45+).

## Workflow 4, its other modes (not used in the video)

MiniMax H3 Ultimate has more modes than image to video. These files are only for those modes; what each one is for is in
[h3-ultimate-12gb/downloads.md](../h3-ultimate-12gb/downloads.md).

| Folder | File (click = download) | Size / note |
|---|---|---|
| `diffusion_models/` | [minimax_h3_ref2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | 21.0 GB |
| `loras/` | [minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) | 2.0 GB |
| `model_patches/` | [minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/model_patches/minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors) | 2.3 GB |
| `checkpoints/` | [sdpose_wholebody_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) | 1.9 GB |
| `diffusion_models/` | [rt_detr_v4-x-hgnet_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) | 0.1 GB |

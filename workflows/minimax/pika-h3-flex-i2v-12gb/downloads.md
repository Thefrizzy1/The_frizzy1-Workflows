# Downloads - Pika H3 Flex I2V · 12 GB v1.0.0

Verified from the workflow JSON. Every file was downloaded on 2026-11-24 and its size and SHA-256 matched the Hugging Face listing (`?blobs=true`, saved with the run).

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Video+audio model, MiniMax H3 FL2VA (pruned, int8 convrot) | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `diffusion_models/` | 21.0 GB | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | JSON |
| Text encoder, Qwen3-VL 32B for H3 (NVFP4 AWQ) | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders/` | 15.7 GB | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | JSON |
| H3 video VAE (int8 convrot) | `minimax_h3_video_vae_int8_convrot.safetensors` | `vae/` | 2.8 GB | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | JSON |
| H3 audio VAE | `minimax_h3_audio_vae_fp32.safetensors` | `vae/` | 0.6 GB | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | JSON |
| Pika Flex FL2VA LoRA (official, 6 steps) | `pika_h3_flex_fl2va_v1_bf16.safetensors` | `loras/` | 2.0 GB | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/pika_h3_flex_fl2va_v1_bf16.safetensors) | JSON |
| Pika Flex Turbo LoRA, FL2VA 4-step, lite (rank 32) | `pika_h3_flex_turbo_4step_fl2va_lite_r32.safetensors` | `loras/` | 0.31 GB | [Pika-Labs/Pika-H3-Flex-Turbo-LoRA](https://huggingface.co/Pika-Labs/Pika-H3-Flex-Turbo-LoRA/resolve/main/pika_h3_flex_turbo_4step_fl2va_lite_r32.safetensors) | JSON |
| Group 7 only: RelayVSR x2 model (int8 convrot) | `relayvsr_x2_lightx2v_int8_convrot.safetensors` | `diffusion_models/` | 5.2 GB | [Comfy-Org/RelayVSR](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/diffusion_models/relayvsr_x2_lightx2v_int8_convrot.safetensors) | JSON (bypassed group) |
| Group 7 only: RelayVSR x2 Flash decoder | `relayvsr_flash_vae_x2_fp32.safetensors` | `vae/` | 0.13 GB | [Comfy-Org/RelayVSR](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/vae/relayvsr_flash_vae_x2_fp32.safetensors) | JSON (bypassed group) |

**What the workflow needs:** the first six files, 42.4 GB. The Turbo LoRA is needed even with Turbo off (ComfyUI checks every loader before it runs). Group 7 is bypassed in the shipped file, and a bypassed node is not sent to ComfyUI, so the two RelayVSR files (5.3 GB) are only needed once you switch it on.

- The Comfy-Org copy of the Flex LoRA (`pika_h3_flex_fl2va_v1_bf16`, the one the template loads) is not byte-identical to Pika's own `comfy/loras/pika_h3_flex_fl2va_comfy_bf16.safetensors` (128 bytes shorter, different SHA-256). Only the Comfy-Org file was run.
- The full Turbo file `pika_h3_flex_turbo_4step_fl2va.safetensors` (3.9 GB) was run too and gave nearly the same frames as the lite one (same seed, compared at 4.5 s); you can load it instead. The 8-step HD and 2-step draft Turbo files were not run.
- Other H3 FL2VA files in the Comfy-Org repo (checked 2026-11-24): fp8 scaled (21.0 GB), w6a8 (16.0 GB), pruned bf16 (40.2 GB). Not run here. Core ComfyUI has no GGUF loader.

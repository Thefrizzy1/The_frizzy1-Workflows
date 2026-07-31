# Downloads — Wan 2.2 AIO Rapid v1.0.0

Verified from the workflow JSON.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| Diffusion (single AIO) | `wan2.2-rapid-mega-aio-v12-Q4_K.gguf` | Phr00t "Wan2.2 Rapid Mega AIO" (search HF/CivitAI for the mega-aio GGUF) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files) | JSON |
| VAE | `wan_2.1_vae.safetensors` | Comfy-Org repackaged | JSON |

> The single-file design bakes the experts + LoRA into one GGUF, so no separate high/low-noise or lightx2v downloads are needed.

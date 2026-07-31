# Model Families

One place to understand every base model used across the workflows — what it is, which workflow runs it,
its recommended VRAM/quant, and where to download it. Filenames and downloads are in
[docs/DOWNLOADS.md](../docs/DOWNLOADS.md); the Wan generations are compared in detail in
[docs/WAN-LINEAGE.md](../docs/WAN-LINEAGE.md).

| Family | What it is | Tasks | Workflow(s) | Min VRAM |
|---|---|---|---|---|
| **Wan 2.1** | First-gen Wan video (1.3B/14B) | T2V·I2V·VACE·FLF·Fun | [wan-2.1-gguf-lowvram](../workflows/wan-2.1-gguf-lowvram) · [wan-2.1-flf2v](../workflows/wan-2.1-flf2v) | 4 GB |
| **Wan 2.2** | MoE dual-expert video (A14B) + TI2V-5B | T2V·I2V | [wan-2.2-gguf-lowvram](../workflows/wan-2.2-gguf-lowvram) · [wan-2.2-aio-rapid](../workflows/wan-2.2-aio-rapid) | 4 GB |
| **Wan 2.2 Animate** | Reference-driven character animation | V2V | [wan-2.2-animate](../workflows/wan-2.2-animate) | 4 GB |
| **Flux (Dev/Schnell/Kontext)** | High-quality image gen + editing | T2I·edit | [flux-kontext-gguf](../workflows/flux-kontext-gguf) | 4 GB |
| **Flux.2 Dev** | Newest Flux image model (Mistral encoder) | T2I | [flux2-dev-gguf](../workflows/flux2-dev-gguf) | 6 GB |
| **Qwen Image** | Image gen + editing (2509) | T2I·edit | [qwen-image-edit-2509](../workflows/qwen-image-edit-2509) | 4 GB |
| **Z-Image Turbo** | Fast few-step image gen (Qwen-3 encoder) | T2I | [z-image-turbo-gguf](../workflows/z-image-turbo-gguf) | 4 GB |
| **Hunyuan Video** | Tencent video model | T2V·I2V | [hunyuan-video-lowvram](../workflows/hunyuan-video-lowvram) | 4 GB |
| **LTXV-2 (19B)** | Fast audio-aware video | T2V·I2V·audio | [ltx2-gguf](../workflows/ltx2-gguf) | 4 GB |
| **LTXV-2.3 (22B)** | Newest LTX, FFLF + ID LoRA | T2V·I2V·FFLF·audio | [ltx2.3-ultimate](../workflows/ltx2.3-ultimate) | 12 GB |
| **MMAudio** | Audio generation / video-sync | audio | [ai-audio-maker](../workflows/ai-audio-maker) | low |

## Shared support models

Several workflows reuse the same encoders/VAEs — download once:

| File | Used by | Source |
|---|---|---|
| `t5xxl_um_fp8_e4m3fn_scaled.safetensors` (UMT5) | Wan 2.1, Wan 2.2 | Comfy-Org Wan repackaged |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | Wan 2.2 Animate, AIO Rapid | Comfy-Org Wan repackaged |
| `wan_2.1_vae.safetensors` | Wan 2.1, Wan 2.2 14B, Animate, AIO | Comfy-Org repackaged |
| `gemma_3_12B_it_*.safetensors` | LTX-2, LTX-2.3 | Comfy-Org ltx-2 |
| `clip_l.safetensors` | Flux Kontext, Hunyuan | comfyanonymous/flux_text_encoders |
| `rife49.pth` / `RealESRGAN_x4.pth` | most video workflows | RIFE · RealESRGAN |

## Licenses (read before commercial use)

| Family | License |
|---|---|
| Wan (all) | Apache-2.0 |
| Flux Dev / Kontext | FLUX.1 [dev] **Non-Commercial** |
| Flux.2 Dev | FLUX.2 [dev] — check model card |
| Qwen Image | Apache-2.0 |
| Hunyuan Video | Tencent Hunyuan Community |
| LTXV-2 / 2.3 | Apache-2.0 (check LTX card) |
| Z-Image / MMAudio | Check model card |

# Model Families

One place to understand every base model used across the workflows — what it is, which workflow runs it,
its recommended VRAM, and where to download it. Filenames and downloads are in each workflow's `downloads.md`
(and [docs/DOWNLOADS.md](../docs/DOWNLOADS.md)); the Wan generations are compared in
[docs/WAN-LINEAGE.md](../docs/WAN-LINEAGE.md).

**Current** = the workflow I'd use today. **Older** = still works, kept for 4 GB cards or because people use it.

| Family | What it is | Tasks | Workflow(s) | Min VRAM | |
|---|---|---|---|---|---|
| **MiniMax H3** | Video + sound (T2V/I2V/references/pose/extend), Ref2VA + FL2VA models | T2V·I2V·R2V·FLF·pose·extend·audio | [minimax/h3-ultimate-12gb](../workflows/minimax/h3-ultimate-12gb) | 12 GB | current |
| **Viggle-Animate (H3 finetune)** | Swap the person in a video for one still | V2V | [minimax/viggle-animate-h3](../workflows/minimax/viggle-animate-h3) | 12 GB | current |
| **LTX 2.5 (22B)** | Video + sound, first/last frame, pose IC-LoRA | T2V·I2V·FLF·pose·audio | [ltx/ltx-2.5-ultimate-12gb](../workflows/ltx/ltx-2.5-ultimate-12gb) | 12 GB | current |
| **LTXV-2.3 (22B)** | LTX before 2.5, FFLF + ID LoRA | T2V·I2V·FFLF·audio | [ltx/ltx2.3-ultimate](../workflows/ltx/ltx2.3-ultimate) | 12 GB | older |
| **LTXV-2 (19B)** | First audio-aware LTX | T2V·I2V·audio | [ltx/ltx2](../workflows/ltx/ltx2) | 4 GB | older |
| **Wan Animate 2** | Character animation from a driving video (distilled, int8) | V2V | [wan2.2/animate-ultimate](../workflows/wan2.2/animate-ultimate) | 12 GB (GGUF mode lower) | current |
| **Wan 2.2 Animate** | Reference-driven character animation (GGUF) | V2V | [wan2.2/animate](../workflows/wan2.2/animate) · GGUF mode of [animate-ultimate](../workflows/wan2.2/animate-ultimate) | 4 GB | older |
| **Wan 2.2** | MoE dual-expert video (A14B) + TI2V-5B | T2V·I2V | [wan2.2/gguf-lowvram](../workflows/wan2.2/gguf-lowvram) · [wan2.2/aio-rapid](../workflows/wan2.2/aio-rapid) | 4 GB | 4 GB pick |
| **Wan 2.1** | First-gen Wan video (1.3B/14B) | T2V·I2V·VACE·FLF·Fun | [wan2.1/gguf-lowvram](../workflows/wan2.1/gguf-lowvram) · [wan2.1/flf2v](../workflows/wan2.1/flf2v) | 4 GB | older |
| **Hunyuan Video** | Tencent video model | T2V·I2V | [hunyuan/video](../workflows/hunyuan/video) | 4 GB | older |
| **Qwen Image 2.1** | 7B image gen + edit, native 2K, Turbo, Fun ControlNet, remove background | T2I·edit·ControlNet | [qwen/image-2.1-ultimate-12gb](../workflows/qwen/image-2.1-ultimate-12gb) · [qwen/image-2.1-12gb](../workflows/qwen/image-2.1-12gb) | 12 GB | current |
| **Qwen Image (2509)** | First Qwen Image + edit (GGUF) | T2I·edit | [qwen/image-edit-2509](../workflows/qwen/image-edit-2509) | 4 GB | 4 GB pick |
| **Krea 2 / Kroma** | Krea 2 Turbo + lodestones' Kroma fine-tune, style reference + style LoRAs | T2I·style | [krea/krea-2-ultimate-12gb](../workflows/krea/krea-2-ultimate-12gb) | 12 GB | current |
| **Ming Image 0.1 Design** | Design / text-in-image model with real transparency | T2I·edit·RGBA | [ming/image-0.1-design-12gb](../workflows/ming/image-0.1-design-12gb) | 12 GB | current |
| **Flux.2 Dev** | Flux.2 image model (Mistral encoder) | T2I | [flux/flux2-dev](../workflows/flux/flux2-dev) | 6 GB | older |
| **Flux (Kontext)** | Flux image gen + editing (GGUF) | T2I·edit | [flux/kontext](../workflows/flux/kontext) | 4 GB | older |
| **Z-Image Turbo** | Fast few-step image gen (Qwen-3 encoder) | T2I | [z-image/turbo](../workflows/z-image/turbo) | 4 GB | 4 GB pick |
| **Pixal3D · TRELLIS.2** | One image → textured 3D mesh (.glb) | 3D | [3d/image-to-3d-ultimate-12gb](../workflows/3d/image-to-3d-ultimate-12gb) | 12 GB | current |
| **YuE2** | Songs with vocals from a style + lyrics, cover mode | music | [audio/yue2-music-12gb](../workflows/audio/yue2-music-12gb) | 12 GB | current |
| **MMAudio** | Audio for a video clip | audio | [audio/ai-audio-maker](../workflows/audio/ai-audio-maker) | low | current |

## Shared support models

Several workflows reuse the same encoders/VAEs — download once (subfolders inside the model folder are fine):

| File | Used by | Source |
|---|---|---|
| `t5xxl_um_fp8_e4m3fn_scaled.safetensors` (UMT5) | Wan 2.1, Wan 2.2 GGUF | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (same encoder, Comfy's name) | Wan 2.2 Animate, AIO Rapid, Wan Animate Ultimate | Comfy-Org Wan repackaged |
| `wan_2.1_vae.safetensors` | Wan 2.1, Wan 2.2 14B, AIO, Wan Animate Ultimate (GGUF mode) | Comfy-Org repackaged |
| `gemma_3_12B_it_*.safetensors` | LTX-2, LTX-2.3 | Comfy-Org ltx-2 / GitMylo (fp8) |
| `qwen3vl_32b_minimax_h3_*` · `minimax_h3_*_vae_*` | H3 Ultimate, Viggle-Animate | Comfy-Org/MiniMax-H3 |
| `sdpose_wholebody_fp16.safetensors` + `rt_detr_v4-x-hgnet_fp16.safetensors` | H3 / LTX 2.5 / Qwen 2.1 Ultimates, Wan Animate Ultimate (pose) | Comfy-Org/SDPose |
| `clip_l.safetensors` | Flux Kontext, Hunyuan | comfyanonymous/flux_text_encoders |
| `RealESRGAN_x4.pth` / `RealESRGAN_x2.pth` | Wan 2.1, Wan 2.2 GGUF, Flux Kontext | ai-forever/Real-ESRGAN |
| `rife49.pth` | Wan 2.1, Wan 2.2 GGUF, Wan 2.2 Animate | downloaded by ComfyUI-Frame-Interpolation itself |

## Licenses (read before commercial use)

From each model's Hugging Face card, read 2026-10-14. This repo's MIT license covers the workflow files and docs
only — every model keeps its own license. Not legal advice: open the card before you use outputs commercially.

| Family | License on the card |
|---|---|
| Wan 2.1 / 2.2 / 2.2 Animate / Wan Animate 2 | Apache-2.0 |
| Qwen Image (original, 2509) | Apache-2.0 |
| Z-Image Turbo | Apache-2.0 |
| Ming Image 0.1 | MIT |
| Pixal3D · TRELLIS.2 · BiRefNet · MoGe · SDPose | MIT |
| Lotus (depth) | Apache-2.0 |
| MiniMax H3 (+ Viggle-Animate finetune) | MiniMax H3 Community License Agreement (its own terms; the standard grant excludes some territories — read it) |
| LTX-2 / LTX-2.3 / LTX 2.5 | LTX-2 Community License Agreement (LTX 2.5 is gated: accept the terms on the model page) |
| Krea 2 / Kroma | Krea 2 Community License |
| Hunyuan Video | Tencent Hunyuan Community License |
| Gemma 3 text encoder (LTX-2 / 2.3) | Gemma Terms of Use |
| **Qwen Image 2.1** (+ Viggle turbo LoRA) | **Qwen Research License** — research / non-commercial |
| **Flux Kontext / Flux.2 Dev** | **FLUX [dev] Non-Commercial License** (Flux.2 Dev is gated) |
| **YuE2** | **CC-BY-NC-4.0** — non-commercial |
| **MMAudio** | **CC-BY-NC-4.0** — non-commercial (Kijai's safetensors repack is tagged MIT; the original weights are NC) |

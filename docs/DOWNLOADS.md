# Master Download Database

Every model, LoRA, VAE, text encoder and helper referenced by any workflow in this repository.

**How to read this:**
- **In-workflow filename** = the exact string found inside the workflow `.json` (verified). This is what the
  loader node expects to see in your `ComfyUI/models/...` folder.
- **Source** = the repository the file comes from (from the creator's Hugging Face READMEs).
- **Verified?** = `JSON` means the filename was read straight out of a workflow file; `README` means it comes
  from the creator's published notes but the workflow JSON wasn't available to cross-check (the four
  CivitAI-only workflows); `Not verified` means neither could confirm it.

> Folder targets throughout: `diffusion_models/`, `loras/`, `vae/`, `text_encoders/`, `clip_vision/` inside `ComfyUI/models/`.

---

## Wan 2.1 — [wan2.1/gguf-lowvram](../workflows/wan2.1/gguf-lowvram)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion (I2V 14B) | `wan2.1-i2v-14b-480p-Q3_K_M.gguf` | [city96/Wan2.1-I2V-14B-480P-gguf](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf) | JSON |
| Diffusion (T2V 1.3B) | `Wan2.1-T2V-1.3B-F16.gguf` | [calcuis/wan-1.3b-gguf](https://huggingface.co/calcuis/wan-1.3b-gguf) | JSON |
| Diffusion (FLF 14B) | `wan2.1-flf2v-720p-14b-q2_k.gguf` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | JSON |
| Diffusion (VACE 1.3B) | `wan2.1-vace-1.3b-f16.gguf` | [QuantStack/Wan2.1_14B_VACE-GGUF](https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF) | JSON |
| Diffusion (Fun Control) | `wan2.1-fun-control-1.3b-q8_0.gguf` | [city96/Wan2.1-Fun-14B-Control-gguf](https://huggingface.co/city96/Wan2.1-Fun-14B-Control-gguf) | JSON |
| Diffusion (Fun Camera) | `Wan2.1-Fun-V1.1-14B-Control-Camera-Q3_K_M.gguf` | [QuantStack/Wan2.1-Fun-V1.1-14B-Control-Camera-GGUF](https://huggingface.co/QuantStack/Wan2.1-Fun-V1.1-14B-Control-Camera-GGUF) | JSON |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files) | JSON |
| VAE | `wan_2.1_vae.safetensors` / `wan_2.1_vae_fp8_e4m3fn.safetensors` | Comfy-Org repackaged (above) | JSON |
| CLIP vision | `clip_vision_h_fp8_e4m3fn.safetensors` | Comfy-Org repackaged (above) | JSON |
| Frame interp | `rife49.pth` | RIFE (ComfyUI-Frame-Interpolation) | JSON |
| Upscale | `RealESRGAN_x4.pth` | RealESRGAN | JSON |
| Depth (Fun) | `depth_anything_vitl14.pth` | Depth-Anything | JSON |

## Wan 2.2 — [wan2.2/gguf-lowvram](../workflows/wan2.2/gguf-lowvram)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion (T2V 14B, **high noise**) | `wan2.2_t2v_high_noise_14B_Q2_K.gguf` | [QuantStack/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF) | JSON |
| Diffusion (T2V 14B, **low noise**) | `wan2.2_t2v_low_noise_14B_Q2_K.gguf` | QuantStack (above) | JSON |
| Diffusion (I2V 14B, high/low) | `Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf` · `...-LowNoise-Q2_K.gguf` | [bullerwins/Wan2.2-I2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF) | JSON |
| Diffusion (TI2V 5B) | `Wan2.2-TI2V-5B-Q5_1.gguf` | [QuantStack/Wan2.2-TI2V-5B-GGUF](https://huggingface.co/QuantStack/Wan2.2-TI2V-5B-GGUF) | JSON |
| Speed LoRA (T2V) | `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | JSON |
| Speed LoRA (I2V) | `Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_fixed.safetensors` | Kijai/WanVideo_comfy | JSON |
| VAE (5B) | `Wan2.2_VAE.safetensors` | Comfy-Org Wan 2.2 repackaged | JSON |
| VAE (14B) | `wan_2.1_vae.safetensors` | Comfy-Org repackaged | JSON |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled.safetensors` | Comfy-Org repackaged | JSON |

## Wan 2.2 Animate — [wan2.2/animate](../workflows/wan2.2/animate)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `Wan2.2-Animate-14B-Q8_0.gguf` / `Q5_K_S` | [QuantStack/Wan2.2-Animate-14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF) | JSON |
| Relight LoRA | `WanAnimate_relight_lora_fp16.safetensors` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) | JSON |
| Speed LoRA | `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | Comfy-Org Wan 2.1 repackaged | JSON |
| CLIP vision | `clip_vision_h.safetensors` | Comfy-Org repackaged | JSON |
| VAE | `wan_2.1_vae.safetensors` / `Wan2.1_VAE.pth` | Comfy-Org repackaged | JSON |
| Frame interp | `rife49.pth` | RIFE | JSON |

## Flux Kontext — [flux/kontext](../workflows/flux/kontext)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `flux1-kontext-dev-Q5_1.gguf` | [QuantStack/FLUX.1-Kontext-dev-GGUF](https://huggingface.co/QuantStack/FLUX.1-Kontext-dev-GGUF) | JSON |
| VAE | `ae.safetensors` | [ffxvs/vae-flux](https://huggingface.co/ffxvs/vae-flux/blob/main/ae.safetensors) | JSON |
| CLIP | `clip_l.safetensors` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) | JSON |
| Text encoder | `t5xxl_fp8_e4m3fn.safetensors` | comfyanonymous/flux_text_encoders | JSON |
| Style LoRAs | `FC Flux Perfect Busts` · `FLUX_Polyhedron_all_Kohya_ss-000001` · `FluxDFaeTasticDetails` | CivitAI (style LoRAs, optional) | JSON |
| Upscale | `RealESRGAN_x4.pth` | RealESRGAN | JSON |

## Hunyuan Video — [hunyuan/video](../workflows/hunyuan/video)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion ⚠️ | `flux1-dev-Q5_K_S.gguf` **(see audit — likely a leftover node)** | recommended instead: [city96/FastHunyuan-gguf](https://huggingface.co/city96/FastHunyuan-gguf) → `fast-hunyuan-video-t2v-720p-Q5_K_M.gguf` | JSON (mismatch) |
| VAE | `kijai_hunyuan_video_vae_bf16.safetensors` | [calcuis/hunyuan-gguf](https://huggingface.co/calcuis/hunyuan-gguf) | JSON |
| Text encoder | `llava_llama3_fp8_scaled.safetensors` | calcuis/hunyuan-gguf | JSON |
| CLIP | `clip_l.safetensors` | comfyanonymous/flux_text_encoders | JSON |
| Upscale | `4x-AnimeSharp.pth` | 4x-AnimeSharp | JSON |

## Qwen Image & Edit 2509 — [qwen/image-edit-2509](../workflows/qwen/image-edit-2509)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `Qwen_Image-Q8_0.gguf` | [QuantStack/Qwen-Image-GGUF](https://huggingface.co/QuantStack/Qwen-Image-GGUF) · [Edit-2509](https://huggingface.co/QuantStack/Qwen-Image-Edit-2509-GGUF) | JSON |
| Speed LoRA | `Qwen-Image-Lightning-8steps-V2.0.safetensors` | [lightx2v/Qwen-Image-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Lightning) | JSON |
| Text encoder | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI) | JSON |
| VAE | `qwen_image_vae.safetensors` | Comfy-Org/Qwen-Image_ComfyUI | JSON |

## LTX-2 — [ltx/ltx2](../workflows/ltx/ltx2)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `ltx-2-19b-distilled_Q4_K_M.gguf` | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy) | JSON |
| Text encoder | `gemma_3_12B_it_fp8_e4m3fn.safetensors` | [Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders) | JSON |
| Connector | `ltx-2-19b-embeddings_connector_dev_bf16.safetensors` | Kijai/LTXV2_comfy | JSON |
| VAE (video) | `LTX2_video_vae_bf16.safetensors` | Kijai/LTXV2_comfy | JSON |
| VAE (audio) | `LTX2_audio_vae_bf16.safetensors` | Kijai/LTXV2_comfy | JSON |
| Upscaler | `ltx-2-spatial-upscaler-x2-1.0.safetensors` | [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2) | JSON |
| Distill LoRA | `ltx-2-19b-distilled-lora-384.safetensors` | Lightricks/LTX-2 | JSON |

## LTX-2.3 Ultimate — [ltx/ltx2.3-ultimate](../workflows/ltx/ltx2.3-ultimate)

| Role | In-workflow filename | Source | Verified? |
|---|---|---|---|
| Diffusion | `ltx-2.3-22b-dev-Q5_K_M.gguf` | [unsloth/LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF) | JSON |
| Text encoder | `gemma_3_12B_it_fp4_mixed.safetensors` | [Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders) | JSON |
| Text projection | `ltx-2.3_text_projection_bf16.safetensors` | [Kijai/LTX2.3_comfy](https://huggingface.co/Kijai/LTX2.3_comfy) | JSON |
| VAE (video/audio) | `ltx-2.3-22b-dev_video_vae.safetensors` · `..._audio_vae.safetensors` | unsloth/LTX-2.3-GGUF | JSON |
| Distill LoRA (required) | `ltx-2.3-22b-distilled-lora-384-1.1.safetensors` | Kijai/LTX2.3_comfy | JSON |
| ID LoRA | `ltx-2.3-id-lora-talkvid-3k.safetensors` | Kijai/LTX2.3_comfy | JSON |
| Upscaler | `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | Lightricks/LTX-2 | JSON |

---

## Flux.2 Dev — [flux/flux2-dev](../workflows/flux/flux2-dev)

| Role | In-workflow filename | Verified? |
|---|---|---|
| Diffusion | `flux2-dev-Q5_K_M.gguf` | JSON |
| Text encoder | `mistral_3_small_flux2_fp4_mixed.safetensors` | JSON |
| VAE | `flux2-vae.safetensors` | JSON |

## Z-Image Turbo — [z-image/turbo](../workflows/z-image/turbo)

| Role | In-workflow filename | Verified? |
|---|---|---|
| Diffusion | `z-image-turbo-q8_0.gguf` | JSON |
| Text encoder | `qwen_3_4b.safetensors` | JSON |
| VAE | `ae.safetensors` | JSON |

## Wan 2.2 AIO Rapid — [wan2.2/aio-rapid](../workflows/wan2.2/aio-rapid)

| Role | In-workflow filename | Verified? |
|---|---|---|
| Diffusion (single AIO) | `wan2.2-rapid-mega-aio-v12-Q4_K.gguf` | JSON |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | JSON |
| VAE | `wan_2.1_vae.safetensors` | JSON |

## AI Audio Maker — [audio/ai-audio-maker](../workflows/audio/ai-audio-maker)

| Role | In-workflow filename | Verified? |
|---|---|---|
| MMAudio model | `mmaudio_large_44k_v2_fp16.safetensors` | JSON |
| Synchformer | `mmaudio_synchformer_fp16.safetensors` | JSON |
| MMAudio VAE | `mmaudio_vae_44k_fp16.safetensors` | JSON |
| CLIP | `apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors` | JSON |

> ✅ **All 12 workflows are now model-verified from their JSON.** Source-repo confirmation for a few Flux.2 /
> Z-Image filenames is still recommended (filenames are verified; exact host repos are best-effort).

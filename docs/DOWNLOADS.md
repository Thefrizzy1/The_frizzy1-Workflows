# Master Download Database

Every model, LoRA, VAE and encoder each workflow loads — generated 2026-10-14 from the workflows' `models.json`
manifests, which were checked against the workflow `.json` files (every file name below is exactly what the loader
expects) and whose links were all tested. `python scripts/frizzy.py get <workflow>` downloads the same list.

- **Folder** = inside `ComfyUI/models/` (or your extra model paths). Subfolders inside it are fine.
- **required / optional** = what `frizzy.py get` fetches by default / with `--optional`.
- Where a source file has another name than the one the workflow loads, the tool saves it under the workflow's
  name (the note says so) — that is why the loader finds it without re-picking.
- Licenses: [models/README.md](../models/README.md#licenses-read-before-commercial-use).

---

# 🎬 Video

## Wan 2.2 Animate — [wan2.2/animate](../workflows/wan2.2/animate)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`Wan2.2-Animate-14B-Q8_0.gguf`](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q8_0.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-Animate-14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF) | 12GB target. Use Q4_K_M for 4GB. |
| required | LoRA | [`WanAnimate_relight_lora_fp16.safetensors`](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) |  |
| optional | LoRA | [`lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors`](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | Speed LoRA. The .json loads a renamed file, high_noise_model(wan2.2light2xvI2v_v2.2).safetensors, that has no public source: use this one and pick it in the LoRA loader (tested in animate-ultimate). |
| required | Text encoder | [`umt5_xxl_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) |  |
| required | CLIP vision | [`clip_vision_h.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) | `clip_vision/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) |  |
| required | VAE | [`Wan2.1_VAE.pth`](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B/resolve/main/Wan2.1_VAE.pth) | `vae/` | [Wan-AI/Wan2.2-Animate-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B) | 0.5 GB |

Custom node packs: [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [execution-inversion-demo-comfyui](https://github.com/BadCafeCode/execution-inversion-demo-comfyui), [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials), [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

## Wan 2.2 GGUF Low-VRAM — [wan2.2/gguf-lowvram](../workflows/wan2.2/gguf-lowvram)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| optional | Model | [`Wan2.2-TI2V-5B-Q5_1.gguf`](https://huggingface.co/QuantStack/Wan2.2-TI2V-5B-GGUF/resolve/main/Wan2.2-TI2V-5B-Q5_1.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-TI2V-5B-GGUF](https://huggingface.co/QuantStack/Wan2.2-TI2V-5B-GGUF) | TI2V-5B single-file alternative (neither .json loads it; swap it into the loader). |
| optional | LoRA | [`lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors`](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank128_bf16.safetensors) | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | Speed LoRA for T2V. |
| required | VAE | [`wan_2.1_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |  |
| optional | VAE | [`wan2.2_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) | VAE for the TI2V-5B alternative only. |
| required | Model | [`wan2.2_t2v_high_noise_14B_Q2_K.gguf`](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF/resolve/main/wan2.2_t2v_high_noise_14B_Q2_K.gguf) | `diffusion_models/` | [bullerwins/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF) | T2V 14B high-noise expert (you need both). 5.3 GB |
| required | Model | [`wan2.2_t2v_low_noise_14B_Q2_K.gguf`](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF/resolve/main/wan2.2_t2v_low_noise_14B_Q2_K.gguf) | `diffusion_models/` | [bullerwins/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF) | T2V 14B low-noise expert. 5.3 GB |
| required | Model | [`Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf`](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/HighNoise/Wan2.2-I2V-A14B-HighNoise-Q2_K.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-I2V-A14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF) | I2V 14B high-noise expert. 5.3 GB |
| required | Model | [`Wan2.2-I2V-A14B-LowNoise-Q2_K.gguf`](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/LowNoise/Wan2.2-I2V-A14B-LowNoise-Q2_K.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-I2V-A14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF) | I2V 14B low-noise expert. 5.3 GB |
| required | Text encoder | [`t5xxl_um_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 6.7 GB |
| required | Upscaler | [`RealESRGAN_x2.pth`](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x2.pth) | `upscale_models/` | [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN) | Upscaler, 0.07 GB |
| optional | LoRA | `Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64_fixed.safetensors` (by hand) | `loras/` | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy) | I2V speed LoRA: this name is no longer published. Use Kijai's lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors and pick it in the LoRA loader. |

Custom node packs: [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation), [ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox).

## Wan 2.2 AIO Rapid — [wan2.2/aio-rapid](../workflows/wan2.2/aio-rapid)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Text encoder | [`umt5_xxl_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) |  |
| required | VAE | [`wan_2.1_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |  |
| required | Model | [`wan2.2-rapid-mega-aio-v12-Q4_K.gguf`](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF/resolve/main/Mega-v12/wan2.2-rapid-mega-aio-v12-Q4_K.gguf) | `diffusion_models/` | [befox/WAN2.2-14B-Rapid-AllInOne-GGUF](https://huggingface.co/befox/WAN2.2-14B-Rapid-AllInOne-GGUF) | Single all-in-one file. 11.6 GB |

Custom node packs: [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler).

## Wan 2.1 GGUF Low-VRAM — [wan2.1/gguf-lowvram](../workflows/wan2.1/gguf-lowvram)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`wan2.1-i2v-14b-480p-Q3_K_M.gguf`](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf/resolve/main/wan2.1-i2v-14b-480p-Q3_K_M.gguf) | `diffusion_models/` | [city96/Wan2.1-I2V-14B-480P-gguf](https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf) | I2V. Pick your quant from the repo. |
| optional | Model | [`Wan2.1-T2V-1.3B-F16.gguf`](https://huggingface.co/calcuis/wan-1.3b-gguf/resolve/main/wan2.1_t2v_1.3b-f16.gguf) | `diffusion_models/` | [calcuis/wan-1.3b-gguf](https://huggingface.co/calcuis/wan-1.3b-gguf) | T2V 1.3B, the lightest option. Downloads calcuis' wan2.1_t2v_1.3b-f16.gguf (renamed on the repo) and saves it under the name the workflow loads. 2.9 GB |
| required | VAE | [`wan_2.1_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |  |
| required | Text encoder | [`t5xxl_um_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 6.7 GB |
| required | CLIP vision | [`clip_vision_h_fp8_e4m3fn.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/clip_vision_h_fp8_e4m3fn.safetensors) | `clip_vision/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 0.6 GB |
| required | Upscaler | [`RealESRGAN_x4.pth`](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | `upscale_models/` | [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN) | Upscaler, 0.07 GB |
| required | VAE | [`wan_2.1_vae_fp8_e4m3fn.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/wan_2.1_vae_fp8_e4m3fn.safetensors) | `vae/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 0.1 GB |

Custom node packs: [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

## Wan 2.1 FLF2V — [wan2.1/flf2v](../workflows/wan2.1/flf2v)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`wan2.1-flf2v-720p-14b-q2_k.gguf`](https://huggingface.co/calcuis/wan-gguf/resolve/main/wan2.1-flf2v-720p-14b-q2_k.gguf) | `diffusion_models/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | Pick your quant from the repo. |
| required | VAE | [`wan_2.1_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) |  |
| required | Text encoder | [`t5xxl_um_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/t5xxl_um_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 6.7 GB |
| required | CLIP vision | [`clip_vision_h_fp8_e4m3fn.safetensors`](https://huggingface.co/calcuis/wan-gguf/resolve/main/clip_vision_h_fp8_e4m3fn.safetensors) | `clip_vision/` | [calcuis/wan-gguf](https://huggingface.co/calcuis/wan-gguf) | 0.6 GB |
| required | Upscaler | [`RealESRGAN_x4.pth`](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | `upscale_models/` | [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN) | Upscaler, 0.07 GB |

Custom node packs: [gguf](https://github.com/calcuis/gguf), [tiled_ksampler](https://github.com/FlyingFireCo/tiled_ksampler), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

## Hunyuan Video Low-VRAM — [hunyuan/video](../workflows/hunyuan/video)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`fast-hunyuan-video-t2v-720p-Q5_K_M.gguf`](https://huggingface.co/city96/FastHunyuan-gguf/resolve/main/fast-hunyuan-video-t2v-720p-Q5_K_M.gguf) | `diffusion_models/` | [city96/FastHunyuan-gguf](https://huggingface.co/city96/FastHunyuan-gguf) | Fast Hunyuan, recommended. |
| required | Text encoder | [`llava_llama3_fp8_scaled.safetensors`](https://huggingface.co/calcuis/hunyuan-gguf/resolve/main/llava_llama3_fp8_scaled.safetensors) | `text_encoders/` | [calcuis/hunyuan-gguf](https://huggingface.co/calcuis/hunyuan-gguf) |  |
| required | Text encoder | [`clip_l.safetensors`](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) | `text_encoders/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) |  |
| required | VAE | [`kijai_hunyuan_video_vae_bf16.safetensors`](https://huggingface.co/Kijai/HunyuanVideo_comfy/resolve/main/hunyuan_video_vae_bf16.safetensors) | `vae/` | [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | Downloads Kijai/HunyuanVideo_comfy hunyuan_video_vae_bf16.safetensors and saves it under the name the workflow loads. 0.5 GB |
| required | Upscaler | [`4x-AnimeSharp.pth`](https://huggingface.co/Kim2091/AnimeSharp/resolve/main/4x-AnimeSharp.pth) | `upscale_models/` | [Kim2091/AnimeSharp](https://huggingface.co/Kim2091/AnimeSharp) | Upscaler, 0.07 GB |

Custom node packs: [gguf](https://github.com/calcuis/gguf), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-HunyuanVideoWrapper](https://github.com/kijai/ComfyUI-HunyuanVideoWrapper), [ComfyUI-HunyuanVideoSamplerSave](https://github.com/ShmuelRonen/ComfyUI-HunyuanVideoSamplerSave).

## LTX-2 GGUF — [ltx/ltx2](../workflows/ltx/ltx2)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | VAE | [`LTX2_video_vae_bf16.safetensors`](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_video_vae_bf16.safetensors) | `vae/` | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy) |  |
| required | VAE | [`LTX2_audio_vae_bf16.safetensors`](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_audio_vae_bf16.safetensors) | `vae/` | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy) |  |
| required | Text encoder | [`ltx-2-19b-embeddings_connector_dev_bf16.safetensors`](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/text_encoders/ltx-2-19b-embeddings_connector_dev_bf16.safetensors) | `text_encoders/` | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy) |  |
| required | Model | [`ltx-2-19b-distilled_Q4_K_M.gguf`](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/diffusion_models/ltx-2-19b-distilled_Q4_K_M.gguf) | `diffusion_models/` | [Kijai/LTXV2_comfy](https://huggingface.co/Kijai/LTXV2_comfy) | The distilled model both .json files load. 12.7 GB |
| required | Text encoder | [`gemma_3_12B_it_fp8_e4m3fn.safetensors`](https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/resolve/main/gemma_3_12B_it_fp8_e4m3fn.safetensors) | `text_encoders/` | [GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn](https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn) | Gemma 3 12B text encoder. 13.2 GB |
| required | Latent upscaler | [`ltx-2-spatial-upscaler-x2-1.0.safetensors`](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) | `latent_upscale_models/` | [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2) | 2x latent upscaler. 1.0 GB |
| optional | LoRA | [`ltx-2-19b-distilled-lora-384.safetensors`](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) | `loras/` | [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2) | Its loader ships bypassed. 7.7 GB |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

## LTX-2.3 Ultimate — [ltx/ltx2.3-ultimate](../workflows/ltx/ltx2.3-ultimate)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`ltx-2.3-22b-dev-Q5_K_M.gguf`](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/ltx-2.3-22b-dev-Q5_K_M.gguf) | `diffusion_models/` | [unsloth/LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF) | Use Q4_K_M for lower VRAM. |
| required | VAE | [`ltx-2.3-22b-dev_video_vae.safetensors`](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/vae/ltx-2.3-22b-dev_video_vae.safetensors) | `vae/` | [unsloth/LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF) | 1.5 GB |
| required | VAE | [`ltx-2.3-22b-dev_audio_vae.safetensors`](https://huggingface.co/unsloth/LTX-2.3-GGUF/resolve/main/vae/ltx-2.3-22b-dev_audio_vae.safetensors) | `vae/` | [unsloth/LTX-2.3-GGUF](https://huggingface.co/unsloth/LTX-2.3-GGUF) | The audio VAE from this repo (static / no sound = wrong audio VAE). 0.4 GB |
| required | LoRA | [`ltx-2.3-22b-distilled-lora-384-1.1.safetensors`](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384-1.1.safetensors) | `loras/` | [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) | Distilled LoRA. 7.6 GB |
| required | Text encoder | [`ltx-2.3_text_projection_bf16.safetensors`](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/text_encoders/ltx-2.3_text_projection_bf16.safetensors) | `text_encoders/` | [Kijai/LTX2.3_comfy](https://huggingface.co/Kijai/LTX2.3_comfy) | Text projection connector. 2.3 GB |
| required | Text encoder | [`gemma_3_12B_it_fp4_mixed.safetensors`](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) | `text_encoders/` | [Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2) | Gemma 3 12B text encoder. 9.5 GB |
| required | Latent upscaler | [`ltx-2.3-spatial-upscaler-x2-1.1.safetensors`](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) | `latent_upscale_models/` | [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) | 2x latent upscaler. 1.0 GB |
| required | LoRA | [`ltx-2.3-id-lora-talkvid-3k.safetensors`](https://huggingface.co/AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K/resolve/main/lora_weights.safetensors) | `loras/` | [AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K](https://huggingface.co/AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K) | ID LoRA. Downloads AviadDahan/LTX-2.3-ID-LoRA-TalkVid-3K lora_weights.safetensors and saves it under the name the workflow loads. 1.2 GB |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI-JakeUpgrade](https://github.com/jakechai/ComfyUI-JakeUpgrade), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack), [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use).

## MiniMax H3 Ultimate · 12 GB — [minimax/h3-ultimate-12gb](../workflows/minimax/h3-ultimate-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`minimax_h3_fl2va_pruned_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 21.0 GB |
| required | Model | [`minimax_h3_ref2va_pruned_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 21.0 GB |
| required | LoRA | [`minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) | `loras/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 2.0 GB |
| required | LoRA | [`minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) | `loras/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 2.0 GB |
| required | Text encoder | [`qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | `text_encoders/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 15.7 GB |
| required | VAE | [`minimax_h3_video_vae_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 2.8 GB |
| required | VAE | [`minimax_h3_audio_vae_fp32.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 0.6 GB |
| required | Model patch (ControlNet) | [`minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/model_patches/minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors) | `model_patches/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 2.3 GB |
| required | Checkpoint | [`sdpose_wholebody_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) | `checkpoints/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 1.9 GB |
| required | Model | [`rt_detr_v4-x-hgnet_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) | `diffusion_models/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 0.1 GB |

Custom node packs: none (core ComfyUI).

## LTX 2.5 Ultimate · 12 GB — [ltx/ltx-2.5-ultimate-12gb](../workflows/ltx/ltx-2.5-ultimate-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`ltx-2.5-22b-distilled-transformer-nvfp4.safetensors`](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-nvfp4.safetensors) | `diffusion_models/` | [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Gated: accept Lightricks' terms on huggingface.co/Lightricks/LTX-2.5 (logged in), then set HF_TOKEN. 18.7 GB |
| required | Text encoder | [`gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors`](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) | `text_encoders/` | [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Gated: accept Lightricks' terms on huggingface.co/Lightricks/LTX-2.5 (logged in), then set HF_TOKEN. 15.4 GB |
| required | VAE | [`ltx-2.5-video-vae-bf16.safetensors`](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors) | `vae/` | [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Gated: accept Lightricks' terms on huggingface.co/Lightricks/LTX-2.5 (logged in), then set HF_TOKEN. 1.5 GB |
| required | VAE | [`ltx-2.5-audio-vae-bf16.safetensors`](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors) | `vae/` | [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Gated: accept Lightricks' terms on huggingface.co/Lightricks/LTX-2.5 (logged in), then set HF_TOKEN. 0.4 GB |
| required | Latent upscaler | [`ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors`](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors) | `latent_upscale_models/` | [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Gated: accept Lightricks' terms on huggingface.co/Lightricks/LTX-2.5 (logged in), then set HF_TOKEN. 1.0 GB |
| required | LoRA | [`ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors`](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control/resolve/main/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors) | `loras/` | [Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control) | 0.7 GB |
| required | Checkpoint | [`sdpose_wholebody_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) | `checkpoints/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 1.9 GB |
| required | Model | [`rt_detr_v4-x-hgnet_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) | `diffusion_models/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 0.1 GB |

Custom node packs: none (core ComfyUI).

## Viggle-Animate (H3) — [minimax/viggle-animate-h3](../workflows/minimax/viggle-animate-h3)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`minimax_h3_ref2va_viggle_pruned_int8_convrot.safetensors`](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI/resolve/main/diffusion_models/minimax_h3_ref2va_viggle_pruned_int8_convrot.safetensors) | `diffusion_models/` | [drbaph/Viggle-Animate-ComfyUI](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI) | 21.0 GB |
| required | LoRA | [`viggle_animate_dmd_lora_r64.safetensors`](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI/resolve/main/loras/viggle_animate_dmd_lora_r64.safetensors) | `loras/` | [drbaph/Viggle-Animate-ComfyUI](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI) | 0.9 GB |
| required | Text conditioning | [`fixed_embed_fwd_anyframe.safetensors`](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI/resolve/main/text_cond/fixed_embed_fwd_anyframe.safetensors) | `text_cond/` | [drbaph/Viggle-Animate-ComfyUI](https://huggingface.co/drbaph/Viggle-Animate-ComfyUI) | 0.0 GB |
| required | VAE | [`minimax_h3_video_vae_fp16.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | 5.2 GB |

Custom node packs: [ComfyUI-Viggle-Animate-H3](https://github.com/Saganaki22/ComfyUI-Viggle-Animate-H3).

## H3 Character Swap · 12 GB — [minimax/h3-character-swap-12gb](../workflows/minimax/h3-character-swap-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`minimax_h3_ref2va_pruned_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | all. 21.0 GB |
| required | LoRA | [`minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) | `loras/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | Turbo (4 steps). 2.0 GB |
| required | Text encoder | [`qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | `text_encoders/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | all. 15.7 GB |
| required | VAE | [`minimax_h3_video_vae_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | all. 2.8 GB |
| required | VAE | [`minimax_h3_audio_vae_fp32.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | all. 0.6 GB |
| required | LoRA | [`h3_character_swap_pro4500_1000.safetensors`](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/resolve/main/h3_character_swap_pro4500_1000.safetensors) | `loras/` | [akatz-ai/MiniMax-H3-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA) | the swap. 0.2 GB |

Custom node packs: none (core ComfyUI).

## Story Creator · 12 GB — [story/story-creator-12gb](../workflows/story/story-creator-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`qwen_image_2.1_turbo_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | stills. 7.3 GB |
| required | Text encoder | [`qwen3vl_8b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | `text_encoders/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | stills. 9.4 GB |
| required | VAE | [`qwen_image_2.1_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | stills. 0.7 GB |
| required | Model | [`minimax_h3_fl2va_pruned_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | video. 21.0 GB |
| required | LoRA | [`minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) | `loras/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | video. 2.0 GB |
| required | Text encoder | [`qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | `text_encoders/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | video. 15.7 GB |
| required | VAE | [`minimax_h3_video_vae_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | video. 2.8 GB |
| required | VAE | [`minimax_h3_audio_vae_fp32.safetensors`](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | `vae/` | [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | video. 0.6 GB |
| required | Checkpoint | [`yue2_3b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/YuE2/resolve/main/checkpoints/yue2_3b_int8_convrot.safetensors) | `checkpoints/` | [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | music. 4.0 GB |

Custom node packs: none (core ComfyUI).

## Wan Animate Ultimate — [wan2.2/animate-ultimate](../workflows/wan2.2/animate-ultimate)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`wan_animate_2_distill_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) | 16.7 GB |
| required | Text encoder | [`umt5_xxl_fp8_e4m3fn_scaled.safetensors`](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | `text_encoders/` | [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) | 6.7 GB |
| required | CLIP vision | [`clip_vision_h.safetensors`](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/clip_vision/clip_vision_h.safetensors) | `clip_vision/` | [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) | 1.3 GB |
| required | VAE | [`Wan2_1_VAE_bf16.safetensors`](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/vae/Wan2_1_VAE_bf16.safetensors) | `vae/` | [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) | 0.3 GB |
| optional | LoRA | [`lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors`](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/loras/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) | `loras/` | [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) | 0.7 GB |
| optional | Model | [`Wan2.2-Animate-14B-Q5_K_S.gguf`](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q5_K_S.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-Animate-14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF) | GGUF mode only (lower VRAM). 12.3 GB |
| optional | Model | [`Wan2.2-Animate-14B-Q8_0.gguf`](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/resolve/main/Wan2.2-Animate-14B-Q8_0.gguf) | `diffusion_models/` | [QuantStack/Wan2.2-Animate-14B-GGUF](https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF) | GGUF mode, more VRAM/RAM: pick it in the GGUF loader. 18.7 GB |
| optional | LoRA | [`wan2.2_animate_14B_relight_lora_bf16.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_animate_14B_relight_lora_bf16.safetensors) | `loras/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) | 1.4 GB |
| optional | VAE | [`wan_2.1_vae.safetensors`](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | `vae/` | [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) | 0.2 GB |
| optional | Checkpoint | [`sdpose_wholebody_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) | `checkpoints/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 1.9 GB |
| optional | Model | [`rt_detr_v4-x-hgnet_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) | `diffusion_models/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | 0.1 GB |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF).

---

# 🖼️ Image

## Flux Kontext GGUF — [flux/kontext](../workflows/flux/kontext)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`flux1-kontext-dev-Q5_1.gguf`](https://huggingface.co/QuantStack/FLUX.1-Kontext-dev-GGUF/resolve/main/flux1-kontext-dev-Q5_1.gguf) | `diffusion_models/` | [QuantStack/FLUX.1-Kontext-dev-GGUF](https://huggingface.co/QuantStack/FLUX.1-Kontext-dev-GGUF) | Pick your quant from the repo. |
| required | VAE | [`ae.safetensors`](https://huggingface.co/ffxvs/vae-flux/resolve/main/ae.safetensors) | `vae/` | [ffxvs/vae-flux](https://huggingface.co/ffxvs/vae-flux) |  |
| required | Text encoder | [`clip_l.safetensors`](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) | `text_encoders/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) |  |
| required | Text encoder | [`t5xxl_fp8_e4m3fn.safetensors`](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors) | `text_encoders/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) |  |
| required | Upscaler | [`RealESRGAN_x4.pth`](https://huggingface.co/ai-forever/Real-ESRGAN/resolve/main/RealESRGAN_x4.pth) | `upscale_models/` | [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN) | Upscaler, 0.07 GB |
| optional | LoRA | `FC Flux Perfect Busts.safetensors` (by hand) | `loras/` | [page](https://civitai.com/models) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |
| optional | LoRA | `FLUX_Polyhedron_all_Kohya_ss-000001.safetensors` (by hand) | `loras/` | [page](https://civitai.com/models) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |
| optional | LoRA | `FluxDFaeTasticDetails.safetensors` (by hand) | `loras/` | [page](https://civitai.com/models) | One of my own LoRAs in the LoRA stack: use any Flux LoRA, or switch the slot off. |

Custom node packs: [gguf](https://github.com/calcuis/gguf), [rgthree-comfy](https://github.com/rgthree/rgthree-comfy), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes), [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials), [ComfyUI-TeaCache](https://github.com/welltop-cn/ComfyUI-TeaCache).

## Flux.2 Dev GGUF — [flux/flux2-dev](../workflows/flux/flux2-dev)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`flux2-dev-Q5_K_M.gguf`](https://huggingface.co/city96/FLUX.2-dev-gguf/resolve/main/flux2-dev-Q5_K_M.gguf) | `diffusion_models/` | [city96/FLUX.2-dev-gguf](https://huggingface.co/city96/FLUX.2-dev-gguf) | Pick your quant from the repo. |
| required | Text encoder | [`mistral_3_small_flux2_fp4_mixed.safetensors`](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_fp4_mixed.safetensors) | `text_encoders/` | [Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev) | 12.3 GB |
| required | VAE | [`flux2-vae.safetensors`](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) | `vae/` | [Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev) | 0.3 GB |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

## Qwen Image & Edit 2509 — [qwen/image-edit-2509](../workflows/qwen/image-edit-2509)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`Qwen_Image-Q8_0.gguf`](https://huggingface.co/QuantStack/Qwen-Image-GGUF/resolve/main/Qwen_Image-Q8_0.gguf) | `diffusion_models/` | [QuantStack/Qwen-Image-GGUF](https://huggingface.co/QuantStack/Qwen-Image-GGUF) | Generation. For editing use QuantStack/Qwen-Image-Edit-2509-GGUF. |
| optional | LoRA | [`Qwen-Image-Lightning-8steps-V2.0.safetensors`](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V2.0.safetensors) | `loras/` | [lightx2v/Qwen-Image-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Lightning) | Speed LoRA. |
| required | Text encoder | [`qwen_2.5_vl_7b_fp8_scaled.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) | `text_encoders/` | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI) |  |
| required | VAE | [`qwen_image_vae.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) | `vae/` | [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI) |  |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

## Qwen Image 2.1 · 12 GB — [qwen/image-2.1-12gb](../workflows/qwen/image-2.1-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`qwen_image_2.1_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | 7.3 GB |
| required | Text encoder | [`qwen3vl_8b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | `text_encoders/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | 9.4 GB |
| required | VAE | [`qwen_image_2.1_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | 0.68 GB |
| optional | LoRA | [`Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256.safetensors`](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256.safetensors) | `loras/` | [Viggle/Qwen-Image-2.1-viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo) | TURBO group only. 1.4 GB. |

Custom node packs: none (core ComfyUI).

## Qwen Image 2.1 Ultimate · 12 GB — [qwen/image-2.1-ultimate-12gb](../workflows/qwen/image-2.1-ultimate-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`qwen_image_2.1_turbo_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | Turbo on (8 steps). 7.3 GB |
| optional | Model | [`qwen_image_2.1_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | Turbo off (base). 7.3 GB |
| required | Text encoder | [`qwen3vl_8b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | `text_encoders/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | all modes. 9.4 GB |
| required | VAE | [`qwen_image_2.1_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | all modes. 0.7 GB |
| optional | Model patch (ControlNet) | [`qwen_image_2.1_fun_controlnet_union_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/model_patches/qwen_image_2.1_fun_controlnet_union_int8_convrot.safetensors) | `model_patches/` | [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | ControlNet modes. 3.8 GB |
| optional | Checkpoint | [`sdpose_wholebody_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) | `checkpoints/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | ControlNet: pose. 1.9 GB |
| optional | Model | [`rt_detr_v4-x-hgnet_fp16.safetensors`](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) | `diffusion_models/` | [Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose) | ControlNet: pose. 0.1 GB |
| optional | Model | [`lotus-depth-d-v1-1.safetensors`](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) | `diffusion_models/` | [Comfy-Org/lotus](https://huggingface.co/Comfy-Org/lotus) | ControlNet: depth. 1.7 GB |
| optional | VAE | [`vae-ft-mse-840000-ema-pruned.safetensors`](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) | `vae/` | [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | ControlNet: depth. 0.3 GB |

Custom node packs: none (core ComfyUI).

## Ming Image 0.1 · 12 GB — [ming/image-0.1-design-12gb](../workflows/ming/image-0.1-design-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`ming_image_0.1_design_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Ming-Image](https://huggingface.co/Comfy-Org/Ming-Image) | all modes. 6.2 GB |
| required | Text encoder | [`ming_image_0.1_ling_mini_2.0_w4a8.safetensors`](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_w4a8.safetensors) | `text_encoders/` | [Comfy-Org/Ming-Image](https://huggingface.co/Comfy-Org/Ming-Image) | all modes (32 GB RAM). 12.8 GB |
| required | VAE | [`ming_image_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/vae/ming_image_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Ming-Image](https://huggingface.co/Comfy-Org/Ming-Image) | all modes. 0.3 GB |

Custom node packs: none (core ComfyUI).

## Z-Image Turbo GGUF — [z-image/turbo](../workflows/z-image/turbo)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | VAE | [`ae.safetensors`](https://huggingface.co/ffxvs/vae-flux/resolve/main/ae.safetensors) | `vae/` | [ffxvs/vae-flux](https://huggingface.co/ffxvs/vae-flux) |  |
| required | Model | [`z-image-turbo-q8_0.gguf`](https://huggingface.co/unsloth/Z-Image-Turbo-GGUF/resolve/main/z-image-turbo-Q8_0.gguf) | `diffusion_models/` | [unsloth/Z-Image-Turbo-GGUF](https://huggingface.co/unsloth/Z-Image-Turbo-GGUF) | Downloads unsloth/Z-Image-Turbo-GGUF z-image-turbo-Q8_0.gguf and saves it under the name the workflow loads. 7.2 GB |
| required | Text encoder | [`qwen_3_4b.safetensors`](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) | `text_encoders/` | [Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo) | 8.0 GB |

Custom node packs: [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF), [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes).

## Krea 2 Ultimate · 12 GB — [krea/krea-2-ultimate-12gb](../workflows/krea/krea-2-ultimate-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`krea2_turbo_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2) | 12 GB (tested). 13.5 GB |
| required | Text encoder | [`qwen3vl_4b_fp8_scaled.safetensors`](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) | `text_encoders/` | [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2) | all. 5.2 GB |
| required | VAE | [`qwen_image_vae.safetensors`](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) | `vae/` | [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2) | all. 0.3 GB |
| required | LoRA | [`krea2_style_reference.safetensors`](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_style_reference.safetensors) | `loras/` | [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2) | Style reference. 0.5 GB |
| required | LoRA | [`krea2_darkbrush.safetensors`](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_darkbrush.safetensors) | `loras/` | [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2) | Style LoRA (example). 0.5 GB |
| optional | Model | [`krea_kroma_v0.3.1_turbo_opd_w4a8.safetensors`](https://huggingface.co/jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants/resolve/main/krea_kroma_v0.3.1_turbo_opd_w4a8.safetensors) | `diffusion_models/` | [jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants](https://huggingface.co/jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants) | Model = Kroma. Kroma, 12 GB (tested). 8.8 GB |
| optional | Model | [`krea_kroma_v0.3.1_turbo_opd_int8_convrot.safetensors`](https://huggingface.co/jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants/resolve/main/krea_kroma_v0.3.1_turbo_opd_int8_convrot.safetensors) | `diffusion_models/` | [jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants](https://huggingface.co/jakethessmake/Krea-Kroma-v0.3.1-Turbo-OPD-ComfyUI-Quants) | Model = Kroma. Kroma int8 (pick it in the Kroma model field). 14.1 GB |

Custom node packs: none (core ComfyUI).

---

# 🧊 3D

## Image to 3D Ultimate · 12 GB — [3d/image-to-3d-ultimate-12gb](../workflows/3d/image-to-3d-ultimate-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Model | [`pixal3d_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D) | 5.6 GB |
| required | CLIP vision | [`dino_v3_L_naf_fp32.safetensors`](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) | `clip_vision/` | [Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D) | 1.2 GB |
| required | VAE | [`trellis_2_shape_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D) | 1.1 GB |
| required | VAE | [`trellis_2_texture_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) | `vae/` | [Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D) | 0.9 GB |
| required | Model | [`trellis_2_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/TRELLIS.2/resolve/main/diffusion_models/trellis_2_int8_convrot.safetensors) | `diffusion_models/` | [Comfy-Org/TRELLIS.2](https://huggingface.co/Comfy-Org/TRELLIS.2) | 5.3 GB |
| required | background_removal | [`birefnet.safetensors`](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) | `background_removal/` | [Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet) | 0.4 GB |
| required | geometry_estimation | [`moge_2_vitl_normal_fp16.safetensors`](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) | `geometry_estimation/` | [Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe) | 0.7 GB |

Custom node packs: none (core ComfyUI).

---

# 🔊 Audio

## AI Audio Maker — [audio/ai-audio-maker](../workflows/audio/ai-audio-maker)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | MMAudio | [`mmaudio_large_44k_v2_fp16.safetensors`](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_large_44k_v2_fp16.safetensors) | `mmaudio/` | [Kijai/MMAudio_safetensors](https://huggingface.co/Kijai/MMAudio_safetensors) |  |
| required | MMAudio | [`mmaudio_synchformer_fp16.safetensors`](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_synchformer_fp16.safetensors) | `mmaudio/` | [Kijai/MMAudio_safetensors](https://huggingface.co/Kijai/MMAudio_safetensors) |  |
| required | MMAudio | [`mmaudio_vae_44k_fp16.safetensors`](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_vae_44k_fp16.safetensors) | `mmaudio/` | [Kijai/MMAudio_safetensors](https://huggingface.co/Kijai/MMAudio_safetensors) |  |
| required | MMAudio | [`apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors`](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors) | `mmaudio/` | [Kijai/MMAudio_safetensors](https://huggingface.co/Kijai/MMAudio_safetensors) |  |

Custom node packs: [ComfyUI-MMAudio](https://github.com/kijai/ComfyUI-MMAudio), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite).

## YuE2 Music · 12 GB — [audio/yue2-music-12gb](../workflows/audio/yue2-music-12gb)

| Need | Role | File the workflow loads | Folder | Source | Note |
|---|---|---|---|---|---|
| required | Checkpoint | [`yue2_3b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/YuE2/resolve/main/checkpoints/yue2_3b_int8_convrot.safetensors) | `checkpoints/` | [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | all modes. 4.0 GB |
| required | audio_encoders | [`sheetsage2_bf16.safetensors`](https://huggingface.co/Comfy-Org/YuE2/resolve/main/audio_encoders/sheetsage2_bf16.safetensors) | `audio_encoders/` | [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | Cover mode. 1.4 GB |

Custom node packs: none (core ComfyUI).

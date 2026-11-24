# Changelog - Hunyuan Video 1.5 I2V · 12 GB
## v1.0.0 (2026-11-24)
- Initial release, built from the ComfyUI template `video_hunyuan_video_1.5_720p_i2v`: numbered groups, the six inputs in group 1 (App mode), "How to use", "Downloads + requirements" and "Why the split" notes inside. Core nodes only.
- Loads the authors' 480p I2V step-distilled model as the Comfy-Org fp8 file (8.34 GB) instead of the template's 720p I2V fp16 file (16.7 GB), with the authors' settings for it: 12 steps, CFG 1, shift 7 (template: 20 steps, CFG 6, shift 7).
- The video follows the picture's shape (long side 848, other side rounded to 16 px) instead of a fixed 1280x720 crop.
- Tiled VAE decode (tile 512, overlap 64, temporal 128) instead of the plain decode: with a 10 GiB budget the plain decode reached 15.5 GiB, the tiled one 9.7 GiB.
- The template's bypassed 1080p upscale is replaced by a bypassed 480p → 720p upscale (720p latent upsampler + 720p SR step-distilled fp8, 6 steps, split at step 3). EasyCache and the template notes are removed.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, 8 GiB budget: 7 min 13 s and 11.4 GiB peak (whole GPU) for the defaults, 22 min 34 s and 12.1 GiB with the 720p upscale. Not verified on a 12 GB card.

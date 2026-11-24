# Changelog - InfiniteTalk Talking Video
## v1.0.0 (2026-11-24)
- Initial release, built from the ComfyUI template `video_wan2_1_infinitetalk`. The template's two subgraphs are laid out flat in numbered groups with the inputs in group 1. Core nodes only.
- Single speaker instead of the template's two speakers: one picture, one speech clip, the `single` InfiniteTalk patch. No masks to paint.
- Three parts (81 + 72 + 72 = 225 frames, 9.0 s at 25 fps) instead of the template's two, so an 8 s clip fits. Each part continues from all frames made so far, so part 3 reads the speech from frame 144 on.
- The 9 repeated frames at the start of each continuing part are dropped with the node's `trim_image` output. The template joins them untrimmed: in a test run that put frames 72-80 in twice and made the mouth in part 2 trail the speech by 8 frames (0.32 s).
- The video keeps the picture's shape (long side 832, sides a multiple of 16) instead of a fixed 832x480.
- Loads the Comfy-Org `wan2.1_i2v_480p_14B_fp8_scaled` and `wan_2.1_vae` instead of the template's Kijai files. Sampler, scheduler, steps (6), CFG (1) and the lightx2v LoRA are the template's.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: about 14 min for a 9 s video. Not verified on a 12 GB card.

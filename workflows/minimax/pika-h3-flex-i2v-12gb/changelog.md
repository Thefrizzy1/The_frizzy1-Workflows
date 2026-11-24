# Changelog - Pika H3 Flex I2V · 12 GB

## v1.0.0 (2026-11-24)
- Initial release. Built from ComfyUI's built-in template `video_pika_h3_flex_fl2va` (template pack 0.11.101): MiniMax H3 FL2VA int8 + Pika Flex FL2VA LoRA, the Pika 6-step sigma list, `lcm`, CFG 1, audio through the H3 audio VAE. Taken out of the subgraph into 7 numbered groups; the 8 inputs are in group 1 (App mode).
- Changed from the template: the video size is the start frame resized to 0.4 MP (shape kept, 32 px grid) instead of the picture's full size; the end frame is optional (Boolean switch, off).
- Added: **Turbo** switch for the community Pika Flex Turbo LoRA (lite r32 file, 4 steps, shift 6 / 3); group 7 (bypassed) **RelayVSR 2x** from the template `utility_relayvsr_video_x2_upscale` (1 step, CFG 1, VSR Decode).
- Tested on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, 64 GB RAM: 5 s at 800x544 in 94.6 to 100.8 s (6 steps), 65.1 to 70.1 s (Turbo); forest + 2x (1600x1088) 110.1 to 112.3 s. In a 10 GiB `--reserve-vram` budget the whole GPU peaked at 11.3 GiB with identical videos; process RAM reached 29.2 GiB. Not run on a 12 GB card.

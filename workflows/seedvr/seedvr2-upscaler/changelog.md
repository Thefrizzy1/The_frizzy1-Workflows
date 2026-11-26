# Changelog - SeedVR2 Upscaler
## v1.0.0 (2026-11-26)
- Initial release, two files: picture (SeedVR2 7B int8) and video (SeedVR2 3B int8). Core nodes only.
- Built from the ComfyUI templates `utility_seedvr2_7b_int8_upscale_image` and `utility_seedvr2_3b_int8_upscale_video`: subgraph opened into numbered groups, inputs collected in group 1 (file, factor, and for video Start / Seconds) with App mode labels. Seed and Frames per chunk sit in group 4 and are not in the App mode list.
- Changes against the templates: picture factor 2 instead of 4; colour match `lab` instead of `none`; the video is always split into chunks of 21 frames with an overlap of 2 latent frames (manual mode) instead of the template's optional split (off, `auto` mode, overlap 0); the trim switch is replaced by Start / Seconds inputs (0 = whole clip).
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell SFF Edition 24 GB, with no VRAM limit and in 12 and 10 GiB `--reserve-vram` budgets. Not verified on a 12 GB card.

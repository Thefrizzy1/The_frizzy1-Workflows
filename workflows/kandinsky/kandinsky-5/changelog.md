# Changelog - Kandinsky 5.0 Lite
## v1.0.0 (2026-11-21)
- Initial release: three workflows built from the ComfyUI templates `image_kandinsky5_t2i`, `video_kandinsky5_t2v` and `video_kandinsky5_i2v`, restructured into numbered groups with the inputs in group 1. Core nodes only.
- Text to video uses the 16-step distilled model at CFG 1 by default (3 min 35 s for 5 s on the test card); the template's sft model at 50 steps / CFG 5 took 19 min 55 s and is kept as a documented swap.
- Text to image and image to video keep the template's models and sampler settings.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB with `--reserve-vram 12`. Not verified on a 12 GB card.

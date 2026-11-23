# Changelog - ACE-Step 1.5 XL Music
## v1.0.0 (2026-11-22)
- Initial release, built from the ComfyUI template `audio_ace_step1_5_xl_base` and restructured into numbered groups with the inputs in group 1. Core nodes only.
- Same four model files and the same sampler settings as the template (50 steps, CFG 6, euler / simple, shift 3).
- The decode is `VAEDecodeAudioTiled` (tile 512, overlap 64) instead of the template's `VAEDecodeAudio`: with ComfyUI held to about 10 GiB of VRAM, a 240 s song peaked at 20.8 GiB with the template's decode and at 11.3 GiB with the tiled one.
- Style, lyrics, seconds, BPM, seed, steps and CFG are inputs in group 1. Beats per bar, language and key stay on the conditioning node and are listed in App mode.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, with and without a VRAM limit. Not verified on a 12 GB card.

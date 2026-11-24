# Changelog - ACE-Step 1.5 XL Music
## v1.1.0 (2026-11-24)
- New: `The_frizzy1_ace-step-1.5-xl-turbo-12gb_v1.1.0.json`, the same layout with the XL **turbo** model, the 1.7B song planner, 8 steps and CFG 1 (euler / simple, shift 3, tiled decode 512 / 64 as before).
- Tested on an **RTX 3060 12 GB** (32 GB RAM, ComfyUI 0.45.3, portable, sage attention), run from the saved file in the browser: the default 120 s song took 42 s on the first run and 34 to 37 s on the next two (other seeds). Whole-GPU peak 11.4 GiB, of which 2.7 GiB was held by other programs before ComfyUI started.
- The turbo model's SHA-256 matched Hugging Face (2026-11-24).
- New sample: `samples/turbo-song-1-indie-pop-120s.mp3` (default text, seed 22112026), lyrics checked by transcription.
- The base workflow (v1.0.0) is unchanged.
## v1.0.0 (2026-11-22)
- Initial release, built from the ComfyUI template `audio_ace_step1_5_xl_base` and restructured into numbered groups with the inputs in group 1. Core nodes only.
- Same four model files and the same sampler settings as the template (50 steps, CFG 6, euler / simple, shift 3).
- The decode is `VAEDecodeAudioTiled` (tile 512, overlap 64) instead of the template's `VAEDecodeAudio`: with ComfyUI held to about 10 GiB of VRAM, a 240 s song peaked at 20.8 GiB with the template's decode and at 11.3 GiB with the tiled one.
- Style, lyrics, seconds, BPM, seed, steps and CFG are inputs in group 1. Beats per bar, language and key stay on the conditioning node and are listed in App mode.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, with and without a VRAM limit. Not verified on a 12 GB card.

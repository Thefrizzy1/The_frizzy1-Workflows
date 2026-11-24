# Changelog · Stable Audio 3 Medium Base

## v1.0.0 (2026-11-24)
- First version. Built from ComfyUI's built-in template `audio_stable_audio_3_medium_base` (one subgraph node), unpacked and laid out in five numbered groups. The five inputs (idea, kind of sound, seconds, seed, Qwen on/off) are in group 1 and shown in App mode. Three notes inside.
- Same three files as the template, and the same steps (50), CFG (7), scheduler (simple), length (150 s) and Qwen settings.
- Changed from the template: sampler **euler** instead of lcm (lcm gave noise or the wrong sound on every sound effect tried); decode **in tiles** (512 / 64) instead of in one piece (20.8 GiB peak without a limit); a seed input in group 1; the prompt preview is switched on and shows the prompt actually used (the template's is bypassed); output to `output/audio/Stable-Audio-3/`.
- Run on ComfyUI 0.45.3 only, RTX PRO 4000 Blackwell 24 GB, with and without a 10 GiB VRAM budget. Not verified on a 12 GB card.

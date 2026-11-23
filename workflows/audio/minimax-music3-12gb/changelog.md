# Changelog · MiniMax Music 3 · 12 GB
## v1.1.0 (2026-11-22)
- Rebuilt from the ComfyUI template `audio_minimax_music_3` in the house layout: five numbered groups instead of one subgraph node, the five inputs as primitives in group 1 (App mode lists them), three notes. Same three files and the same sampler settings as v1.0.x.
- Longest length is 180 s by default (was 60): the default lyrics came out 163 s long.
- Output goes to `output/audio/MiniMax-Music-3/`.
- Run on ComfyUI 0.45.3 only (older versions not verified), RTX PRO 4000 Blackwell 24 GB, with and without a VRAM limit. Not verified on a 12 GB card in this version; the RTX 3060 numbers are from v1.0.0.
- Licence line corrected: the model is under the MiniMax-Music3 Community License; Apache-2.0 is the tag of the Comfy-Org repackage.
- New samples and `samples/workflow.png`; the v1.0.0 samples were renamed `v1.0.0-rtx3060-*.mp3` and moved to `source/`, together with the v1.0.1 file.
## v1.0.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, inputs, seed, tiled_decode, model pickers, sampler settings, tips, attention launch flags, Tested on.
- Checked against the ComfyUI 0.45.3 node list: all nodes core. Not run on 0.45.3.
- v1.0.0 file moved to `source/`.
## v1.0.0
- One file: caption + lyrics to mp3, int8 DiT. Core nodes only (ComfyUI 0.42+). Tested on the RTX 3060 (ComfyUI 0.43.1).

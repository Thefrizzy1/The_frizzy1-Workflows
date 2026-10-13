# Changelog — MiniMax H3 Ultimate · 12 GB
## v2.3.0
- **Extend keeps the clip's sound**: the clip's last 0.9 s of audio go into the H3 guide with its last 22 frames (core `TrimAudioDuration` + `Add Guide for MiniMax H3`), so the sound doesn't jump at the join. New switch **Extend: keep the clip's sound** (on by default, off for silent clips).
- Tested on the RTX 3060 (ComfyUI 0.39.2, 0.4 MP, 5 s): every mode validated; Extend 3 min 51 s–3 min 53 s with the sound, 3 min 31 s–3 min 33 s without. Music test: first 0.9 s envelope match 0.961 on vs -0.016 off.
- How-to note: long videos = run Extend again on the result.
- v2.2.0 kept in `source/`.

## v2.2.0
- **Inputs start bypassed**, so T2V runs right after loading, without any image or video. Before, ComfyUI checked the file of every input loader before a run, also in modes that never read it, so T2V failed when the example files weren't there.
- Un-bypass (Ctrl+B) only the inputs your mode uses and keep everything you are not using bypassed (How to use note + README).
- If the mode needs the First frame, Last frame or Video and it is still bypassed, the run stops at a "Needs ..." node (3 s, before any model loads) instead of quietly making a T2V. Core nodes only (Switch + RepeatImageBatch / GetVideoComponents).
- **Your LoRAs:** two LoRA slots on the node (core LoRA loaders, strength 0 = off).
- The node's input sockets are named after their inputs (First frame, Last frame, ...) instead of on_true_1, image_2.
- Tested on the RTX 3060: T2V as shipped (all 8 inputs bypassed), 0.4 MP, 5 s: 3 min 00 s from start to finished (models loaded fresh after another job), 864×480, 124 frames, with sound. I2V with the First frame still bypassed: stopped after 3.0 s at "Needs the First frame".
- v2.1.1 kept in `source/`.

## v2.1.1 (day-one fix)
- Extend tested on the RTX 3060: 0.4 MP, 5 s, 4 min 31 s from a cold start, peak VRAM 11.5 GB; the clip continues the input's last 0.9 s.
- The Extend switch moved into the FL2VA path, so the main node has 46 nodes inside again (as in the video).
- README: Quick start, what to download for T2V/I2V only (~42 GB) and what to do with the loaders you skipped, 32 GB system RAM, stay at 0.4 / 0.9 MP (1.5 MP timed out), 0.9 MP times, troubleshooting.
- Same tips in the How to use note inside the workflow.
- v2.1.0 kept in `source/`.

## v2.1.0
- New mode **Extend (continue a clip)**: the video input's last 22 frames are anchored at frame 0 of a new FL2VA clip (MiniMaxH3AddGuide), so H3 continues your clip. Core nodes only (GetVideoComponents, GetImageSize, ImageFromBatch).
- The video input is now shared by ControlNet (pose) and Extend: `Video (ControlNet pose / Extend)`.
- Character swap is linked to the separate [Viggle-Animate (H3)](../viggle-animate-h3) workflow (it needs a node pack; this one stays core-only).
- Not benchmarked yet: the 7 measured modes are unchanged; Extend has no time in the table.
- Previous version kept in `source/The_frizzy1_minimax-h3-ultimate-12gb_v2.0.0.json`.

## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- Previous version kept in `source/The_frizzy1_minimax-h3-ultimate-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: all 7 local H3 modes behind one dropdown, lazy model loading, turbo LoRAs, notes with direct download links.

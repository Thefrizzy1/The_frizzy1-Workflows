# Changelog — MiniMax H3 Ultimate · 12 GB
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

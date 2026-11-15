# Changelog - H3 Relight · 12 GB
## v1.0.1 (2026-11-14)
- How to use note rewritten: inputs, every setting on the H3 Relight node, tips, an attention line, and a Tested on line (adds ComfyUI 0.45.3 on a 24 GB card). Downloads note moved down to make room.
- Graph unchanged (same API graph as v1.0.0). Converts to an API graph for ComfyUI 0.45.3 with no errors; every node is in 0.45.3 core.
- v1.0.0 json moved to `source/`.
## v1.0.0
- Your video + a light sphere + the preset's light text -> the same shot in the new light (MiniMax H3 Ref2VA, ref2v turbo LoRA, 6 steps). Qwen3-VL 8B describes the first frame and adapts the light text to the shot (Sirio Berati's describe + adapt steps, his presets are MIT). Original sound kept.
- One main node with the settings; everything else inside it (subgraphs, colour-coded groups).
- Full HD (1088p) dropdown: Off, Gentle H3 refine (H3 latent upscaler + 3 Regenerate-2K steps from sigma 0.55), RealESRGAN x2. Only the chosen path runs.
- Long clip switch: up to 60 s in 5.2 s passes (core Start Loop / End Loop), same sphere, prompt and seed in every pass, each pass continues from the last 22 frames of the one before. Not GPU-tested yet.
- The API graph ComfyUI makes from the saved file was checked node by node against the graph every RTX 3060 relight test ran (480p and 736p + gentle refine): the same computation. Core nodes only, ComfyUI 0.44+.

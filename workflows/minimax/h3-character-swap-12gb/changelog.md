# Changelog - MiniMax H3 Character Swap · 12 GB
## v1.1.1 (2026-11-14)
- Notes only, the graph is the same as v1.1.0 (ComfyUI makes the identical run graph from both). "How to use" note rewritten: inputs, every setting with its default, tips, the attention launch flags, and a Tested on line (RTX 3060 / ComfyUI 0.39.2, also ComfyUI 0.45.3 on a 24 GB card). Downloads note moved down so the two notes do not overlap.
- Checked on ComfyUI 0.45.3: converts and validates. Full HD (from H3 Relight) not added: see README.
## v1.1.0
- Every model loader is on the main node now (model, both LoRAs, text encoder, both VAEs): pick your files there, also when they sit in a subfolder. Tested on the RTX 3060 exactly as its Run button sends it: van exit → raccoon, 7.0 s, 11 min 46 s.
## v1.0.0
- Video + character picture → the swapped clip with its own sound, the whole clip in 5 s passes (core Start Loop / End Loop nodes, 22-frame overlap). Core nodes only (ComfyUI 0.39+). Tested on the RTX 3060 (ComfyUI 0.39.2).

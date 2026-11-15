# Changelog: LTX-2 GGUF
## v2.0.1 (2026-11-14)
- Notes only, graph unchanged. New "How to use" note on the left of each graph: inputs, main settings, Length and Frame Rate, tips, attention flags, tested-on.
- Downloads note: text encoder and connector go in `text_encoders` (was `clip`), direct links for both VAE files, the optional distill LoRA added. Matches downloads.md.
- Node-pack notes (GGUF, KJNodes): punctuation only.
- Checked on ComfyUI 0.45.3: both files convert and validate (not run there).
- v2.0.0 files moved to `source/`.

## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_ltx2-i2v_v1.5.0.json`.

## v1.5.0 (CivitAI v1.5)
- Current release.
## v1.0.0
- Initial release.

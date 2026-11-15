# Changelog - Qwen Image & Edit 2509 GGUF
## v2.0.1 (2026-11-14)
- New How to use note (left of the graph): what it does, inputs, settings, text to image vs editing steps, tips, attention line, tested-on.
- Model links note renamed Downloads and matched to downloads.md (the files the workflow loads, plus the Edit-2509 GGUF and 4-step LoRA links, both custom node packs).
- Editing/Image switch note now says where the nodes are (inside the subgraph).
- Graph unchanged (same API prompt). Converts and validates on ComfyUI 0.45.3; not run there.
- Previous version kept in `source/The_frizzy1_qwen-image-edit-2509_v2.0.0.json`.

## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_qwen-image-edit-2509_v1.0.0.json`.

## v1.0.0 (CivitAI v1.0)
- Initial release: generation + editing, GGUF, Lightning LoRA support.

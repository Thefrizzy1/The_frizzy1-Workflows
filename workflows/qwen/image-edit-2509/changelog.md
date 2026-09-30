# Changelog — Qwen Image & Edit 2509 GGUF
## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_qwen-image-edit-2509_v1.0.0.json`.

## v1.0.0 (CivitAI v1.0)
- Initial release: generation + editing, GGUF, Lightning LoRA support.

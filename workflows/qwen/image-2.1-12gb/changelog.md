# Changelog — Qwen Image 2.1 · 12 GB
## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_qwen-image-2.1-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: native 2K QUALITY path (40 steps, Comfy Kitchen attention) + bypassed TURBO path (Viggle 6-step LoRA v0.2.1, Viggle's sigma schedule). Core nodes only. Tested on RTX 3060 12 GB.

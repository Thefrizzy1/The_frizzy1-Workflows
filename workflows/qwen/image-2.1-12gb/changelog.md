# Changelog - Qwen Image 2.1 · 12 GB
## v2.0.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, each input on the main node, outputs, how to switch to TURBO (incl. enabling the bottom Save Image), important settings, tips, the attention flags line, and a Tested on list (RTX 3060 + ComfyUI 0.45.3 on a 24 GB card).
- Downloads note: punctuation only, text unchanged.
- Notes that the main node's Seed drives TURBO; the QUALITY seed is inside the node.
- Checked on ComfyUI 0.45.3: all nodes are core, converts and validates. No core swaps needed.
- Previous version kept in `source/The_frizzy1_qwen-image-2.1-12gb_v2.0.0.json`.

## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_qwen-image-2.1-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: native 2K QUALITY path (40 steps, Comfy Kitchen attention) + bypassed TURBO path (Viggle 6-step LoRA v0.2.1, Viggle's sigma schedule). Core nodes only. Tested on RTX 3060 12 GB.

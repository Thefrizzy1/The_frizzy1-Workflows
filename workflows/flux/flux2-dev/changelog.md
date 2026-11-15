# Changelog: Flux.2 Dev GGUF
## v2.0.1 (2026-11-14)
- Notes only, graph unchanged (same run graph as v2.0.0).
- New "How to use" note: what it does, the inputs, settings, tips, attention launch flags, tested-on line.
- "Models and .whl files" note renamed "Downloads" and made to match downloads.md (old Q8_0 / bf16 file names, SageAttention .whl steps removed).
- Recommendation note: removed the MultiGPU virtual VRAM line (there is no MultiGPU node in this graph).
- README: ComfyUI requirement and node list added. Converts and validates on ComfyUI 0.45.3 (not run there).
- Previous version kept in `source/The_frizzy1_flux2-dev-gguf_v2.0.0.json`.

## v2.0.0
- Rebuilt as a subgraph: your inputs and outputs stay outside, one node carries the settings you change most (prompt, seed, steps, size, model file); all steps and the Step groups are inside it, unchanged.
- Previous version kept in `source/The_frizzy1_flux2-dev-gguf_v1.0.0.json`.

## v1.0.0 (CivitAI v1.0)
- Initial release.

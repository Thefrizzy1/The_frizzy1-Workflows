# Changelog · MOSS-Image · 12 GB
## v1.0.1 (2026-11-14)
- Notes only, graph unchanged (except the edit id counter below). All four files renamed to v1.0.1, v1.0.0 files moved to source/.
- "How to use" notes rewritten: what each file does, inputs, the important settings (enhancer and Skip Layer Guidance switches, sampler settings, MoGe `output`), tips, measured RTX 3060 numbers, Tested on line and a faster-attention line. Downloads notes moved down so they do not overlap.
- Text to image note: peak VRAM corrected to 11.3 GB (the README's measured value).
- Control: note and README now say the MoGe `output` that actually runs is the outer node's setting (*depth* as saved), not the *mask* inside the subgraph.
- Edit file: link id counter (last_link_id) raised to the highest link id. Nothing else in any graph changed.
- Checked on ComfyUI 0.45.3: every node is in core, not run there. Still needs ComfyUI 0.43+ and no custom nodes.

## v1.0.0
- Four files: text to image, layout (boxes), edit (LoRA), control (MoGe ViT-L). w4a8 text encoder. Core nodes only (ComfyUI 0.43+). Tested on the RTX 3060 (ComfyUI 0.43.1).

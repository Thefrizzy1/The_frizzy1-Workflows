# Changelog · MOSS-Image · 12 GB
## v1.0.2 (2026-11-24)
- All four files rebuilt flat (no subgraphs) in numbered groups: 1 · Your inputs (also App mode), 2 · Models, then prompt, sampling, save. Plain-language input titles, a "How to use · v1.0.2" and a "Downloads + requirements" note in every file. v1.0.1 files moved to source/.
- Same settings as v1.0.1 / Comfy's templates (steps, CFG, samplers, enhancer and Skip Layer Guidance defaults, edit and control settings).
- Prompt enhancer: `TextGenerate` (deprecated in ComfyUI 0.45.3) replaced by `TextGenerateV2` with the same values.
- Edit and control open with `example.png` (ships with ComfyUI) instead of template pictures a fresh install does not have, with prompts written for it.
- Control: the map is *depth* (the template's; the v1.0.1 outer node was set to *mask* although the note said depth). The unwired Painter is gone.
- Seeds fixed. Text to image (seed 1) and layout (seed 7) give the README pictures on the first Run. The control sample was made with other inputs (the standard full-body photo and an astronaut prompt), and edit has no README picture.
- Run on ComfyUI 0.45.3 (lab server, 24 GB card, 10 GiB budget): all four files. Not run on a 12 GB card yet; the RTX 3060 numbers in the README are v1.0.1's.
- Samples replaced (text to image, layout poster, control; no edit sample); graph screenshots of all four files added.
- Control note: says the depth/mask switch is in group 3 on purpose (App mode does not show it). Layout: the Boxes title says the editor needs Nodes 2.0. models.json: edit LoRA, control LoRA and MoGe marked not required (only one file needs each).

## v1.0.1 (2026-11-14)
- Notes only, graph unchanged (except the edit id counter below). All four files renamed to v1.0.1, v1.0.0 files moved to source/.
- "How to use" notes rewritten: what each file does, inputs, the important settings (enhancer and Skip Layer Guidance switches, sampler settings, MoGe `output`), tips, measured RTX 3060 numbers, Tested on line and a faster-attention line. Downloads notes moved down so they do not overlap.
- Text to image note: peak VRAM corrected to 11.3 GB (the README's measured value).
- Control: note and README now say the MoGe `output` that actually runs is the outer node's setting (*depth* as saved), not the *mask* inside the subgraph.
- Edit file: link id counter (last_link_id) raised to the highest link id. Nothing else in any graph changed.
- Checked on ComfyUI 0.45.3: every node is in core, not run there. Still needs ComfyUI 0.43+ and no custom nodes.

## v1.0.0
- Four files: text to image, layout (boxes), edit (LoRA), control (MoGe ViT-L). w4a8 text encoder. Core nodes only (ComfyUI 0.43+). Tested on the RTX 3060 (ComfyUI 0.43.1).

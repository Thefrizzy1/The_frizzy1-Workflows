# Changelog - Image to 3D Ultimate · 12 GB
## v2.0.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, the input, every setting on the node (Model, Texture size, Seed, model files), where the .glb is saved, tips, an attention line and a Tested on line. Colour legend fixed for this workflow.
- Note text also stored in the note's named-widget field so both copies match.
- Downloads note moved down so the two notes do not overlap.
- Checked on ComfyUI 0.45.3: all nodes are core and the graph converts and validates on 0.45.3 (not run on 0.45.3).
- Previous version kept in `source/The_frizzy1_image-to-3d-ultimate-12gb_v2.0.0.json`.

## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- Previous version kept in `source/The_frizzy1_image-to-3d-ultimate-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: Pixal3D / TRELLIS.2 image-to-mesh behind one dropdown.

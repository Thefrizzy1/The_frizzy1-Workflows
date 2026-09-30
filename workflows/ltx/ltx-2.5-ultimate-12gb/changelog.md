# Changelog — LTX 2.5 Ultimate · 12 GB
## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- New **Keep the pose video's audio** switch for Pose mode (lip-sync; the ia2v method: 84% timing against my mouth on my android clip).
- Previous version kept in `source/The_frizzy1_ltx-2.5-ultimate-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: 4 LTX 2.5 modes behind one dropdown, pose via IC-LoRA Union + SDPose.

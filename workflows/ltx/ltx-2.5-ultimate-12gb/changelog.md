# Changelog — LTX 2.5 Ultimate · 12 GB
## v3.1.1
- New modes: **VFX: video to video** with a VFX LoRA picker (Lightricks LTX-2.5 Creative Lab: clean plate, day to night, water, deblur, decompression, colorization, alpha matte, restore, refine details, pixel upscaler x2), **VFX: Layout to Render**, **VFX: Ingredients**, **I2V + Cinemagraph**, **I2V + Slow motion**.
- **VFX LoRA strength** on the main node, and the settings from my tests in the notes (Clean Plate 1.2 + name the person, Colorization 1.3, Water at 1280x704, Slow motion 0.2).
- **Keep the source video's audio** works in VFX video to video too.
- Needs ComfyUI 0.44.0+: it added a chroma_subsampling setting to the core CreateVideo node, and v3.1.1 sets it to auto.
- Fixed two resize links in First + last frame that made ComfyUI refuse the saved file (unpublished v3.0.0 only).
- Every mode run from the saved file on an RTX 3060 (README). Ingredients runs but keeps the reference sheet's grid.
- Previous version kept in `source/The_frizzy1_ltx-2.5-ultimate-12gb_v2.0.0.json`.

## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- New **Keep the pose video's audio** switch for Pose mode (lip-sync; the ia2v method: 84% timing against my mouth on my android clip).
- Previous version kept in `source/The_frizzy1_ltx-2.5-ultimate-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: 4 LTX 2.5 modes behind one dropdown, pose via IC-LoRA Union + SDPose.

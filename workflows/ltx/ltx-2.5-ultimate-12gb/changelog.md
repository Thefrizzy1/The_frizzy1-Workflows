# Changelog — LTX 2.5 Ultimate · 12 GB
## v3.2.0
- New switch **LTX x2 upscale (2 stages)**, on by default (= v3.1.1). Off: T2V / I2V / Cinemagraph / Slow motion stop after stage 1, the latent upscaler and stage 2 never run. About 2x faster on the RTX 3060, half the size.
- New switch **RelayVSR x2**, off by default: upscales the finished video of any mode x2 with ComfyUI's built-in RelayVSR (1 step, cfg 1, VSR Decode), like the official RelayVSR template. Full HD 1920x1024 from a 960x512 run in 1:41.
- Needs ComfyUI 0.45.0+ (the RelayVSR nodes). On 0.44 use `source/The_frizzy1_ltx-2.5-ultimate-12gb_v3.1.1.json`.
- Built by patching the tested v3.1.1 file, so every v3.1.1 link is unchanged. Every new combination run from the saved file on an RTX 3060 (README).
- Previous version kept in `source/The_frizzy1_ltx-2.5-ultimate-12gb_v3.1.1.json`.

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

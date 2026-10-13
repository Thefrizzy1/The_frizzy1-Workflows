# Changelog — Krea 2 Ultimate · 12 GB
## v2.1.0
- New **Model** switch: Krea 2 Turbo or **Kroma** (lodestones' Krea 2 fine-tune, v0.3.1 Turbo OPD, w4a8 file). Only the picked model loads; text encoder, VAE, settings, modes and style LoRAs are shared.
- Kroma download links in the Downloads note and on the loader. Tested in both models and both modes on the RTX 3060 (ComfyUI 0.39.2).
- Previous version kept in `source/The_frizzy1_krea-2-ultimate-12gb_v2.0.0.json`.

## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- One seed for both modes (v1 had one per mode).
- Previous version kept in `source/The_frizzy1_krea-2-ultimate-12gb_v1.0.0.json`.

## v1.0.0
- Initial release: T2I + style reference behind one dropdown, style LoRA picker, prompt enhancer toggle.

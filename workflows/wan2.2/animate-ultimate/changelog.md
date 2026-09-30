# Changelog — Wan Animate Ultimate
## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- Model choice is now: Wan 2.2 Animate GGUF (default; best lip-sync) or Wan Animate 2 int8.
- New **Face video** switch (on = the mouth follows the driving video: 95% timing against my mouth with it, 48% without, same clip).
- Width, height, frames and seed are now one setting each for both models.
- **Fix:** the relight LoRA never loaded in v1.0.0. Kijai's file has no `diffusion_model.` prefix, so native ComfyUI skipped every key ("lora key not loaded"). v2 uses Comfy-Org's repackaged copy (`wan2.2_animate_14B_relight_lora_bf16.safetensors`, same 960 weights).
- Previous version kept in `source/The_frizzy1_wan-animate-ultimate_v1.0.0.json`.

## v1.0.0
- Initial release: native rebuild of Wan 2.2 Animate + Wan Animate 2, one dropdown, side-by-side output, fixed download links.

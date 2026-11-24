# Changelog - ERNIE-Image Turbo
## v1.0.0 (2026-11-24)
- Initial release: built from the ComfyUI template `image_ernie_image_turbo` (one subgraph node) and laid out flat in six numbered groups with the inputs in group 1. Core nodes only.
- Same files and settings as the template: `ernie-image-turbo.safetensors` (bf16), `ministral-3-3b.safetensors`, `ernie-image-prompt-enhancer.safetensors`, `flux2-vae.safetensors`; 8 steps, CFG 1, euler / simple; prompt enhancer on.
- Changes to the template: width and height became a Size input (shape + megapixels); the seed is `fixed` instead of `randomize`; the deprecated `TextGenerate` node is replaced by `TextGenerateV2` (same code in ComfyUI 0.45.3, pixel-identical pictures).
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 29 s (1024x1024, enhancer on, first run) and 14 s (1360x768, enhancer off) in a 12 GiB VRAM budget, 12.2 GiB peak; same pictures in a 10 GiB budget (10.2 GiB). Not verified on a 12 GB card.

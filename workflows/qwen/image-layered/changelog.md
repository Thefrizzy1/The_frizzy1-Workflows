# Changelog - Qwen-Image-Layered
## v1.0.0 (2026-11-24)
- Initial release, built from the ComfyUI template `image_qwen_image_layered`: its "Image to Layers" subgraph laid out flat in six numbered groups with the inputs in group 1. Core nodes only.
- Loads the Comfy-Org fp8mixed model (20.5 GB) instead of the template's bf16 file (40.9 GB), as the template's own note suggests for lower VRAM.
- Sampler settings are the template's (20 steps, CFG 2.5, euler / simple, shift 1, long side 640, 2 layers). The seed is fixed instead of randomized, and the description starts empty instead of describing the template's picture.
- The template's bypassed "Text to Layers" subgraph is not included.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 78 s for 2 layers, 102 s for 4 layers. In 12 and 10 GiB `--reserve-vram` budgets the layers were pixel-identical, peak 13.2 / 11.1 GiB whole GPU. Not verified on a 12 GB card.

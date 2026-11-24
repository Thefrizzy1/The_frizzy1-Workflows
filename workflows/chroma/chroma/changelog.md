# Changelog - Chroma1-HD
## v1.0.0 (2026-11-24)
- Initial release: built from the ComfyUI template `image_chroma_text_to_image` and restructured into five numbered groups with the inputs in group 1. Core nodes only.
- Same files and settings as the template: `Chroma1-HD-fp8mixed.safetensors`, `t5xxl_fp8_e4m3fn_scaled.safetensors`, `ae.safetensors`, euler / beta, 26 steps, CFG 3.5, flow shift 1, T5 padding 0 / 0, the template's prompt and negative prompt.
- Changes to the template: the fixed 1024x1024 size became a Size input (shape + megapixels, multiple 16), the seed moved to group 1 with default 24112026 (on `fixed`, so the first Run gives the README picture), pictures go to `output/Chroma/`, the template notes became the How to use and Downloads notes.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 1024x1024 in 46 to 47 s, 16:9 (1360x768) in 47 s. In a 10 GiB `--reserve-vram` budget: 49 to 50 s, 10.1 GiB process / 11.0 GiB whole-GPU peak, identical pictures. Not verified on a 12 GB card.

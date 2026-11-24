# Changelog - Capybara Image Edit
## v1.0.0 (2026-11-24)
- Initial release, built from the ComfyUI template `Image_capybara_v0_1_image_edit`, taken out of its subgraph and restructured into numbered groups with every input in group 1 and two notes. Core nodes only.
- The picture keeps its shape: it is resized to 1 megapixel with sides rounded to 16 (a 1776x1184 picture gives 1248x832). The template centre-crops every picture to 1024x1024.
- Loads the fp8 Qwen 2.5 VL text encoder (9.38 GB) instead of the template's bf16 file (16.58 GB).
- Steps 20, CFG 6, shift 7, euler / simple, as in the template. The authors' edit settings (50 steps, CFG 1, shift 5) were tried on both samples and left the forest edit half done.
- The seed is fixed (24112026), so the same picture and instruction give the same result each run; the template randomizes it.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, also in 12 and 10 GiB `--reserve-vram` budgets. Not verified on a 12 GB card.

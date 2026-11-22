# Changelog - SDXL
## v1.0.0 (2026-11-22)
- Initial release: built from the ComfyUI template `image_sdxl_simple` and restructured into five numbered groups with the inputs in group 1. Core nodes only.
- Same model and sampler settings as the template: `sd_xl_base_1.0.safetensors`, 25 steps, CFG 7, dpmpp_2m / karras, 1024x1024.
- Changes to the template: the fixed 1024x1024 size became a Size input (shape + megapixels), there is a new default prompt, and the negative prompt is the template's without `color, colored` (those two words belonged to the template's marble statue prompt).
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 1024x1024 in 9 to 10 s (11 s on the first run), whole-GPU peak 7.6 to 10.0 GiB. Not verified on a 12 GB card.

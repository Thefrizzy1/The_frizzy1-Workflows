# Changelog - Anima
## v1.0.0 (2026-11-22)
- Initial release: built from the ComfyUI template `image_anima_base_v1` and restructured into numbered groups with the inputs in group 1. Core nodes only.
- Same models and sampler settings as the template: Anima Base v1.0, 30 steps, CFG 4, euler / simple; the Turbo switch loads the Turbo LoRA v0.2 at 8 steps, CFG 1.
- Two changes to the template's defaults: a new default prompt, and the negative prompt is the model page's recommended list (not the template's) plus `border, white border`. With the model page's list, 3 of 8 test pictures had a white frame; with the two tags the same 3 pictures had none.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 1024x1024 in 21 to 23 s (Turbo: about 4 s), whole-GPU peak 6.3 to 7.4 GiB. Not verified on a 12 GB card.

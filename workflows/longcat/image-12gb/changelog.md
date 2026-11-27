# Changelog - LongCat-Image · 12 GB
## v1.0.0 (2026-11-25)
- Initial release: text to image and Edit Turbo, built from the ComfyUI templates `image_longcat_text_to_image` and `image_longcat_image_edit`, taken out of their subgraphs into numbered groups with two notes each. Core nodes only.
- Text to image: the template's 20 steps, CFG 4, CFG norm 1. `text` and `logo` were removed from the template's negative prompt, and the FluxGuidance nodes were left out (ComfyUI's LongCat code ignores that value). Default shape 3:2, sides a multiple of 16 (template: 1:1, 8).
- Edit: loads Edit-Turbo at the authors' 8 steps, CFG 1 (template: the Edit model, 50 steps, CFG 4.5). The resized picture is the reference through `ReferenceLatent`, so its sides fit 16 pixels (template: the text encoder node makes its own).
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, also in 12 and 10 GiB `--reserve-vram` budgets. Not verified on a 12 GB card.

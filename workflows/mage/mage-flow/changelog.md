# Changelog - Mage-Flow
## v1.0.0 (2026-11-24)
- Initial release: built from the ComfyUI template `image_mage_flow_t2i_int8`, taken out of its subgraph and laid out in five numbered groups with the inputs in group 1. Core nodes only.
- Same files, CFG (5), sampler (euler / simple), size input (ResolutionSelector, 1024x1024) and default prompt as the template.
- Changes to the template: 20 steps instead of 30 (the authors' step count for this RL-aligned file; side by side on 3 pictures from 2 prompts they were nearly the same and took 8 s instead of 12 s), the seed is fixed at 24112026 instead of random, and the picture is saved to `output/Mage-Flow/`.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 8 to 9 s per picture once loaded, 11 s on a fresh start; also run capped to 12 and 10 GiB budgets with pixel-identical pictures. Not verified on a 12 GB card.

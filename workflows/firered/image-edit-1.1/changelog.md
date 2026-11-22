# Changelog - FireRed Image Edit 1.1
## v1.0.0 (2026-11-22)
- Initial release, built from the ComfyUI template `image_firered_image_edit1_1` and restructured into numbered groups with the inputs in group 1. Core nodes only.
- Loads a 20.6 GB int8 convrot model instead of the template's 40.9 GB file. The Lightning LoRA is the template's (`FireRed-Image-Edit-1.0-Lightning-8steps-v1.0`): the newer 1.1 LoRA v1.2 put a woven pattern over foliage in the three-picture test (8 of 8 settings), this one did not (3 of 3 seeds).
- Lightning is on by default (the template has it off): 8 steps took 19 to 22 s on the test card, 40 steps at CFG 4 took 3 min 10 s.
- Pictures are resized to sides that are a multiple of 16 and added with Set Reference Latent. With the template's wiring the 16:9 test picture got a skin-coloured strip on the right edge in 8 of 8 runs; with this wiring in none.
- Picture 2 and Picture 3 are switched on with their own inputs instead of being wired by hand.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, no VRAM limit set. Not verified on a 12 GB card.

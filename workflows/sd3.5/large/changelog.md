# Changelog - Stable Diffusion 3.5 Large
## v1.0.0 (2026-11-24)
- Initial release: built from the ComfyUI template `sd3.5_simple_example` and restructured into five numbered groups with the inputs in group 1. Core nodes only.
- Same model, prompt and sampler settings as the template: `sd3.5_large_fp8_scaled.safetensors`, 20 steps, CFG 4.01, euler / sgm_uniform, empty negative prompt, 1024x1024.
- Changes to the template: the fixed 1024x1024 size became a Size input (shape + megapixels), the seed is fixed at 24112026 instead of random, and pictures go to `output/SD3.5/`.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB: 1024x1024 in 23 s (24 s with the model load), whole-GPU peak 15.4 to 17.4 GiB; in a 10 GiB `--reserve-vram` budget 24 to 25 s at 11.1 GiB whole GPU, byte-identical pictures. Not verified on a 12 GB card.

# Changelog - Bernini-R Image Edit
## v1.0.0 (2026-11-22)
- Initial release, built from the ComfyUI template `video_bernini_r_image_editing`: the subgraph laid out flat in numbered groups with the inputs in group 1. Core nodes only.
- Loads the Comfy-Org int8 convrot files (14.5 GB each) instead of the template's fp8 files (15.6 GB each), and `wan_2.1_vae.safetensors` from Comfy-Org instead of `Wan2_1_VAE_bf16.safetensors` from Kijai.
- Turbo is on by default, as in the template (6 steps, CFG 1, lightx2v LoRA at 3 and 1.5). On the test card Turbo took 16 to 24 s per picture, Turbo off (40 steps, CFG 5) 3 min 23 s to 4 min 19 s.
- The picture is trimmed to sides that are a multiple of 16 after the long-side resize. With the template's wiring a 1368x768 picture came back as 1280x712; here it goes in and comes out as 1280x704.
- The template's task menu is replaced by the fixed image editing system prompt. A reference picture can be switched on with one input.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB. Five runs with `--reserve-vram 13.5` peaked at 11.3 to 11.5 GiB (whole GPU). Not verified on a 12 GB card.

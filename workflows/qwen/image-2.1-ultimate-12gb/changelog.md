# Changelog — Qwen Image 2.1 Ultimate · 12 GB
## v2.0.0
- First Ultimate release: text to image, edit (1–3 images), ControlNet pose / depth / edges (Fun ControlNet Union, core since ComfyUI 0.38), Turbo on/off. Core nodes only.
- ControlNet modes run at their own size (ControlNet megapixels, default 1): at 2K the ControlNet broke in my test.
- Inputs ship bypassed; "Needs …" checks stop a run whose mode needs a bypassed input.
- Tested in every mode on the RTX 3060 (ComfyUI 0.39.2).

# Changelog - FLUX 3 Klein · 12 GB
## v1.0.1 (2026-11-14)
- Notes only, graph unchanged. Rewrote the "How to use" note in both files: inputs, important settings, tips, attention flags, tested-on line. Moved the Downloads note down so the notes do not overlap.
- Fixed the text to image note: peak VRAM 11.2 GB (11.4 GB was the edit file's number).
- Checked on ComfyUI 0.45.3: both files convert and validate, every node is core. Not run on 0.45.3 yet.
- v1.0.0 files moved to source/.

## v1.0.0
- Two files: text to image (optional bounding boxes) and edit (image 1 + up to 3 references), both with BFL's prompt upsampler. Core nodes only (ComfyUI 0.41+). Tested on the RTX 3060 (ComfyUI 0.43.1).

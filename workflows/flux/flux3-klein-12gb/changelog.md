# Changelog - FLUX 3 Klein · 12 GB
## v2.0.0 (2026-11-24)
- Text to image is **one node** now (a single subgraph, the two v1.0.2 subgraphs merged): prompt, shape, megapixels, upsampler on/off, seed, steps, alpha and the model files on the outside, App mode set, second output shows the upsampled prompt. The optional box editor stays beside it; its canvas no longer follows the size, set its width and height yourself. v1.0.2 moved to source/.
- `TextGenerate` (deprecated in ComfyUI 0.45.3) replaced by `TextGenerateV2` with the same values. Same upsampled prompt and same pixels as v1.0.2 in the check. Seed is fixed now.
- RTX 3060 12 GB, ComfyUI 0.45.3: 31 s with the models unloaded first, 27 s for a new prompt, 13 s for a new seed, 11.3 to 11.4 GiB peak VRAM.
- No Turbo mode: 8 and 4 steps were tested and lose too much, the one turbo LoRA needs a custom node and the base model (see README).
- Edit files unchanged.

## v1.1.0 (2026-11-24)
- New file `The_frizzy1_flux3-klein-edit-lowvram_v1.1.0.json`: edit one photo without the prompt upsampler, 3 files (11.0 GB instead of 17.7 GB). BFL's `flux3_klein_int8_i2i` template rebuilt flat in the house layout (numbered groups, inputs in group 1 for App mode, How to use + Downloads notes). Same sampling as the template: 16 steps, CFG 1, euler / simple, shift 2.77 (alpha 16); output keeps the photo's shape at 1 MP.
- Ran on ComfyUI 0.45.3 inside 6, 8 and 12 GiB budgets (lab card capped with `--reserve-vram`): 15 to 17 s per picture, ComfyUI peaked at 5.93 / 7.93 / 10.80 GiB. Not run on a real 6, 8 or 12 GB card.
- README: why there is no GGUF file (needs a custom node) and no TrueRelight LoRA (core ComfyUI 0.45.3 does not load its keys).
- Samples: `edit-lowvram-01.webp`, `edit-lowvram-02.webp`, and `workflow.png` (ComfyUI screenshot of the new file).
- Download total corrected to 17.7 GB in README and downloads.md (the four files add up to 17.75 GB; it said 17.8).
- t2i and edit files v1.0.2: notes only, graph unchanged. The Downloads note now says Total 17.7 GB (was 17.8). Not run on 0.45.3. v1.0.1 files moved to source/.

## v1.0.1 (2026-11-14)
- Notes only, graph unchanged. Rewrote the "How to use" note in both files: inputs, important settings, tips, attention flags, tested-on line. Moved the Downloads note down so the notes do not overlap.
- Fixed the text to image note: peak VRAM 11.2 GB (11.4 GB was the edit file's number).
- Checked on ComfyUI 0.45.3: both files convert and validate, every node is core. Not run on 0.45.3 yet.
- v1.0.0 files moved to source/.

## v1.0.0
- Two files: text to image (optional bounding boxes) and edit (image 1 + up to 3 references), both with BFL's prompt upsampler. Core nodes only (ComfyUI 0.41+). Tested on the RTX 3060 (ComfyUI 0.43.1).

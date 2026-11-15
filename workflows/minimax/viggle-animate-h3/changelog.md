# Changelog - Viggle-Animate (MiniMax H3) · 12 GB
## v2.0.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, inputs, every setting on the node, tips, measured RTX 3060 numbers from the README, "Tested on" line, and an attention line (--use-sage-attention / --use-ck-attention). Downloads note moved down so the notes do not overlap.
- Removed the unmeasured 7-step time from the note.
- README: core node list, ComfyUI 0.45.3 check line, step count in the summary corrected (3 steps Fast, 7 optional).
- Previous version kept in `source/The_frizzy1_viggle-animate-h3_v2.0.0.json`.

## v2.0.0
- Rebuilt with ComfyUI subgraphs: one node with the settings you change (mode / model version switches, prompt, size, length, seed, model files); every step is inside it in colour-coded groups (blue models, green inputs, purple prompt, orange sampling, yellow decode, grey switches), one nested node per model path.
- Every loader carries its download link, so ComfyUI's missing-models panel offers a Download button per file.
- New **Steps** choice: Fast (3 steps) or the node pack's 7-step example.
- Previous version kept in `source/The_frizzy1_viggle-animate-h3_v1.0.0.json`.

## v1.0.0
- Initial release: native-first Viggle-Animate workflow: 4-step DMD, driving audio kept, notes with direct download links.

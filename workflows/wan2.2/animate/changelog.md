# Changelog: Wan 2.2 Animate

Versions follow the repository [naming standard](../../../docs/NAMING.md). CivitAI labels in parentheses.

## v1.2.1 (2026-11-14)
- New How to use note on the far left: what it does, the inputs, Width / Height / Length / Loop Extend / Seed, sampler and output settings, Move vs Mix mode, tips, an attention line and a Tested on line.
- Model links note renamed Downloads and rewritten to match downloads.md (the GGUF files this graph loads, the speed LoRA and VAE to pick).
- Custom nodes note lists all eight packs the graph uses (it listed three).
- Looping note: fixed the formula (frames read = Length x (Loop Extend + 1)) and finished the example.
- Graph unchanged (same API graph as v1.2.0). No node swaps: the graph needs custom packs and model files that are not on the 0.45.3 check server, so a swap could not be tested.
- v1.2.0 json moved to `source/`.

## v1.2.0 (CivitAI v1.2)
- Added looping mechanism for unlimited video length.
- Moved the points editor out of the subgraph.
- Better graph organisation.
- Dropped the IAMCCS-nodes dependency (only needed on v1.0.0).

## v1.0.0 (CivitAI v1.0)
- Initial release: Wan 2.2 Animate 14B in GGUF, reference image + driving video.

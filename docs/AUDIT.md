# Verification Audit & Open Issues

A running log of what was checked, what was confirmed from primary sources, and what still needs a human.
"Primary source" = the workflow `.json` itself (read node-by-node) and the creator's own Hugging Face READMEs.

_Last run: 2026-07-31._

---

## Method

1. Listed every `The-frizzy1` repo on Hugging Face (11 model repos; 1 private, unrelated).
2. Downloaded every available workflow `.json` (raw + unzipped the LFS zips; extracted the Hunyuan workflow
   embedded in its PNG's `tEXt` chunk).
3. Parsed each workflow's nodes and pulled out every model filename (`.gguf/.safetensors/.pth/...`).
4. Cross-referenced those filenames against the download links in each repo's README.

Result: **all 12** workflows are fully model-verified from their JSON (the 4 CivitAI-only ones were supplied as zips and extracted).

---

## ⚠️ Issues found

### 1. Hunyuan workflow loaded a Flux model — ✅ FIXED (v1.1.1)
The shipped Hunyuan Video workflow's diffusion loader referenced **`flux1-dev-Q5_K_S.gguf`** (a leftover),
while the README correctly says to use **`fast-hunyuan-video-t2v-720p-Q5_K_M.gguf`**. **Resolved:** the loader
was repointed to the Fast Hunyuan GGUF and saved as `The_frizzy1_hunyuan-video-lowvram_v1.1.1.json`; the
untouched original is preserved in that folder's `source/`.

### 2. Four CivitAI-only workflows — ✅ RESOLVED (JSONs received)
`Flux.2 Dev GGUF`, `Wan 2.2 AIO Rapid`, `Z-Image Turbo GGUF` and `AI Audio Maker` had no HF mirror; their
workflow zips were supplied and extracted. **All four are now model-verified from their JSON** and have their
own workflow folders. Remaining nicety: confirm the exact host repos for a couple of Flux.2 / Z-Image
filenames (the filenames themselves are verified).

### 3. Wan 2.2 AIO Rapid vs the "Custom Advanced VACE Node"
The HF `Custom-Advanced-VACE-Node` repo describes a "Rapid AIO I2V (First → Last Frame)" node built for the
Phr00t workflow. Confirm whether this node is what the CivitAI "WAN 2.2 AIO Rapid" page depends on, and link
them explicitly.

---

## Version reconciliation
CivitAI labels were normalised to semver — see [NAMING.md](NAMING.md). No conflicts beyond inconsistent
labelling; the mapping table is the source of truth.

## Links checked
All Hugging Face repo URLs in the READMEs resolved during listing. External model-host links
(QuantStack, city96, Kijai, Comfy-Org, calcuis, Lightricks, unsloth, bullerwins) are reproduced as published
by the creator; a full HTTP link-check pass is still **TODO** and should be automated (see below).

## Recommended next automation
- A `scripts/check-links.sh` that HEAD-requests every URL in `docs/DOWNLOADS.md` and reports dead ones.
- A `scripts/extract-models.py` (the parser used here) committed to the repo so re-verifying a new workflow is one command.

---

## Confirmed-good summary

| Workflow | Models verified from JSON? |
|---|---|
| Wan 2.1 GGUF Low-VRAM | ✅ (6 variants) |
| Wan 2.2 GGUF Low-VRAM | ✅ (4 variants) |
| Wan 2.2 Animate | ✅ (2 variants) |
| Flux Kontext GGUF | ✅ |
| Qwen Image & Edit 2509 | ✅ |
| Hunyuan Video Low-VRAM | ✅ — but see issue #1 |
| LTX-2 GGUF | ✅ |
| LTX-2.3 Ultimate | ✅ |
| Wan 2.1 FLF2V | ✅ (FLF json from the Wan 2.1 pack) |
| Flux.2 Dev GGUF | ✅ |
| Z-Image Turbo GGUF | ✅ |
| Wan 2.2 AIO Rapid | ✅ (single mega-AIO GGUF) |
| AI Audio Maker | ✅ (MMAudio stack) |

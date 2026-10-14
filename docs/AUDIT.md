# Verification Audit & Open Issues

A running log of what was checked, what was confirmed from primary sources, and what still needs a human.
"Primary source" = the workflow `.json` itself (read node-by-node) and the model cards on Hugging Face.

_Last run: 2026-10-14 — 23 workflows, `python scripts/check_repo.py --links`: 0 problems, 135 links, 5 gated._

---

## How to re-check (one command)

```bash
python scripts/check_repo.py --links
```

For every workflow folder it checks: every model file the `.json` loads is in `models.json` and `downloads.md` with
the exact name; `models.json` requires nothing the `.json` never loads; the custom node packs the `.json` uses (the
node-pack ids ComfyUI saves in the file) are in `models.json`; the version in the `.json` name = the root README = the
changelog; the README names its `.json`; and with `--links` every download link answers. Documented exceptions
(helper files the node packs download themselves, one renamed LoRA) are in `scripts/check_allow.json`.

---

## 2026-10-14 audit (23 workflows)

**Found and fixed:**
1. **Root README, `index.html`, `docs/DOWNLOADS.md`, `docs/COMPATIBILITY.md`, `models/README.md` stopped at the first 13
   workflows** — the 10 newer 12 GB ones (H3, LTX 2.5, Viggle-Animate, Wan Animate Ultimate, Qwen 2.1 ×2, Krea 2, Ming,
   Image to 3D, YuE2) were missing. All five now cover all 23; `docs/DOWNLOADS.md` is generated from the `models.json`
   files so it can't drift again.
2. **`models.json` didn't match the `.json` in the older workflows**, so `frizzy.py get` downloaded files the loaders
   never ask for (e.g. Wan 2.1 loads `t5xxl_um_fp8_e4m3fn_scaled` + `clip_vision_h_fp8_e4m3fn`, the manifest fetched
   Comfy's `umt5_xxl…` + `clip_vision_h`; Wan 2.2 GGUF fetched QuantStack-named experts while the `.json` loads
   bullerwins' names; LTX-2 fetched the dev model, the `.json` loads the distilled one). 13 manifests corrected; where a
   source repo renamed a file, the tool now saves it under the name the workflow loads.
3. **Vague "grab by hand" entries** (LTX-2/2.3 VAEs, LoRAs, text encoders; Flux.2 encoder + VAE; Z-Image; AIO Rapid) →
   exact direct links.
4. **Custom node packs missing from the manifests** (read from the node-pack ids in each `.json`): e.g. Flux.2 / Z-Image
   need KJNodes, LTX-2.3 needs Impact Pack + Easy-Use, Wan 2.2 Animate needs essentials + Custom-Scripts +
   Frame-Interpolation, Kontext uses calcuis' `gguf` (not ComfyUI-GGUF) + TeaCache + essentials, Viggle-Animate needs its
   own pack. Unused ones removed (WanVideoWrapper from Wan 2.1).
5. **Wan Animate Ultimate** marked both GGUF files and the GGUF-mode helpers as required → now optional (`--optional`),
   so the default download is the Wan Animate 2 path only.
6. **Dead link:** `Wan2.1-T2V-1.3B-F16.gguf` (renamed on calcuis/wan-1.3b-gguf) → fixed.
7. **Wrong licenses:** LTX-2 / 2.3 said Apache-2.0 (the cards say LTX-2 Community License); Wan 2.2 Animate said OpenRAIL
   (Apache-2.0); MMAudio, Flux.2, Z-Image said "check the card". All read from the cards → [models/README.md](../models/README.md#licenses-read-before-commercial-use).
8. **`frizzy.py` only looked in `ComfyUI/models/<folder>/`** → it now also looks in subfolders and in the folders from
   `extra_model_paths.yaml` (and ComfyUI Desktop's config), so models you already have aren't downloaded twice.
9. Nine READMEs didn't name their `.json`; `index.html` had three stale versions (Flux.2, Qwen 2509, LTX-2).

**Open (documented, not errors):**
- LTX 2.5's files are **gated**: accept Lightricks' terms on the model page, set `HF_TOKEN`.
- Wan 2.2 Animate (older) loads a renamed speed LoRA with no public source — the manifest gives the substitute to pick.
- Wan 2.2 GGUF: the TI2V-5B files are listed as optional; neither `.json` loads them.
- Flux Kontext's LoRA stack holds three of my own LoRAs — use any Flux LoRA or switch the slots off.
- VRAM for Flux.2 / Z-Image / AI Audio / AIO Rapid is not measured here.

---

## 2026-07-31 audit (first 12 workflows)

1. Listed every `The-frizzy1` repo on Hugging Face, downloaded every workflow `.json` (raw + LFS zips; the Hunyuan
   workflow was extracted from its PNG's `tEXt` chunk), parsed each workflow's nodes and pulled out every model file name,
   cross-referenced them against the creator's READMEs.

### Hunyuan workflow loaded a Flux model — ✅ FIXED (v1.1.1)
The shipped Hunyuan Video workflow's diffusion loader referenced **`flux1-dev-Q5_K_S.gguf`** (a leftover), while the
README says **`fast-hunyuan-video-t2v-720p-Q5_K_M.gguf`**. The loader was repointed and saved as
`The_frizzy1_hunyuan-video-lowvram_v1.1.1.json`; the untouched original is in that folder's `source/`.

### Four CivitAI-only workflows — ✅ RESOLVED (JSONs received)
`Flux.2 Dev GGUF`, `Wan 2.2 AIO Rapid`, `Z-Image Turbo GGUF` and `AI Audio Maker` had no HF mirror; their workflow zips
were supplied and extracted, and all four are model-verified from their JSON (host repos confirmed 2026-10-14).

### Wan 2.2 AIO Rapid vs the "Custom Advanced VACE Node" — open
The HF `Custom-Advanced-VACE-Node` repo describes a "Rapid AIO I2V (First → Last Frame)" node built for the Phr00t
workflow. Confirm whether the CivitAI "WAN 2.2 AIO Rapid" page depends on it, and link them explicitly.

## Version reconciliation
CivitAI labels were normalised to semver — see [NAMING.md](NAMING.md). The mapping table is the source of truth.

---

## Confirmed-good summary (2026-10-14)

| Workflow | Models = manifest | Node packs = manifest | Links |
|---|:--:|:--:|:--:|
| MiniMax H3 Ultimate · 12 GB | ✅ | ✅ (none) | ✅ |
| Viggle-Animate (H3) | ✅ | ✅ | ✅ |
| LTX 2.5 Ultimate · 12 GB | ✅ | ✅ (none) | ✅ gated |
| LTX-2.3 Ultimate | ✅ | ✅ | ✅ |
| LTX-2 GGUF | ✅ | ✅ | ✅ |
| Wan Animate Ultimate | ✅ | ✅ | ✅ |
| Wan 2.2 Animate | ✅ (1 renamed LoRA, substitute given) | ✅ | ✅ |
| Wan 2.2 GGUF Low-VRAM | ✅ | ✅ | ✅ |
| Wan 2.2 AIO Rapid | ✅ | ✅ | ✅ |
| Wan 2.1 GGUF Low-VRAM | ✅ | ✅ | ✅ |
| Wan 2.1 FLF2V | ✅ | ✅ | ✅ |
| Hunyuan Video Low-VRAM | ✅ | ✅ | ✅ |
| Qwen Image 2.1 Ultimate · 12 GB | ✅ | ✅ (none) | ✅ |
| Qwen Image 2.1 · 12 GB | ✅ | ✅ (none) | ✅ |
| Qwen Image & Edit 2509 | ✅ | ✅ | ✅ |
| Krea 2 Ultimate · 12 GB | ✅ | ✅ (none) | ✅ |
| Ming Image 0.1 · 12 GB | ✅ | ✅ (none) | ✅ |
| Flux Kontext GGUF | ✅ (3 own LoRAs: by hand) | ✅ | ✅ |
| Flux.2 Dev GGUF | ✅ | ✅ | ✅ |
| Z-Image Turbo GGUF | ✅ | ✅ | ✅ |
| Image to 3D Ultimate · 12 GB | ✅ | ✅ (none) | ✅ |
| YuE2 Music · 12 GB | ✅ | ✅ (none) | ✅ |
| AI Audio Maker | ✅ | ✅ | ✅ |

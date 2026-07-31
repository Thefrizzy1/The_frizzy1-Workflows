# Naming & Versioning Standard

This is the single source of truth for how workflows, files and versions are named across the repository.
Everything else in the repo follows it. Nothing here renames anything on CivitAI — this is the *canonical*
naming that CivitAI pages should link **back** to.

---

## 1. Display name

```
The_frizzy1 — <Model Family> <Variant> vX.Y.Z
```

Examples:

- `The_frizzy1 — Wan 2.2 Animate v1.2.0`
- `The_frizzy1 — Wan 2.1 GGUF Low-VRAM v2.0.0`
- `The_frizzy1 — Flux Kontext GGUF v2.2.0`
- `The_frizzy1 — Qwen Image & Edit 2509 v1.0.0`

Rules:

- One em dash (` — `) between the author and the name.
- Model family is written the way the model authors write it: `Wan 2.2`, `Flux`, `Hunyuan`, `Qwen`, `LTXV-2.3`, `Z-Image`.
- No ALL-CAPS, no random underscores inside the display name, no `(12v etc)` fragments.

## 2. Folder / slug name

Lower-case kebab-case, no version number in the folder name (the folder always holds the latest; history lives in `changelog.md`):

```
workflows/wan2.2/animate/
workflows/wan2.1/gguf-lowvram/
workflows/flux/kontext/
```

## 3. Workflow file name inside a folder

```
The_frizzy1_<slug>_vX.Y.Z.json
```

e.g. `The_frizzy1_wan-2.2-animate_v1.2.0.json`. Keep the raw CivitAI/HF file as-is in a `source/` subfolder
so nothing is lost; the templated name is the copy users are pointed at.

## 4. Image / asset names

```
<slug>-<kind>-NN.<ext>
```

e.g. `wan-2.2-animate-preview-01.webp`, `flux-kontext-workflow.png`.

---

## 5. Versioning — CivitAI → semantic version

CivitAI versions are inconsistent (`v1.0`, `v2.0-ALL`, `v2.2`, `v3.0 T2V I2V FFLF +IDlora`). This repo
**normalises** them to `MAJOR.MINOR.PATCH`:

- **MAJOR** — the workflow was re-architected or the base model changed.
- **MINOR** — features/variants added (new sampler, looping, extra workflow in the pack).
- **PATCH** — settings fixes, node updates, no new capability.

The table below maps every published CivitAI version to its canonical semver. This mapping is authoritative;
when a new CivitAI version drops, add a row.

| Workflow | CivitAI label(s) | Canonical | Notes |
|---|---|---|---|
| Wan 2.1 GGUF Low-VRAM | v1.0, v1.1, v1.8, **v2.0-ALL** | **v2.0.0** | v2.0 added Teacache, Torch Compile, new GGUF loader |
| Wan 2.1 FLF2V | **v2.0-FirstFrameLastFrame** | **v2.0.0** | separate CivitAI model 1624167 |
| Wan 2.2 T2V/I2V + LoRA | **v1.0** | **v1.0.0** | |
| Wan 2.2 Animate | v1.0, **v1.2** | **v1.2.0** | v1.2 added looping + points editor out of subgraph |
| Flux Kontext GGUF | v1.0, v2.0, **v2.2** | **v2.2.0** | v2.0 two-pass; v2.2 fixed settings + Torch Compile |
| Flux.2 Dev GGUF | **v1.0** | **v1.0.0** | CivitAI 2508110 |
| Qwen Image & Edit 2509 | **v1.0** | **v1.0.0** | |
| Z-Image Turbo GGUF | **v1.0** | **v1.0.0** | CivitAI 2561639 |
| Hunyuan Video Low-VRAM | v1.0, **v1.1-Text2Vid** | **v1.1.0** | v1.1 added T2V |
| LTX-2 GGUF | v1.0, **v1.5** | **v1.5.0** | |
| LTX-2.3 Ultimate | **v3.0** | **v3.0.0** | CivitAI 2339823 (LTXV2.3 …+IDlora) |
| AI Audio Maker | **v1.0** | **v1.0.0** | CivitAI 2539489 |

> When CivitAI and this repo disagree, **this table wins** and the CivitAI label is shown in parentheses so
> existing users can still find the release they know.

<div align="center">

# The_frizzy1 — Low-VRAM ComfyUI Workflows

**The definitive home for every `The_frizzy1` ComfyUI workflow.**
GGUF-quantised image, video and audio generation that runs on as little as **4 GB VRAM**.

[![CivitAI](https://img.shields.io/badge/CivitAI-The__frizzy1-2b7cff?style=flat-square)](https://civitai.com/user/The_frizzy1)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-The--frizzy1-ffb000?style=flat-square)](https://huggingface.co/The-frizzy1)
[![YouTube](https://img.shields.io/badge/YouTube-@the__frizzy1-ff0033?style=flat-square)](https://www.youtube.com/@the_frizzy1)
[![Workflows](https://img.shields.io/badge/workflows-12-6a5cff?style=flat-square)](#workflows)
[![Min VRAM](https://img.shields.io/badge/min%20VRAM-4%20GB-3ecf8e?style=flat-square)](#workflows)
[![License](https://img.shields.io/badge/license-MIT-black?style=flat-square)](LICENSE)

</div>

> **Every model name in this repository was read directly out of the workflow `.json` files — not guessed.**
> All 12 workflows are model-verified. Where a source repo couldn't be fully confirmed it's flagged in the [audit](docs/AUDIT.md).

---

## Contents

- [Which workflow should I use?](#which-workflow-should-i-use)
- [Workflows](#workflows) — [Video](#-video) · [Image](#-image) · [Audio](#-audio)
- [Wan 2.1 vs 2.2 vs Animate](#wan-21-vs-22-vs-animate-read-this) — **read before mixing files**
- [Installation](#installation)
- [Documentation](#documentation)
- [Repository layout](#repository-layout)
- [Credits & license](#credits--license)

---

## Which workflow should I use?

| I want to… | Use | Runs on |
|---|---|---|
| Make **video** from text or an image, best quality | [Wan 2.2 GGUF Low-VRAM](workflows/wan2.2/gguf-lowvram) | 4 GB+ |
| **Animate a person** from a driving video (unlimited length) | [Wan 2.2 Animate](workflows/wan2.2/animate) | 4 GB+ |
| The **fastest / lightest** video path | [Wan 2.1 GGUF Low-VRAM](workflows/wan2.1/gguf-lowvram) | 4 GB+ |
| Video from **first frame → last frame** | [Wan 2.1 FLF2V](workflows/wan2.1/flf2v) | 4 GB+ |
| One **single-file** Wan 2.2, simplest setup | [Wan 2.2 AIO Rapid](workflows/wan2.2/aio-rapid) | 4–12 GB |
| **Edit or generate images**, realistic & cinematic | [Flux Kontext GGUF](workflows/flux/kontext) | 4 GB+ |
| The **newest Flux** image model | [Flux.2 Dev GGUF](workflows/flux/flux2-dev) | 6 GB+ |
| **Beginner-friendly** image generation + editing | [Qwen Image & Edit 2509](workflows/qwen/image-edit-2509) | 4 GB+ |
| **Fast, tiny** image generation | [Z-Image Turbo GGUF](workflows/z-image/turbo) | 4 GB+ |
| Newer **LTX video** (audio-aware) | [LTX-2](workflows/ltx/ltx2) · [LTX-2.3 Ultimate](workflows/ltx/ltx2.3-ultimate) | 4–12 GB |
| The **older Hunyuan** video path | [Hunyuan Video Low-VRAM](workflows/hunyuan/video) | 4 GB+ |
| Generate **audio** for a clip | [AI Audio Maker](workflows/audio/ai-audio-maker) | low |

---

## Workflows

Each workflow has its own folder with a full README, a verified download table, a changelog, and the
templated `.json`. Model names are verified from the workflow file.

### 🎬 Video

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[Wan 2.2 Animate](workflows/wan2.2/animate)** | v1.2.0 | 4 GB | V2V animate · looping | [CivitAI](https://civitai.com/models/2046477) · [HF](https://huggingface.co/The-frizzy1/Wan22ANIMATE) · [▶](https://www.youtube.com/watch?v=rtyfdmL-wF4) |
| **[Wan 2.2 GGUF Low-VRAM](workflows/wan2.2/gguf-lowvram)** | v1.0.0 | 4 GB | T2V · I2V (14B) · TI2V (5B) | [CivitAI](https://civitai.com/models/1817858) · [HF](https://huggingface.co/The-frizzy1/Wan22-T2V-I2V-LORA-4GB) · [▶](https://www.youtube.com/watch?v=C7ZttV320qk) |
| **[Wan 2.2 AIO Rapid](workflows/wan2.2/aio-rapid)** | v1.0.0 | 4–12 GB | T2V · I2V (single file) | [CivitAI](https://civitai.com/models/2522688) · [▶](https://www.youtube.com/watch?v=RdsyWkvG1nE) |
| **[Wan 2.1 GGUF Low-VRAM](workflows/wan2.1/gguf-lowvram)** | v2.0.0 | 4 GB | T2V · I2V · VACE · FLF · Fun | [CivitAI](https://civitai.com/models/1309674) · [HF](https://huggingface.co/The-frizzy1/Wan21-GGUF-4GB-Workflow) · [▶](https://www.youtube.com/watch?v=Xqjabf_eQ_U) |
| **[Wan 2.1 FLF2V](workflows/wan2.1/flf2v)** | v2.0.0 | 4 GB | First → Last frame | [CivitAI](https://civitai.com/models/1624167) |
| **[Hunyuan Video Low-VRAM](workflows/hunyuan/video)** | v1.1.1 | 4 GB | T2V · I2V | [CivitAI](https://civitai.com/models/1312419) · [HF](https://huggingface.co/The-frizzy1/Hunyuan-Video-Low-VRAM-4GB) |
| **[LTX-2 GGUF](workflows/ltx/ltx2)** | v1.5.0 | 4 GB | T2V · I2V · audio | [CivitAI](https://civitai.com/models/2339823) · [HF](https://huggingface.co/The-frizzy1/LTX2-GGUF-workflow) · [▶](https://www.youtube.com/watch?v=nnHUBMgdJac) |
| **[LTX-2.3 Ultimate](workflows/ltx/ltx2.3-ultimate)** | v3.0.0 | 12 GB | T2V · I2V · FFLF · audio · ID | [CivitAI](https://civitai.com/models/2339823) · [HF](https://huggingface.co/The-frizzy1/LTX23-Ultimate) · [▶](https://www.youtube.com/watch?v=im4wolfHvMk) |

### 🖼️ Image

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[Flux Kontext GGUF](workflows/flux/kontext)** | v2.2.0 | 4 GB | T2I · image edit | [CivitAI](https://civitai.com/models/1311703) · [HF](https://huggingface.co/The-frizzy1/Flux-Kontext-GGUF-4GB) · [▶](https://www.youtube.com/watch?v=4C0RJ01yRok) |
| **[Flux.2 Dev GGUF](workflows/flux/flux2-dev)** | v1.0.0 | 6 GB | T2I | [CivitAI](https://civitai.com/models/2508110) · [▶](https://www.youtube.com/watch?v=dcekWAbgDXg) |
| **[Qwen Image & Edit 2509](workflows/qwen/image-edit-2509)** | v1.0.0 | 4 GB | T2I · image edit | [CivitAI](https://civitai.com/models/2229874) · [HF](https://huggingface.co/The-frizzy1/Qwen-Image-Edit-2509-GGUF) · [▶](https://www.youtube.com/watch?v=NPni2ulov34) |
| **[Z-Image Turbo GGUF](workflows/z-image/turbo)** | v1.0.0 | 4 GB | T2I (fast turbo) | [CivitAI](https://civitai.com/models/2561639) |

### 🔊 Audio

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[AI Audio Maker](workflows/audio/ai-audio-maker)** | v1.0.0 | low | Audio · video-sync (MMAudio) | [CivitAI](https://civitai.com/models/2539489) |

<sub>▶ = video walkthrough on YouTube.</sub>

---

## Wan 2.1 vs 2.2 vs Animate (read this)

These are **three different model families** and their files are **not interchangeable** — the single most
common cause of "it won't load" errors. The short version:

- **Wan 2.1** — older, lightest. 1.3B/14B. One diffusion file. Often the best choice on 4 GB.
- **Wan 2.2** — current mainline. 14B loads **two** files (high-noise + low-noise experts); 5B is a single file.
- **Wan 2.2 Animate** — animates a character from a **reference image + driving video**. It does *not* generate from a prompt alone.

Full comparison, VAE/encoder traps, and a decision guide: **[docs/WAN-LINEAGE.md](docs/WAN-LINEAGE.md)**.

---

## Installation

The same four steps apply to every workflow; the specifics live in each workflow's own README.

1. **Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI)** and the [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
2. **Install the custom nodes** listed in the workflow's README (via Manager, then restart).
3. **Download the models** from that workflow's `downloads.md` into the exact `ComfyUI/models/…` folders shown.
4. **Load the `.json`** in ComfyUI and run.

> **Low on VRAM?** Pick a smaller GGUF quant (Q4/Q3), and enable Sage Attention / Triton where supported.
> The [quantisation cheat-sheet](docs/COMPATIBILITY.md#quantisation-cheat-sheet-gguf) explains the trade-offs.

---

## Documentation

| Doc | What's in it |
|---|---|
| **[docs/DOWNLOADS.md](docs/DOWNLOADS.md)** | Master model database — every file, the exact name the loader expects, and where to get it. |
| **[docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)** | Task, VRAM, quantisation and custom-node matrices. |
| **[docs/WAN-LINEAGE.md](docs/WAN-LINEAGE.md)** | Wan 2.1 vs 2.2 vs Animate — differences and file traps. |
| **[docs/NAMING.md](docs/NAMING.md)** | Naming standard + the CivitAI → semver version map. |
| **[docs/AUDIT.md](docs/AUDIT.md)** | How everything was verified, and anything still open. |
| **[models/README.md](models/README.md)** | One-line summary of every model family + shared support files. |

---

## Repository layout

Workflows are grouped by model family. Each workflow folder holds the same files.

```
The_frizzy1-Workflows/
├── README.md              you are here
├── docs/                  downloads · compatibility · wan-lineage · naming · audit
├── models/                model-family reference
├── workflows/
│   ├── wan2.1/            gguf-lowvram · flf2v
│   ├── wan2.2/            gguf-lowvram · animate · aio-rapid
│   ├── flux/              kontext · flux2-dev
│   ├── qwen/              image-edit-2509
│   ├── z-image/           turbo
│   ├── hunyuan/           video
│   ├── ltx/               ltx2 · ltx2.3-ultimate
│   └── audio/             ai-audio-maker
│       └── <workflow>/
│           ├── README.md          what it is, settings, nodes
│           ├── downloads.md       verified model table
│           ├── changelog.md       version history
│           ├── The_frizzy1_*.json the workflow (templated name)
│           ├── images/            samples + workflow graph
│           └── source/            original unmodified files
├── templates/             reusable doc templates
└── index.html             optional local dashboard (open in a browser)
```

---

## Credits & license

Workflows by **[The_frizzy1](https://civitai.com/user/The_frizzy1)** · videos on
**[YouTube](https://www.youtube.com/@the_frizzy1)** · mirrors on **[Hugging Face](https://huggingface.co/The-frizzy1)**.

This repository (documentation + workflow JSONs) is **[MIT licensed](LICENSE)**. The underlying AI models keep
their own licenses — FLUX.1 non-commercial, Tencent Hunyuan Community, Apache-2.0, and others — listed per file
in [docs/DOWNLOADS.md](docs/DOWNLOADS.md). Check a model's license before commercial use.

<div align="center">

# The_frizzy1 — Low-VRAM ComfyUI Workflows

**The definitive home for every `The_frizzy1` ComfyUI workflow.**
Video, image, 3D and audio workflows for normal GPUs: the newest models as **12 GB "Ultimate" workflows**
(every mode in one file, core ComfyUI nodes only, tested on an RTX 3060), and **GGUF workflows down to 4 GB VRAM**.

[![CivitAI](https://img.shields.io/badge/CivitAI-The__frizzy1-2b7cff?style=flat-square)](https://civitai.com/user/The_frizzy1)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-The--frizzy1-ffb000?style=flat-square)](https://huggingface.co/The-frizzy1)
[![YouTube](https://img.shields.io/badge/YouTube-@the__frizzy1-ff0033?style=flat-square)](https://www.youtube.com/@the_frizzy1)
[![Workflows](https://img.shields.io/badge/workflows-25-6a5cff?style=flat-square)](#workflows)
[![Min VRAM](https://img.shields.io/badge/min%20VRAM-4%20GB-3ecf8e?style=flat-square)](#workflows)
[![License](https://img.shields.io/badge/license-MIT-black?style=flat-square)](LICENSE)

</div>

☕ If a workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

---

> **Every model name in this repository was read directly out of the workflow `.json` files — not guessed.**
> All 25 workflows checked on 2026-10-15: every model file each `.json` loads is in its `models.json` / `downloads.md`,
> every download link resolves, and the custom node packs listed are the ones the `.json` really uses ([audit](docs/AUDIT.md)).

---

## Contents

- [Which workflow should I use?](#which-workflow-should-i-use)
- [Workflows](#workflows) — [Video](#-video) · [Image](#-image) · [Audio](#-audio)
- [Newest vs older](#newest-vs-older)
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
| **Native 2K** images on a 12 GB card (Qwen Image 2.1) | [Qwen Image 2.1 · 12 GB](workflows/qwen/image-2.1-12gb) | 12 GB |
| **Every Qwen Image 2.1 mode** (Turbo · edit · ControlNet pose / depth / edges) in one workflow | [Qwen Image 2.1 Ultimate · 12 GB](workflows/qwen/image-2.1-ultimate-12gb) | 12 GB |
| **Design images with text + real transparency** (Ming Image 0.1 Design) | [Ming Image 0.1 · 12 GB](workflows/ming/image-0.1-design-12gb) | 4 GB+* |
| **Fast, tiny** image generation | [Z-Image Turbo GGUF](workflows/z-image/turbo) | 4 GB+ |
| Newer **LTX video** (audio-aware) | [LTX-2](workflows/ltx/ltx2) · [LTX-2.3 Ultimate](workflows/ltx/ltx2.3-ultimate) | 4–12 GB |
| **Every MiniMax H3 mode** (T2V · I2V · R2V · multiframe · pose · extend) in one workflow, with sound | [MiniMax H3 Ultimate · 12 GB](workflows/minimax/h3-ultimate-12gb) | 12 GB |
| **LTX 2.5** text / image / first+last / pose-driven video in one workflow | [LTX 2.5 Ultimate · 12 GB](workflows/ltx/ltx-2.5-ultimate-12gb) | 12 GB |
| **Swap the person** in a video for your character (one still) | [Viggle-Animate (H3)](workflows/minimax/viggle-animate-h3) | 12 GB |
| **Genjutsu at home**: swap the person, whole clip, original sound | [H3 Character Swap · 12 GB](workflows/minimax/h3-character-swap-12gb) | 12 GB |
| **A whole story video** from a script: same character, moving scenes, dialogue, narrator + music | [Story Creator · 12 GB](workflows/story/story-creator-12gb) | 12 GB |
| **Animate a character** from a driving video, native nodes | [Wan Animate Ultimate](workflows/wan2.2/animate-ultimate) | 12 GB (GGUF path lower) |
| **Krea 2** or **Kroma** images + style reference | [Krea 2 Ultimate · 12 GB](workflows/krea/krea-2-ultimate-12gb) | 4 GB+* |
| One image → **textured 3D model** (.glb) | [Image to 3D Ultimate · 12 GB](workflows/3d/image-to-3d-ultimate-12gb) | 12 GB |
| The **older Hunyuan** video path | [Hunyuan Video Low-VRAM](workflows/hunyuan/video) | 4 GB+ |
| **Songs with vocals** from a style + your lyrics, or a cover of your song (YuE2) | [YuE2 Music · 12 GB](workflows/audio/yue2-music-12gb) | 4 GB+* |
| Generate **audio** for a clip | [AI Audio Maker](workflows/audio/ai-audio-maker) | low |

---

## Workflows

Each workflow has its own folder with a full README, a verified download table, a changelog, and the
templated `.json`. Model names are verified from the workflow file.

### 🎬 Video

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[Wan 2.2 Animate](workflows/wan2.2/animate)** | v1.2.0 | 4 GB | V2V animate · looping | [CivitAI](https://civitai.com/models/2046477) · [HF](https://huggingface.co/The-frizzy1/Wan22ANIMATE) · [▶](https://www.youtube.com/watch?v=rtyfdmL-wF4&list=PLRe4JVWoY_AU) |
| **[Wan 2.2 GGUF Low-VRAM](workflows/wan2.2/gguf-lowvram)** | v1.0.0 | 4 GB | T2V · I2V (14B) · TI2V (5B) | [CivitAI](https://civitai.com/models/1817858) · [HF](https://huggingface.co/The-frizzy1/Wan22-T2V-I2V-LORA-4GB) · [▶](https://www.youtube.com/watch?v=C7ZttV320qk&list=PLRe4JVWoY_AU) |
| **[Wan 2.2 AIO Rapid](workflows/wan2.2/aio-rapid)** | v1.0.0 | 4–12 GB | T2V · I2V (single file) | [CivitAI](https://civitai.com/models/2522688) · [▶](https://www.youtube.com/watch?v=RdsyWkvG1nE&list=PLRe4JVWoY_AU) |
| **[Wan 2.1 GGUF Low-VRAM](workflows/wan2.1/gguf-lowvram)** | v2.0.0 | 4 GB | T2V · I2V · VACE · FLF · Fun | [CivitAI](https://civitai.com/models/1309674) · [HF](https://huggingface.co/The-frizzy1/Wan21-GGUF-4GB-Workflow) · [▶](https://www.youtube.com/watch?v=Xqjabf_eQ_U&list=PLRe4JVWoY_AU) |
| **[Wan 2.1 FLF2V](workflows/wan2.1/flf2v)** | v2.0.0 | 4 GB | First → Last frame | [CivitAI](https://civitai.com/models/1624167) |
| **[Hunyuan Video Low-VRAM](workflows/hunyuan/video)** | v1.1.1 | 4 GB | T2V · I2V | [CivitAI](https://civitai.com/models/1312419) · [HF](https://huggingface.co/The-frizzy1/Hunyuan-Video-Low-VRAM-4GB) |
| **[LTX-2 GGUF](workflows/ltx/ltx2)** | v2.0.0 | 4 GB | T2V · I2V · audio | [CivitAI](https://civitai.com/models/2339823) · [HF](https://huggingface.co/The-frizzy1/LTX2-GGUF-workflow) · [▶](https://www.youtube.com/watch?v=nnHUBMgdJac&list=PLQ3PcJNbU2Ls) |
| **[LTX-2.3 Ultimate](workflows/ltx/ltx2.3-ultimate)** | v3.0.0 | 12 GB | T2V · I2V · FFLF · audio · ID | [CivitAI](https://civitai.com/models/2339823) · [HF](https://huggingface.co/The-frizzy1/LTX23-Ultimate) · [▶](https://www.youtube.com/watch?v=im4wolfHvMk&list=PLQ3PcJNbU2Ls) |
| **[MiniMax H3 Ultimate · 12 GB](workflows/minimax/h3-ultimate-12gb)** | v2.3.0 | 12 GB | T2V · I2V · last · FLF · R2V · multiframe · ControlNet pose · extend · audio | [▶](https://www.youtube.com/watch?v=KJNksY9Ur3w&list=PLMztlpsP7Bgg) · [▶](https://www.youtube.com/watch?v=H2lZud6dbf4&list=PLMztlpsP7Bgg) |
| **[LTX 2.5 Ultimate · 12 GB](workflows/ltx/ltx-2.5-ultimate-12gb)** | v2.0.0 | 12 GB | T2V · I2V · FLF · pose (IC-LoRA) · audio | [▶](https://www.youtube.com/watch?v=HeHY6N5hH_M&list=PLQ3PcJNbU2Ls) · [▶](https://www.youtube.com/watch?v=TlV72fg9skw&list=PLQ3PcJNbU2Ls) |
| **[Viggle-Animate (H3)](workflows/minimax/viggle-animate-h3)** | v2.0.0 | 12 GB | character replacement (V2V) | — |
| **[H3 Character Swap · 12 GB](workflows/minimax/h3-character-swap-12gb)** | v1.1.0 | 12 GB | character swap (V2V) · whole clip in loop passes · original sound | [▶](https://www.youtube.com/watch?v=zkhLZUGIIfE&list=PLMztlpsP7Bgg) |
| **[Story Creator · 12 GB](workflows/story/story-creator-12gb)** | v1.4.0 | 12 GB | story video: script (WORLD / [camera] / dialogue / narrator / [continue]) → stills → I2V · music | — |
| **[Wan Animate Ultimate](workflows/wan2.2/animate-ultimate)** | v2.0.0 | 12 GB | Wan Animate 2 · Wan 2.2 Animate GGUF + face video | [▶](https://www.youtube.com/watch?v=9idzB8mlYRY&list=PLRe4JVWoY_AU) · [▶](https://www.youtube.com/watch?v=aqFdglMbcIU&list=PLRe4JVWoY_AU) |

### 🖼️ Image

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[Flux Kontext GGUF](workflows/flux/kontext)** | v2.2.0 | 4 GB | T2I · image edit | [CivitAI](https://civitai.com/models/1311703) · [HF](https://huggingface.co/The-frizzy1/Flux-Kontext-GGUF-4GB) · [▶](https://www.youtube.com/watch?v=4C0RJ01yRok&list=PLG_da2oqTx7k) |
| **[Flux.2 Dev GGUF](workflows/flux/flux2-dev)** | v2.0.0 | 6 GB | T2I | [CivitAI](https://civitai.com/models/2508110) · [▶](https://www.youtube.com/watch?v=dcekWAbgDXg&list=PLG_da2oqTx7k) |
| **[Qwen Image & Edit 2509](workflows/qwen/image-edit-2509)** | v2.0.0 | 4 GB | T2I · image edit | [CivitAI](https://civitai.com/models/2229874) · [HF](https://huggingface.co/The-frizzy1/Qwen-Image-Edit-2509-GGUF) · [▶](https://www.youtube.com/watch?v=NPni2ulov34&list=PLG_da2oqTx7k) |
| **[Qwen Image 2.1 · 12 GB](workflows/qwen/image-2.1-12gb)** | v2.0.0 | 12 GB | T2I native 2K · turbo LoRA | [▶](https://www.youtube.com/watch?v=C5wZ2gU7j9E&list=PLG_da2oqTx7k) · [▶](https://www.youtube.com/watch?v=-yJvQ3lxWsE&list=PLG_da2oqTx7k) |
| **[Qwen Image 2.1 Ultimate · 12 GB](workflows/qwen/image-2.1-ultimate-12gb)** | v2.1.0 | 12 GB | T2I · Turbo · edit · remove background · ControlNet pose / depth / edges | [▶](https://www.youtube.com/watch?v=N7X0QBZ_r9c&list=PLG_da2oqTx7k) |
| **[Ming Image 0.1 · 12 GB](workflows/ming/image-0.1-design-12gb)** | v1.0.0 | 4 GB* | T2I · edit · RGBA | [▶](https://www.youtube.com/watch?v=DTleXeD74vs&list=PLG_da2oqTx7k) |
| **[Z-Image Turbo GGUF](workflows/z-image/turbo)** | v1.0.0 | 4 GB | T2I (fast turbo) | [CivitAI](https://civitai.com/models/2561639) |
| **[Krea 2 Ultimate · 12 GB](workflows/krea/krea-2-ultimate-12gb)** | v2.1.0 | 4 GB* | T2I · style reference · style LoRAs · Kroma | — |

### 🧊 3D

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|---|---|---|---|
| **[Image to 3D Ultimate · 12 GB](workflows/3d/image-to-3d-ultimate-12gb)** | v2.0.0 | 12 GB | image → textured mesh (Pixal3D · TRELLIS.2) | — |

### 🔊 Audio

| Workflow | Ver | Min VRAM | Tasks | Links |
|---|:---:|:---:|---|---|
| **[AI Audio Maker](workflows/audio/ai-audio-maker)** | v1.0.0 | low | Audio · video-sync (MMAudio) | [CivitAI](https://civitai.com/models/2539489) |
| **[YuE2 Music · 12 GB](workflows/audio/yue2-music-12gb)** | v1.0.0 | 4 GB* | text → song · cover | — |

<sub>▶ = video walkthrough on YouTube. 4 GB* = the 12 GB workflow's own files also ran on a 4 GB RTX 3050 Ti laptop with 16 GB RAM, slower: times in [docs/BENCHMARKS.md](docs/BENCHMARKS.md).</sub>

---

## Benchmarks
Every workflow's times on an RTX 3060 12 GB and a 4 GB RTX 3050 Ti laptop, the same graphs side by side: [docs/BENCHMARKS.md](docs/BENCHMARKS.md).

---

## Newest vs older

The older GGUF workflows still work and stay here for 4 GB cards. If you have 12 GB, start with the newest one:

| Older | Newest |
|---|---|
| Wan 2.1 GGUF / FLF2V, Hunyuan Video, LTX-2 GGUF, LTX-2.3 Ultimate | [MiniMax H3 Ultimate](workflows/minimax/h3-ultimate-12gb) · [LTX 2.5 Ultimate](workflows/ltx/ltx-2.5-ultimate-12gb) |
| Wan 2.2 Animate (5 custom node packs) | [Wan Animate Ultimate](workflows/wan2.2/animate-ultimate) · [Viggle-Animate (H3)](workflows/minimax/viggle-animate-h3) |
| Flux Kontext, Qwen Image & Edit 2509, Qwen Image 2.1 · 12 GB | [Qwen Image 2.1 Ultimate](workflows/qwen/image-2.1-ultimate-12gb) |
| Flux.2 Dev, Z-Image Turbo | [Krea 2 Ultimate](workflows/krea/krea-2-ultimate-12gb) · [Ming Image 0.1](workflows/ming/image-0.1-design-12gb) |

On **4 GB**: Wan 2.2 GGUF, Wan 2.2 Animate (Q4), Qwen Image & Edit 2509, Z-Image Turbo and LTX-2 GGUF are the
picks. How the 12 GB workflows are built (bypassed loaders, the mode switch, "Needs …" checks), frame counts and
sizes: [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md).

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

### The easy way: one command

Clone this repo and run the setup tool. It finds your ComfyUI, downloads the models a workflow needs into
the right folders, installs the custom nodes, and can launch ComfyUI for you.

```bash
python scripts/frizzy.py
```

That opens a menu. Or drive it directly:

```bash
python scripts/frizzy.py doctor wan2.2/animate --comfy "C:/path/to/ComfyUI"
```

Pure Python, no pip installs. Full usage: [scripts/README.md](scripts/README.md).

### By hand

1. **Install or update [ComfyUI](https://github.com/comfyanonymous/ComfyUI)** — the newest workflows need a recent version
   (0.39+ for H3 v2.3, YuE2, Ming, Kroma; the README says which). Plus the [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
2. **Custom nodes:** the 12 GB Ultimates need **none**. The older workflows list theirs in the README / `downloads.md`
   ([all of them](docs/COMPATIBILITY.md#custom-node-packs-per-workflow)) — install via Manager, then restart.
3. **Download the models** from that workflow's `downloads.md` into the `ComfyUI/models/…` folders shown (subfolders
   inside them are fine). Keep the file names: the loaders look for exactly those names.
4. **Load the `.json`** in ComfyUI and run.

> **Low on VRAM?** Pick a smaller GGUF quant (Q4/Q3), and enable Sage Attention / Triton where supported.
> The [quantisation cheat-sheet](docs/COMPATIBILITY.md#quantisation-cheat-sheet-gguf) explains the trade-offs.

---

## Documentation

| Doc | What's in it |
|---|---|
| **[docs/DOWNLOADS.md](docs/DOWNLOADS.md)** | Master model database — every file, the exact name the loader expects, and where to get it. |
| **[docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)** | Tasks, VRAM, video sizes / frame counts, GGUF vs int8, custom node packs per workflow. |
| **[docs/WAN-LINEAGE.md](docs/WAN-LINEAGE.md)** | Wan 2.1 vs 2.2 vs Animate — differences and file traps. |
| **[docs/NAMING.md](docs/NAMING.md)** | Naming standard + the CivitAI → semver version map. |
| **[docs/AUDIT.md](docs/AUDIT.md)** | How everything was verified, and anything still open. |
| **[models/README.md](models/README.md)** | Every model family (newest vs older), shared support files, **licenses**. |

---

## Repository layout

Workflows are grouped by model family. Each workflow folder holds the same files.

```
The_frizzy1-Workflows/
├── README.md              you are here
├── docs/                  downloads · compatibility · wan-lineage · naming · audit
├── models/                model-family reference
├── workflows/
│   ├── minimax/           h3-ultimate-12gb · viggle-animate-h3 · h3-character-swap-12gb
│   ├── ltx/               ltx-2.5-ultimate-12gb · ltx2.3-ultimate · ltx2
│   ├── wan2.2/            animate-ultimate · animate · gguf-lowvram · aio-rapid
│   ├── wan2.1/            gguf-lowvram · flf2v
│   ├── hunyuan/           video
│   ├── qwen/              image-2.1-ultimate-12gb · image-2.1-12gb · image-edit-2509
│   ├── krea/              krea-2-ultimate-12gb
│   ├── ming/              image-0.1-design-12gb
│   ├── flux/              kontext · flux2-dev
│   ├── z-image/           turbo
│   ├── story/             story-creator-12gb
│   ├── 3d/                image-to-3d-ultimate-12gb
│   └── audio/             yue2-music-12gb · ai-audio-maker
│       └── <workflow>/
│           ├── README.md          what it is, settings, nodes
│           ├── downloads.md       verified model table
│           ├── changelog.md       version history
│           ├── The_frizzy1_*.json the workflow (templated name)
│           ├── models.json        model + node-pack list for scripts/frizzy.py
│           ├── samples/           example outputs + workflow graph
│           └── source/            original unmodified files
├── scripts/               frizzy.py setup tool
├── templates/             reusable doc templates
└── index.html             optional local dashboard (open in a browser)
```

---

## Credits & license

Workflows by **[The_frizzy1](https://civitai.com/user/The_frizzy1)** · videos on
**[YouTube](https://www.youtube.com/@the_frizzy1)** · mirrors on **[Hugging Face](https://huggingface.co/The-frizzy1)**.

This repository (documentation + workflow JSONs) is **[MIT licensed](LICENSE)** — that covers the workflow files, not the
models. Every model keeps its own license: Wan, Qwen Image (original), Z-Image are Apache-2.0; Ming and the 3D models MIT;
MiniMax H3, LTX, Krea 2 / Kroma and Hunyuan have their own community licenses; **Qwen Image 2.1 (research),
Flux Kontext / Flux.2 Dev, YuE2 and MMAudio are non-commercial**. The full table, read from each Hugging Face card:
[models/README.md](models/README.md#licenses-read-before-commercial-use). Check a model's card before commercial use.

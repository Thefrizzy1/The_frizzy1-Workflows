<div align="center">

# The_frizzy1 — Low-VRAM ComfyUI Workflows

**The definitive, verified home for every `The_frizzy1` ComfyUI workflow.**
GGUF-quantised image, video and audio generation that runs on as little as **4 GB VRAM**.

[![CivitAI](https://img.shields.io/badge/CivitAI-The__frizzy1-blue)](https://civitai.com/user/The_frizzy1)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-The--frizzy1-yellow)](https://huggingface.co/The-frizzy1)
[![YouTube](https://img.shields.io/badge/YouTube-@the__frizzy1-red)](https://www.youtube.com/@the_frizzy1)

</div>

> 🖥️ **Visual dashboard:** open [`index.html`](index.html) locally, or (once GitHub Pages is enabled)
> browse it live at `https://<user>.github.io/The_frizzy1-Workflows/`. It's a filterable card view of every
> workflow with video thumbnails, VRAM badges and one-click links.

---

## Start here

New to this? You want two things: a GPU with **4 GB VRAM or more**, and a working **ComfyUI** install.
Then pick a workflow from the table below, open its folder, and follow its README.

> **Every download link, custom node and model name in this repository was extracted directly from the
> actual workflow files (`.json`) and verified against the published Hugging Face repos.** Where something
> could not be confirmed from a workflow file, it is explicitly marked **`Not verified`**.

---

## Which workflow should I use?

| I want to… | Use | Runs on |
|---|---|---|
| Make **video from text or an image** on a tiny GPU | [Wan 2.2 GGUF Low-VRAM](workflows/wan-2.2-gguf-lowvram) | 4 GB+ |
| **Animate a person** from a reference video (unlimited length) | [Wan 2.2 Animate](workflows/wan-2.2-animate) | 4 GB+ |
| The **older, lighter** video path (1.3B models, most variants) | [Wan 2.1 GGUF Low-VRAM](workflows/wan-2.1-gguf-lowvram) | 4 GB+ |
| Video with **first-frame → last-frame** control | [Wan 2.1 FLF2V](workflows/wan-2.1-flf2v) | 4 GB+ |
| **Edit or generate images** (realistic, cinematic) | [Flux Kontext GGUF](workflows/flux-kontext-gguf) | 4 GB+ |
| The **newest Flux** image model | [Flux.2 Dev GGUF](workflows/flux2-dev-gguf) | 6 GB+ |
| **Beginner-friendly image** generation + editing | [Qwen Image & Edit 2509](workflows/qwen-image-edit-2509) | 4 GB+ |
| **Fast, tiny** image generation | [Z-Image Turbo GGUF](workflows/z-image-turbo-gguf) | 4 GB+ |
| Newer **LTX video** (audio-aware) | [LTX-2 GGUF](workflows/ltx2-gguf) · [LTX-2.3 Ultimate](workflows/ltx2.3-ultimate) | 4–12 GB |
| The **older Hunyuan** video path | [Hunyuan Video Low-VRAM](workflows/hunyuan-video-lowvram) | 4 GB+ |
| Generate **audio** | [AI Audio Maker](workflows/ai-audio-maker) | — |

> ⚠️ **Wan 2.1 vs 2.2 vs Animate — which is which?** These are **not** the same model and are **not**
> interchangeable. See [the Wan lineage & compatibility note](docs/WAN-LINEAGE.md) before mixing files —
> most "it won't load" errors come from feeding a 2.2 model into a 2.1 loader, or vice-versa.

---

## All workflows

| Workflow | Version | Model family | Task | Min VRAM | Source |
|---|---|---|---|---|---|
| [Wan 2.1 GGUF Low-VRAM](workflows/wan-2.1-gguf-lowvram) | v2.0.0 | Wan 2.1 | T2V · I2V · VACE · FLF · Fun | 4 GB | [HF](https://huggingface.co/The-frizzy1/Wan21-GGUF-4GB-Workflow) |
| [Wan 2.1 FLF2V](workflows/wan-2.1-flf2v) | v2.0.0 | Wan 2.1 | First→Last frame | 4 GB | [CivitAI](https://civitai.com/models/1624167) |
| [Wan 2.2 GGUF Low-VRAM](workflows/wan-2.2-gguf-lowvram) | v1.0.0 | Wan 2.2 | T2V · I2V (14B) · TI2V (5B) | 4 GB | [HF](https://huggingface.co/The-frizzy1/Wan22-T2V-I2V-LORA-4GB) |
| [Wan 2.2 Animate](workflows/wan-2.2-animate) | v1.2.0 | Wan 2.2 Animate | V2V animate + looping | 4 GB | [HF](https://huggingface.co/The-frizzy1/Wan22ANIMATE) |
| [Flux Kontext GGUF](workflows/flux-kontext-gguf) | v2.2.0 | Flux Dev/Schnell/Kontext | T2I · image edit | 4 GB | [HF](https://huggingface.co/The-frizzy1/Flux-Kontext-GGUF-4GB) |
| [Flux.2 Dev GGUF](workflows/flux2-dev-gguf) | v1.0.0 | Flux.2 Dev | T2I | 6 GB | [CivitAI](https://civitai.com/models/2508110) |
| [Qwen Image & Edit 2509](workflows/qwen-image-edit-2509) | v1.0.0 | Qwen Image | T2I · image edit | 4 GB | [HF](https://huggingface.co/The-frizzy1/Qwen-Image-Edit-2509-GGUF) |
| [Z-Image Turbo GGUF](workflows/z-image-turbo-gguf) | v1.0.0 | Z-Image Turbo | T2I | 4 GB | [CivitAI](https://civitai.com/models/2561639) |
| [Hunyuan Video Low-VRAM](workflows/hunyuan-video-lowvram) | v1.1.0 | Hunyuan Video | T2V · I2V | 4 GB | [HF](https://huggingface.co/The-frizzy1/Hunyuan-Video-Low-VRAM-4GB) |
| [LTX-2 GGUF](workflows/ltx2-gguf) | v1.5.0 | LTXV-2 | T2V · I2V | 4 GB | [HF](https://huggingface.co/The-frizzy1/LTX2-GGUF-workflow) |
| [LTX-2.3 Ultimate](workflows/ltx2.3-ultimate) | v3.0.0 | LTXV-2.3 | T2V · I2V · audio · FFLF | 12 GB | [HF](https://huggingface.co/The-frizzy1/LTX23-Ultimate) |
| [AI Audio Maker](workflows/ai-audio-maker) | v1.0.0 | Audio | Audio generation | — | [CivitAI](https://civitai.com/models/2539489) |

Plus a helper node: [Custom Advanced VACE Node](https://huggingface.co/The-frizzy1/Custom-Advanced-VACE-Node) (for the Phr00t first→last-frame workflow).

---

## Repository map

```
The_frizzy1-Workflows/
├── README.md              ← you are here
├── docs/
│   ├── DOWNLOADS.md       master download database (every model, verified links)
│   ├── COMPATIBILITY.md   workflow × model / VRAM / quant matrices
│   ├── WAN-LINEAGE.md     the Wan 2.1 vs 2.2 vs Animate caveats
│   ├── NAMING.md          naming standard + CivitAI→semver version map
│   └── AUDIT.md           verification log, open issues, things to double-check
├── models/                one page per model family
├── workflows/             one folder per workflow (see wan-2.2-animate for the template)
├── templates/             reusable README / release-note templates
└── assets/                banners, shared images
```

---

## Credits & license

All workflows by **[The_frizzy1](https://civitai.com/user/The_frizzy1)**. Individual models retain their own
licenses (FLUX.1 non-commercial, Tencent Hunyuan Community, Apache-2.0, etc.) — see each workflow page and
[docs/DOWNLOADS.md](docs/DOWNLOADS.md). This documentation repository may be reused and adapted; the underlying
models may not, except under their respective licenses.

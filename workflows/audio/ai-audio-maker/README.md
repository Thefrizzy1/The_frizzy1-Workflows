# The_frizzy1 - AI Audio Maker v1.0.1

> Generate synced audio for video (and standalone audio) using MMAudio in ComfyUI.

| | |
|---|---|
| **Model family** | MMAudio (44kHz) |
| **Tasks** | Audio generation · video-synced audio |
| **Workflow file** | `The_frizzy1_ai-audio-maker_v1.0.1.json` |
| **Min VRAM** | Low (MMAudio is light) |
| **CivitAI** | https://civitai.com/models/2539489 |
| **License** | Workflow: MIT · MMAudio: CC-BY-NC-4.0 (**non-commercial**; Kijai's safetensors repack is tagged MIT, the original weights are NC) |


## Preview

<p align="center"><img src="samples/sample-1.webp" width="70%" alt="AI Audio Maker sample output"></p>

<sub>Example outputs from this workflow.</sub>

**Sample clips:** [clip 1](samples/preview-1.mp4)

## Overview
Uses the **MMAudio** stack to generate audio, including audio synchronised to a video via the Synchformer.
Pairs well with the video workflows (e.g. add audio to a Wan/LTX clip). Models verified from the workflow JSON.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor audio/ai-audio-maker --comfy "C:/path/to/ComfyUI"
```

The only pip package needed is `accelerate`, which ComfyUI-MMAudio requires (install it into the ComfyUI Python if the pack fails to import). Details: [scripts/README.md](../../../scripts/README.md).

## Requirements

- ComfyUI with the core video nodes Load Video, Get Video Components, Create Video and Save Video (recent ComfyUI; checked on 0.45.3).
- Custom node pack [ComfyUI-MMAudio](https://github.com/kijai/ComfyUI-MMAudio): MMAudio Model Loader, MMAudio Feature Utils Loader, MMAudio Sampler. Its `requirements.txt` includes `accelerate`.
- ComfyUI 0.45.3 check (2026-11-14): the graph converts on 0.45.3, but it does not validate there yet: on the bench server ComfyUI-MMAudio failed to import (`No module named 'accelerate'`), so the three MMAudio nodes were unknown. Not run on 0.45.3.
- Attention: on the 24 GB bench server `--use-sage-attention` used less VRAM at the same speed and `--use-ck-attention` gave a different output for the same seed (measured on Z-Image, not on MMAudio).

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- Any video workflow: generate the clip, then add audio here.

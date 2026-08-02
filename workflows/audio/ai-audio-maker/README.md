# The_frizzy1 — AI Audio Maker v1.0.0

> Generate synced audio for video (and standalone audio) using MMAudio in ComfyUI.

| | |
|---|---|
| **Model family** | MMAudio (44kHz) |
| **Tasks** | Audio generation · video-synced audio |
| **Min VRAM** | Low (MMAudio is light) |
| **CivitAI** | https://civitai.com/models/2539489 |
| **License** | Check MMAudio model card |


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

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- Any video workflow — generate the clip, then add audio here.

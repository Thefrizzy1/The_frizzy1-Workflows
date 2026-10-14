# Setup tool — `frizzy.py`

One script that finds your ComfyUI, works out what a workflow needs, downloads the missing models, installs
the custom nodes, and can launch ComfyUI. Python 3.7+, no pip installs. Git is only needed to install nodes.

## Run it

From the repo root:

```bash
python scripts/frizzy.py
```

That opens a menu: pick a workflow, see what's present vs missing, then download models, install nodes, or
launch ComfyUI.

## Commands

```bash
python scripts/frizzy.py find                         # locate ComfyUI and remember it
python scripts/frizzy.py status wan2.2/animate        # what's present, what's missing
python scripts/frizzy.py get    wan2.2/animate        # download missing required models
python scripts/frizzy.py get    wan2.2/animate --optional
python scripts/frizzy.py nodes  wan2.2/animate        # git clone missing custom nodes
python scripts/frizzy.py doctor wan2.2/animate        # do all of it, then offer to launch
```

Workflow names match the folders under `workflows/` — `wan2.1/gguf-lowvram`, `flux/kontext`, `qwen/image-edit-2509`, and so on.

## ComfyUI location

Auto-detected on first run (common install paths, then a bounded scan) and cached in `scripts/.comfypath`.
Override any time:

```bash
python scripts/frizzy.py status flux/kontext --comfy "D:/AI/ComfyUI"
# or set an environment variable
setx FRIZZY_COMFY "D:/AI/ComfyUI"      # Windows
export FRIZZY_COMFY=/opt/ComfyUI        # Linux / macOS
```

## What it does with each file

| File type | Goes to |
|---|---|
| diffusion / GGUF | `ComfyUI/models/diffusion_models/` |
| text encoders | `ComfyUI/models/text_encoders/` |
| VAE | `ComfyUI/models/vae/` |
| CLIP vision | `ComfyUI/models/clip_vision/` |
| LoRAs | `ComfyUI/models/loras/` |
| MMAudio | `ComfyUI/models/mmaudio/` |
| upscalers / latent upscalers | `ComfyUI/models/upscale_models/` · `latent_upscale_models/` |

Files you already have are found and skipped — also in **subfolders** (e.g. `diffusion_models/MiniMax-H3/…`, which
ComfyUI lists as `MiniMax-H3ile`) and in the folders of your **`extra_model_paths.yaml`** (and ComfyUI Desktop's
`extra_models_config.yaml`). Interrupted downloads resume. Where a source repo uses another file name than the
workflow loads, the file is saved under the workflow's name. A few files (your own LoRAs, a renamed file with no
public source) are listed at the end with the page to grab them from. Helper files like `rife49.pth` and the DWPose /
SAM2 models are downloaded by their custom nodes on first run, so the tool doesn't fetch them.

## Gated models

Some models sit behind a licence (LTX 2.5, Flux.2 Dev). Accept it on the model's Hugging Face page, create a token, then:

```bash
setx HF_TOKEN "hf_xxx"      # Windows (reopen the terminal after)
export HF_TOKEN=hf_xxx       # Linux / macOS
```

## After it finishes

New model files show up in ComfyUI when you hit **Refresh** (or the `R` key). A workflow that needs new
custom nodes wants a full restart. The tool's `doctor` command offers to launch ComfyUI for you.

The per-file source of truth is each workflow's `models.json`; [docs/DOWNLOADS.md](../docs/DOWNLOADS.md) and the
"Direct links" part of each `downloads.md` are generated from it.

## Checking the repo — `check_repo.py`

```bash
python scripts/check_repo.py            # models / node packs / versions of all workflows
python scripts/check_repo.py --links    # + HEAD-request every download link
```

Compares every workflow `.json` with its `models.json`, `downloads.md`, README, changelog and the root README, and the
node packs the `.json` really uses. Exit code 1 on any problem; documented exceptions are in `check_allow.json`.
Run it after adding or updating a workflow.

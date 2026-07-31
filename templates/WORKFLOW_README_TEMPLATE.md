<!--
  Workflow README template.
  Copy this file to workflows/<slug>/README.md and fill every {{PLACEHOLDER}}.
  Delete any section that genuinely does not apply — but prefer writing "Not verified"
  over deleting, so the structure stays identical across all workflows.
-->

# The_frizzy1 — {{DISPLAY NAME}} v{{X.Y.Z}}

> {{One-line what-it-does.}}

| | |
|---|---|
| **Model family** | {{Wan 2.2 / Flux / …}} |
| **Tasks** | {{T2V · I2V · …}} |
| **Min VRAM** | {{4 GB}} |
| **Tested on** | {{RTX 3050 4 GB}} |
| **CivitAI** | {{url}} |
| **Hugging Face** | {{url}} |
| **YouTube explainer** | {{url}} |
| **License** | {{Apache-2.0 / FLUX non-commercial / …}} |

## Overview
{{2–4 sentences. What it is, who it's for, what makes it different.}}

## Capabilities
- {{bullet}}

## Hardware & VRAM
{{Table or prose. Include quant→VRAM guidance.}}

## Required models
See the per-workflow [downloads.md](downloads.md) for the full table with verified links.
Every file below was read from the workflow `.json` unless marked *Not verified*.

## Required custom nodes
| Node | Link |
|---|---|
| {{name}} | {{url}} |

## Optional custom nodes
| Node | Link | Why |
|---|---|---|

## Installation
1. {{step}}

## Recommended settings
| Setting | Value | Notes |
|---|---|---|

## Inputs / Outputs
- **Inputs:** {{…}}
- **Outputs:** {{…}}

## Performance
{{Expected render times where known, else "Not verified".}}

## Known issues
- {{issue → fix}}

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- {{link}}

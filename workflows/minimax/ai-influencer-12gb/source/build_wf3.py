"""Workflow 3 for the AI Influencer folder: a ready-to-load Viggle Remake swap workflow (12 GB), made from the API graph that ran on the
RTX 3060 (frontend export wf/viggle_ui_raw.json). Lays the nodes out with space between them, names the inputs, adds the how-to note.
    python build_wf3.py OUT.json"""
import json, sys
w = json.load(open("wf/viggle_ui_raw.json", encoding="utf-8"))
N = {n["id"]: n for n in w["nodes"]}
POS = {7: (640, 0, 440, 520, "Your clip (24 fps, 90 to 345 frames on the 17n+5 grid)"), 9: (640, 620, 440, 520, "Keyframe (painted in workflow 2)"),
       1: (1160, 0, 420, 90, "Viggle Remake swap model"), 4: (1160, 190, 420, 110, "Text encoder"), 5: (1160, 400, 420, 60, "Video VAE"), 6: (1160, 560, 420, 60, "Audio VAE"),
       14: (1160, 720, 420, 60, "Sampler"), 15: (1160, 880, 420, 60, "Sigmas (6 steps)"),
       8: (1660, 0, 260, 110, None), 3: (1660, 210, 320, 60, "Keyframe until"),
       11: (2060, 0, 560, 640, "Viggle Remake: prompt, pins, frames, short edge"),
       12: (2700, 0, 300, 90, None), 13: (2700, 190, 300, 50, None),
       16: (3080, 0, 300, 110, "Sample"), 17: (3080, 210, 300, 50, None), 18: (3080, 360, 300, 50, None),
       19: (3460, 0, 320, 180, None), 20: (3460, 280, 440, 520, "Result")}
for i, (x, y, wd, ht, title) in POS.items():
    N[i]["pos"], N[i]["size"] = [x, y], [wd, ht]
    if title:
        N[i]["title"] = title
for i in (7, 9, 20):
    N[i]["color"], N[i]["bgcolor"] = "#232", "#353"
assert set(POS) == set(N), set(N) - set(POS)
NOTE = """# The_frizzy1 · AI Influencer 3 · Viggle Remake swap · 12 GB · v1.0.0

Puts your character into a clip: the clip gives the motion and the sound, one painted keyframe gives the look.
This is the graph I ran on an RTX 3060 12 GB, built on **Viggle Remake** by Viggle (their nodes and their swap model).

## Before you start
- Install Viggle's node pack: the folder `comfyui/ComfyUI-Viggle-Remake` from huggingface.co/Viggle/Viggle-Remake goes into `ComfyUI/custom_nodes/`.
- Download the swap model `int8/viggle_remake_swap_pruned_int8_convrot.safetensors` (21.0 GB) into `models/diffusion_models/`, plus the MiniMax H3 text encoder, video VAE and audio VAE (see downloads.md in the repo folder).

## How to use
1. **Your clip**: 24 fps, 90 to 345 frames, and the count must be on the grid 17n+5 (90, 107, 124, 141, ...).
2. **Keyframe**: one frame of that clip with your character painted in (AI Influencer 2 with two pictures).
3. On the **Viggle Remake** node:
   - **prompt**: the six-section prompt. Describe your clip and your character; the seconds in it must match the frame count. Example: prompts/6-viggle-remake-video-prompt.txt in the repo folder.
   - **pins**: the frame number the keyframe was taken from (12 = half a second in).
   - **frames**: the frame count of your clip.
   - **short_edge**: 480 is the benchmark size. **Go bigger for quality**: 608 looked clearly better on the same card.
4. **Run**. The clip's own sound is kept.

## Speed (RTX 3060 12 GB, cold start)
832x480, 124 frames: 6:37 · 1056x608, 90 frames: 8:34 (peak VRAM 11.5 GB, RAM 21.6 GB).

## Credits
Viggle Remake by Viggle, built on MiniMax H3 (MiniMax H3 Community License). Graph by **The_frizzy1**:
[YouTube](https://www.youtube.com/@the_frizzy1) · [workflows](https://github.com/Thefrizzy1/The_frizzy1-Workflows).
"""
nid = max(N) + 1
w["nodes"].append({"id": nid, "type": "MarkdownNote", "pos": [0, 0], "size": [580, 1140], "flags": {}, "order": 0, "mode": 0, "inputs": [], "outputs": [],
                   "title": "How to use · v1.0.0", "properties": {}, "widgets_values": [NOTE], "color": "#432", "bgcolor": "#653"})
w["last_node_id"] = nid
w.setdefault("extra", {})["ds"] = {"scale": 0.45, "offset": [40, 60]}
json.dump(w, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", sys.argv[1], len(w["nodes"]), "nodes")

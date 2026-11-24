# Changelog · Fibo 2.0 Edit + Text to Image · 12 GB
## v1.1.0 (2026-11-24)
- New: text-to-image workflow `The_frizzy1_fibo2-t2i-dev-12gb_v1.1.0.json` with Fibo 2.0 Dev int8. Six numbered groups, seven inputs in group 1 (App mode lists them), How to use and Downloads notes. There is no local Comfy text-to-image template for Fibo 2.0, so it was built from the Edit Dev template's loaders and settings, the Dev model card (50 steps, CFG 5, Bria's text-to-image negative) and `bria-vgl` 0.10.2's "generate" enhancer instructions.
- Prompt enhancer: Qwen3-VL 8B int8 (the edit workflow's file) through `TextGenerateV2`, on by default, with a switch to send your own prompt.
- Optional Turbo LoRA (`fibo_2.0_turbo_lora_avg_rank_270_bf16`), bypassed by default; 8 steps / CFG 1 tested on two prompts (12-16 s instead of 82 s).
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, inside a 10.5 GiB VRAM budget (peak 10.2 GiB) and without a budget. Not verified on a 12 GB card.
- The edit workflow is unchanged (still `..._v1.0.1.json`); not run on 0.45.3.
- New samples `fibo2-t2i-sample-01..03.webp` and `samples/workflow.png` (the text-to-image graph).
## v1.0.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, inputs, important settings, tips, tested-on line, attention line (--use-sage-attention / --use-ck-attention). Downloads note moved down so the notes do not overlap.
- Converts and validates on ComfyUI 0.45.3 (not run there). Old v1.0.0 file moved to `source/`.
## v1.0.0
- One file: edit with the Qwen3-VL 8B prompt enhancer, Turbo 4 steps, Qwen3-VL-4B int8. Core nodes only (ComfyUI 0.43+). Tested on the RTX 3060 (ComfyUI 0.43.1).

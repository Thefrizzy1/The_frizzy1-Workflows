#!/usr/bin/env python3
"""
The_frizzy1 workflow setup tool.

Finds your ComfyUI install, tells you what a workflow needs, downloads the
missing models, installs the custom nodes, and can launch ComfyUI for you.
Pure Python 3.7+, no pip installs. Git is only needed for installing nodes.

Quick start (just run it and follow the menu):
    python scripts/frizzy.py

Or drive it directly:
    python scripts/frizzy.py status wan2.2/animate
    python scripts/frizzy.py get    wan2.2/animate --optional
    python scripts/frizzy.py nodes  wan2.2/animate
    python scripts/frizzy.py doctor wan2.2/animate      # check everything + offer to launch
    python scripts/frizzy.py find                       # locate ComfyUI and remember it

ComfyUI location: auto-detected and cached in scripts/.comfypath.
Override any time with  --comfy "C:/path/to/ComfyUI"  or the FRIZZY_COMFY env var.
Gated repos (some Flux models) need a token: set HF_TOKEN in your environment.
"""
import argparse, glob, json, os, subprocess, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CACHE = os.path.join(HERE, ".comfypath")
PORT = 8188

# ---------- small helpers ----------

def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"

def c(txt, code):
    if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
        return txt
    return f"\033[{code}m{txt}\033[0m"

ok_ = lambda s: c(s, "32")
bad_ = lambda s: c(s, "31")
dim_ = lambda s: c(s, "90")
hi_ = lambda s: c(s, "1;36")

def manifests():
    out = {}
    for p in glob.glob(os.path.join(REPO, "workflows", "*", "*", "models.json")):
        d = json.load(open(p, encoding="utf-8"))
        out[d["workflow"]] = d
    return dict(sorted(out.items()))

def load(workflow):
    p = os.path.join(REPO, "workflows", workflow.strip("/"), "models.json")
    if not os.path.isfile(p):
        sys.exit(bad_(f"No manifest for '{workflow}'. Run 'python scripts/frizzy.py' to pick from the list."))
    return json.load(open(p, encoding="utf-8"))

# ---------- find ComfyUI ----------

def _looks_like_comfy(path):
    return path and os.path.isdir(os.path.join(path, "models")) and (
        os.path.isfile(os.path.join(path, "main.py")) or os.path.isdir(os.path.join(path, "custom_nodes")))

def _drives():
    if os.name != "nt":
        return ["/"]
    import string
    return [f"{d}:\\" for d in string.ascii_uppercase if os.path.isdir(f"{d}:\\")]

def find_comfy(cli=None, remember=True, quiet=False):
    if cli and _looks_like_comfy(os.path.expanduser(cli)):
        p = os.path.abspath(os.path.expanduser(cli))
        if remember: open(CACHE, "w").write(p)
        return p
    for src in (os.environ.get("FRIZZY_COMFY"), open(CACHE).read().strip() if os.path.exists(CACHE) else None):
        if src and _looks_like_comfy(src):
            return src
    home = os.path.expanduser("~")
    names = ["ComfyUI", os.path.join("ComfyUI_windows_portable", "ComfyUI"),
             os.path.join("ComfyUI_windows_portable", "ComfyUI_windows_portable", "ComfyUI")]
    bases = [home, os.path.join(home, "Desktop"), os.path.join(home, "Documents"),
             os.path.join(home, "Downloads"), os.getcwd(), os.path.dirname(REPO)] + _drives()
    for b in bases:
        for n in names:
            cand = os.path.join(b, n)
            if _looks_like_comfy(cand):
                p = os.path.abspath(cand)
                if remember: open(CACHE, "w").write(p)
                if not quiet: print(dim_(f"found ComfyUI at {p}"))
                return p
    if not quiet:
        print(dim_("scanning for ComfyUI (this can take a moment)..."))
    skip = {".git", ".venv", "node_modules", "__pycache__", "models", "custom_nodes", "input", "output"}
    for base in [home] + _drives():
        base_depth = base.rstrip("\\/").count(os.sep)
        for root, dirs, _ in os.walk(base):
            if root.count(os.sep) - base_depth > 3:
                dirs[:] = []
                continue
            dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
            if os.path.basename(root) == "ComfyUI" and _looks_like_comfy(root):
                p = os.path.abspath(root)
                if remember: open(CACHE, "w").write(p)
                if not quiet: print(dim_(f"found ComfyUI at {p}"))
                return p
    return None

def need_comfy(cli):
    comfy = find_comfy(cli)
    if not comfy:
        sys.exit(bad_("Could not find ComfyUI. Pass it with --comfy \"C:/path/to/ComfyUI\"."))
    return comfy

# ---------- identify ----------

def scan(data, comfy):
    """Return (present, missing, manual) lists of file specs."""
    present, missing, manual = [], [], []
    for s in data["files"]:
        if s.get("manual"):
            manual.append(s); continue
        path = os.path.join(comfy, "models", s["dest"], s["name"])
        (present if os.path.exists(path) else missing).append(s)
    return present, missing, manual

def scan_nodes(data, comfy):
    have, need = [], []
    for n in data.get("nodes", []):
        (have if os.path.isdir(os.path.join(comfy, "custom_nodes", n["name"])) else need).append(n)
    return have, need

def status(workflow, comfy, verbose=True):
    data = load(workflow)
    present, missing, manual = scan(data, comfy)
    have_n, need_n = scan_nodes(data, comfy)
    if verbose:
        print(f"\n{hi_(data['workflow'])}   {dim_(os.path.abspath(comfy))}\n")
        print(f"  models  {ok_(str(len(present))+' present')}   "
              f"{bad_(str(len(missing))+' missing') if missing else ok_('0 missing')}   "
              f"{dim_(str(len(manual))+' manual') if manual else ''}")
        for s in missing:
            print(bad_(f"     missing  ") + f"{s['name']}  -> models/{s['dest']}/")
        for s in manual:
            print(dim_(f"     manual   {s['name']}  ({s['page']})"))
        print(f"  nodes   {ok_(str(len(have_n))+' present')}   "
              f"{bad_(str(len(need_n))+' missing') if need_n else ok_('0 missing')}")
        for n in need_n:
            print(bad_(f"     missing  ") + f"{n['name']}  ({n['git']})")
        print()
    return data, present, missing, manual, have_n, need_n

# ---------- download ----------

def download(url, dest_path, token=None):
    tmp = dest_path + ".part"
    have = os.path.getsize(tmp) if os.path.exists(tmp) else 0
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if have:
        req.add_header("Range", f"bytes={have}-")
    try:
        resp = urllib.request.urlopen(req, timeout=60)
    except urllib.error.HTTPError as e:
        if e.code == 416 and have:
            os.replace(tmp, dest_path); return True, "already complete"
        if e.code in (401, 403):
            return False, "gated - set HF_TOKEN and accept the model licence on HuggingFace"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:70]
    total = have + int(resp.headers.get("Content-Length", 0))
    done = have
    with open(tmp, "ab" if have else "wb") as fh:
        while True:
            chunk = resp.read(1 << 20)
            if not chunk: break
            fh.write(chunk); done += len(chunk)
            if total:
                bar = ("#" * (done * 24 // total)).ljust(24)
                sys.stdout.write(f"\r      [{bar}] {human(done)}/{human(total)}   ")
                sys.stdout.flush()
    sys.stdout.write("\r" + " " * 60 + "\r")
    # guard against a saved HTML error page
    if total and done < 1024 and open(tmp, "rb").read(1) == b"<":
        os.remove(tmp); return False, "got an HTML page, not a file"
    os.replace(tmp, dest_path)
    return True, "done"

def get(workflow, comfy, optional=False, dry=False):
    data = load(workflow)
    present, missing, manual = scan(data, comfy)
    token = os.environ.get("HF_TOKEN")
    todo = [s for s in missing if s.get("required") or optional]
    skipped_opt = [s for s in missing if not s.get("required") and not optional]
    print(f"\n{hi_(data['workflow'])}  ->  {dim_(os.path.abspath(comfy))}")
    print(f"{len(present)} already present, {len(todo)} to download"
          f"{'' if optional else dim_('  (add --optional for extras)')}\n")
    done = fail = 0
    for s in todo:
        dest_dir = os.path.join(comfy, "models", s["dest"])
        dest = os.path.join(dest_dir, s["name"])
        print(f"  {s['name']}{'' if s.get('required') else dim_(' (optional)')}  -> models/{s['dest']}/")
        if s.get("note"): print(dim_(f"      {s['note']}"))
        if dry:
            print(dim_(f"      would GET {s['url']}\n")); continue
        os.makedirs(dest_dir, exist_ok=True)
        good, msg = download(s["url"], dest, token)
        print((ok_("      " + msg) if good else bad_("      FAILED: " + msg + "\n      " + s["url"])) + "\n")
        done += good; fail += not good
    print("-" * 60)
    print(f"{ok_(str(done)+' downloaded')}   {bad_(str(fail)+' failed') if fail else '0 failed'}"
          f"   {dim_(str(len(skipped_opt))+' optional skipped') if skipped_opt else ''}")
    if manual:
        print("\n" + hi_("Grab these by hand") + " (no reliable direct link yet):")
        for m in manual:
            print(f"  - {m['name']}  -> models/{m['dest']}/")
            print(dim_(f"      {m.get('note','')}\n      {m['page']}"))
    print(dim_("\nHelpers like rife49.pth / RealESRGAN ship with the custom nodes, not here."))
    return fail == 0

# ---------- nodes ----------

def install_nodes(workflow, comfy, dry=False):
    data = load(workflow)
    have, need = scan_nodes(data, comfy)
    if not need:
        print(ok_(f"\nAll {len(have)} custom nodes for {workflow} are already installed.")); return True
    if not _has_git():
        print(bad_("\ngit is not installed, so nodes can't be auto-installed."));
        for n in need: print(f"  clone {n['git']}  into  {comfy}/custom_nodes/")
        return False
    cn = os.path.join(comfy, "custom_nodes")
    os.makedirs(cn, exist_ok=True)
    print(f"\nInstalling {len(need)} node(s) into {dim_(cn)}\n")
    fail = 0
    for n in need:
        print(f"  {n['name']}  ({n['git']})")
        if dry: print(dim_("      would git clone\n")); continue
        r = subprocess.run(["git", "clone", "--depth", "1", n["git"], os.path.join(cn, n["name"])],
                           capture_output=True, text=True)
        print((ok_("      cloned") if r.returncode == 0 else bad_("      FAILED: " + r.stderr.strip()[:80])) + "\n")
        fail += r.returncode != 0
    print(dim_("Install the nodes' requirements.txt if ComfyUI reports missing imports, then restart."))
    return fail == 0

def _has_git():
    try:
        return subprocess.run(["git", "--version"], capture_output=True).returncode == 0
    except Exception:
        return False

# ---------- ComfyUI process ----------

def comfy_running():
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{PORT}/system_stats", timeout=2)
        return True
    except Exception:
        return False

def _comfy_python(comfy):
    for p in (os.path.join(comfy, ".venv", "Scripts", "python.exe"),
              os.path.join(comfy, ".venv", "bin", "python"),
              os.path.join(os.path.dirname(comfy), "python_embeded", "python.exe")):
        if os.path.isfile(p):
            return p
    return sys.executable

def launch_comfy(comfy):
    if comfy_running():
        print(ok_(f"\nComfyUI is already running at http://127.0.0.1:{PORT}"))
        print("New models show up after you hit " + hi_("Refresh") + " (or the R key) in the UI. "
              "A new workflow node set needs a full restart.")
        return
    py = _comfy_python(comfy)
    print(f"\nStarting ComfyUI: {dim_(py + ' main.py')}  (cwd {comfy})")
    kwargs = {"cwd": comfy}
    if os.name == "nt":
        kwargs["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True
    try:
        subprocess.Popen([py, "main.py"], **kwargs)
    except Exception as e:
        print(bad_(f"Could not launch: {e}\nStart it yourself: cd {comfy} && python main.py")); return
    print("Launching... open " + hi_(f"http://127.0.0.1:{PORT}") + " in a minute.")

# ---------- interactive ----------

def menu(comfy_cli):
    all_wf = list(manifests())
    print(hi_("\nThe_frizzy1 workflow setup\n"))
    comfy = find_comfy(comfy_cli, quiet=True)
    print("ComfyUI: " + (ok_(comfy) if comfy else bad_("not found - I'll ask when needed")))
    print("\nWorkflows:")
    for i, w in enumerate(all_wf, 1):
        print(f"  {i:2d}. {w}")
    pick = input("\nPick a number (or q to quit): ").strip()
    if pick.lower() in ("q", ""): return
    try:
        wf = all_wf[int(pick) - 1]
    except Exception:
        print(bad_("not a valid choice")); return
    if not comfy:
        comfy = need_comfy(comfy_cli)
    status(wf, comfy)
    print("What now?")
    print("  1. Download missing models (required)")
    print("  2. Download missing models (+ optional)")
    print("  3. Install missing custom nodes")
    print("  4. Do it all, then launch ComfyUI")
    print("  5. Just launch / check ComfyUI")
    a = input("Choice: ").strip()
    if a == "1": get(wf, comfy)
    elif a == "2": get(wf, comfy, optional=True)
    elif a == "3": install_nodes(wf, comfy)
    elif a == "4":
        get(wf, comfy, optional=True); install_nodes(wf, comfy)
        status(wf, comfy); launch_comfy(comfy)
    elif a == "5": launch_comfy(comfy)

# ---------- cli ----------

def main():
    ap = argparse.ArgumentParser(description="Find ComfyUI, install a The_frizzy1 workflow's models + nodes.")
    ap.add_argument("command", nargs="?", choices=["status", "get", "nodes", "doctor", "find", "menu"], default="menu")
    ap.add_argument("workflow", nargs="?", help="e.g. wan2.2/animate")
    ap.add_argument("--comfy", help="Path to your ComfyUI folder.")
    ap.add_argument("--optional", action="store_true", help="Also fetch optional files.")
    ap.add_argument("--dry-run", action="store_true", help="Show actions, change nothing.")
    a = ap.parse_args()

    if a.command == "menu":
        return menu(a.comfy)
    if a.command == "find":
        p = find_comfy(a.comfy)
        print(ok_(f"ComfyUI: {p}") if p else bad_("Not found. Pass --comfy \"C:/path/to/ComfyUI\".")); return
    if not a.workflow:
        sys.exit("Name a workflow, e.g.: python scripts/frizzy.py " + a.command + " wan2.2/animate")
    comfy = need_comfy(a.comfy)
    if a.command == "status":
        status(a.workflow, comfy)
    elif a.command == "get":
        get(a.workflow, comfy, optional=a.optional, dry=a.dry_run)
    elif a.command == "nodes":
        install_nodes(a.workflow, comfy, dry=a.dry_run)
    elif a.command == "doctor":
        _, _, missing, manual, _, need_n = status(a.workflow, comfy)
        if missing: get(a.workflow, comfy, optional=a.optional)
        if need_n: install_nodes(a.workflow, comfy)
        status(a.workflow, comfy)
        if input("Launch ComfyUI now? [y/N] ").strip().lower() == "y":
            launch_comfy(comfy)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped.")

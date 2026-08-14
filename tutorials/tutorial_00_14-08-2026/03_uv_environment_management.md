# Part 3 — uv: Python Environments Without the Pain

> **Author:** Shuvam Banerji Seal


> **Goal:** master `uv` — the modern tool that replaces `venv` + `pip` +
> `requirements.txt` with two files (`pyproject.toml`, `uv.lock`) and a handful
> of commands.

---

## 3.1 The problem uv solves

Classic Python dependency management is fragile:

```bash
python -m venv .venv                 # create env
source .venv/bin/activate            # activate it
pip install numpy mdtraj             # install packages
pip freeze > requirements.txt        # pray this captures everything
```

`pip freeze` captures your *entire* environment — including packages you did not
mean to install — and `requirements.txt` has no notion of Python version,
platform, or dev-vs-runtime dependencies. Environments rot.

**uv** (by Astral, the Ruff team) is a single, very fast binary that manages:

- **Python interpreters** (`uv python install`)
- **Virtual environments** (`uv venv`)
- **Dependencies** (`uv add` / `uv remove` / `uv sync`)
- **Locking** (`uv lock`) — exact versions for every transitive dependency
- **Running tools** (`uv run`, `uvx`)

One mental model, one tool, ~10–100× faster than pip.

---

## 3.2 Installation (all operating systems)

### 🐧 Linux

```bash
# Option A — official installer (recommended, works on any distro)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Option B — apt (Debian / Ubuntu)
sudo apt update && sudo apt install uv

# Option C — pip (fallback; install inside a venv to keep your system clean)
pip install uv
```

### 🍎 macOS

```bash
# Option A — official installer (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Option B — Homebrew
brew install uv
```

### 🪟 Windows

```powershell
# Option A — PowerShell (recommended)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.sh | iex"

# Option B — winget (Windows Package Manager)
winget install --id=astral-sh.uv

# Option C — pip
pip install uv
```

### Verify on any OS

```bash
uv --version      # e.g. "uv 0.12.2"
```

> 💡 After installing, close and reopen your terminal (or run
> `source ~/.bashrc` on Linux/macOS) so the new `uv` binary is on your `PATH`.
> Windows users: restart the terminal or re-open PowerShell.

### Add uv to your PATH (`.bashrc` / `.zshrc`)

The official installer normally adds `~/.local/bin` to your `PATH` for you. If
you get `uv: command not found` after installing (common with older shells,
non-interactive terminals, or manual installs), add the directory by hand.

**Where uv actually lives, per install method:**

| Install method | Binary location |
|----------------|-----------------|
| Official installer (`curl … \| sh`) | `~/.local/bin/uv` |
| Homebrew (macOS) | `/opt/homebrew/bin/uv` (Apple Silicon) or `/usr/local/bin/uv` (Intel) |
| `cargo install uv` | `~/.cargo/bin/uv` |
| Windows installer / winget | `%USERPROFILE%\.local\bin\uv.exe` (usually on PATH automatically) |

**Bash — edit `~/.bashrc`:**

```bash
# add this line (at the end of ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"
```

Then apply it:

```bash
source ~/.bashrc
```

**Zsh — edit `~/.zshrc`:**

```zsh
# add this line (at the end of ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

Then apply it:

```zsh
source ~/.zshrc
```

**Verify from a fresh terminal:**

```bash
which uv        # should print the path, e.g. /home/you/.local/bin/uv
uv --version    # should print, e.g. uv 0.12.2
```

> 🔎 **Diagnostic:** `echo $PATH` shows the current search path. If
> `~/.local/bin` is missing from it, the `export PATH=…` line above is exactly
> what you need. Don't forget to also check `~/.profile` / `~/.bash_profile` —
> some setups load those instead of `.bashrc`.

---

---

## ⭐ The main commands of this session

If you remember nothing else from today, remember these three — they cover the
entire first-session workflow:

| Command | What it does |
|---------|--------------|
| `uv init` | Create a new project (scaffolds `pyproject.toml`, `src/`, `.gitignore`, `.python-version`) |
| `uv add`  | Add a dependency (updates `pyproject.toml` **and** `uv.lock`, then syncs the env) |
| `uv sync` | Build the environment & install everything from the lockfile |

Minimal session-00 demo:

```bash
uv init demo && cd demo                       # 1. create the project
uv add numpy mdtraj                           # 2. declare dependencies
uv sync                                       # 3. install them into .venv/
uv run python -c "import numpy, mdtraj; print('environment ready')"
```

That is the entire lifecycle of a Python project in four commands.
Sections 3.4 and 3.5 walk through each one in detail.

---

## 3.3 The two-file contract

| File | Who writes it | What it is |
|------|---------------|------------|
| `pyproject.toml` | **You** (or `uv init`) | Declarative metadata + dependencies |
| `uv.lock` | **uv** (machine-generated) | Exact resolved versions of *everything* |

Commit **both**. `uv.lock` is the reproducibility contract: anyone who runs
`uv sync` gets byte-identical dependencies.

---

## 3.4 Your first project — `uv init` → `uv sync`

```bash
uv init my_project
cd my_project
```

`uv init` scaffolds a ready-to-run project:

```
my_project/
├── .python-version        # e.g. 3.13
├── README.md
├── pyproject.toml         # name, version, requires-python, deps
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py        # prints "Hello from my_project!"
└── .gitignore             # uv-aware (ignores .venv/)
```

Now create the environment and install everything:

```bash
uv sync
```

That single command: creates `.venv/`, resolves dependencies, writes `uv.lock`,
and installs the project itself (editable). **No activation needed** — use
`uv run` instead:

```bash
uv run python src/my_project/main.py
# Hello from my_project!
```

> 💡 **`uv run`** is the magic command: it uses the project's environment without
> requiring `source .venv/bin/activate`. You can also activate manually if you
> prefer: `source .venv/bin/activate`.

---

## 3.5 Adding & removing dependencies

```bash
uv add numpy              # add a runtime dependency
uv add "numpy>=2.0"       # with a version constraint
uv add mdtraj matplotlib  # several at once
uv add --dev pytest       # dev-only dependency (tests, linters)
uv remove mdtraj          # remove one
```

Each `uv add` edits `pyproject.toml` **and** updates `uv.lock` automatically,
then syncs the environment. Compare with pip, where this is three manual steps.

### What `pyproject.toml` looks like after `uv add numpy mdtraj`

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "mdtraj>=1.10",
    "numpy>=2.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

> 📌 **`uv add --dev pytest`** writes into `[dependency-groups] dev`. Dev-only
> tools (pytest, ruff, mypy) are installed by `uv sync` but never shipped with
> the package — and they are clearly separated from runtime dependencies.

---

## 3.6 Running code & tools

```bash
uv run python script.py        # run with the project env
uv run pytest                  # run a tool installed in the env
uv run python -c "import numpy; print(numpy.__version__)"
uvx ruff check .               # run a tool WITHOUT installing it (ephemeral)
```

`uvx` (uv's `npx`-equivalent) runs tools like `ruff`, `black`, or `mamba` in a
throwaway environment — nothing pollutes your project.

---

## 3.7 Environments, interpreters, and pinning

```bash
uv python list                 # interpreters uv can see
uv python install 3.12         # install a specific Python
uv python pin 3.12             # pin the project to 3.12 (writes .python-version)
uv venv                        # create a bare venv (no project needed)
uv venv --python 3.12          # ...with a specific interpreter
```

`uv sync` respects `.python-version` and `requires-python` — if your project
needs 3.12, uv downloads and uses exactly that.

---

## 3.8 Updating & upgrading

```bash
uv lock --upgrade              # re-resolve everything to the newest allowed
uv lock --upgrade-package numpy  # upgrade just one package
uv sync                        # apply the new lockfile
```

---

## 3.9 Reproducing someone else's project

```bash
git clone <url> && cd <project>
uv sync
```

That's it. No `pip install -r requirements.txt`, no "works on my machine".
If the repo has a `uv.lock`, you get *exactly* the versions the author used.

---

## 3.10 uv command reference

| Command | What it does |
|---------|--------------|
| `uv init [name]` | Scaffold a new project |
| `uv sync` | Create env + install deps from lockfile |
| `uv add <pkg>` | Add dependency (updates both files) |
| `uv remove <pkg>` | Remove dependency |
| `uv run <cmd>` | Run a command inside the project env |
| `uvx <tool>` | Run a tool in an ephemeral env |
| `uv lock` | (Re)generate `uv.lock` |
| `uv lock --upgrade` | Upgrade all locked versions |
| `uv python install <ver>` | Install a Python interpreter |
| `uv python pin <ver>` | Pin project interpreter |
| `uv venv` | Create a bare virtualenv |
| `uv tree` | Show the dependency tree |
| `uv cache clean` | Clear the global cache |

---

## 3.11 Worked example — a mini MD analysis project

```bash
uv init md_analysis && cd md_analysis
uv add numpy mdtraj matplotlib
uv run python - <<'EOF'
import numpy as np
import mdtraj as md

traj = md.load("traj.xtc", top="top.pdb")
rmsd = md.rmsd(traj, traj, 0)
print(f"frames: {traj.n_frames}, mean RMSD: {np.mean(rmsd):.3f} nm")
EOF
```

One environment, three packages, zero activation, fully locked. This is the
workflow you will use for every simulation project this semester.

## ✅ Check yourself

- What is the difference between `pyproject.toml` and `uv.lock`? Which do you
  hand-edit?
- Why is `uv run` preferred over `source .venv/bin/activate`?
- A collaborator's repo has no `uv.lock` — what command generates one?
- What does `uv add --dev pytest` do differently from `uv add pytest`?
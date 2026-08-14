# Getting Started

> **Course Instructor:** Dr. Susmita Roy · **TA:** Shuvam Banerji Seal

Everything in this repository is managed with [`uv`](https://docs.astral.sh/uv/),
the fast Python package & environment manager. This guide assumes you have
already worked through [tutorial 00](../tutorials/tutorial_00_14-08-2026/README.md);
if not, start there.

## 1. Prerequisites

| Tool    | Version   | Check with      |
|---------|-----------|-----------------|
| Python  | >= 3.12   | `python3 --version` |
| uv      | >= 0.5    | `uv --version`      |
| Git     | >= 2.40   | `git --version`     |
| gh (CLI)| >= 2.50   | `gh --version`      |

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv (macOS/Linux)
```

## 2. Clone & sync

```bash
git clone git@github.com:Shuvam-Banerji-Seal/CH4114_Molecular_Simulation_Tutorials.git
cd CH4114_Molecular_Simulation_Tutorials
uv sync
```

`uv sync` reads `pyproject.toml` + `uv.lock`, creates `.venv/`, and installs every
dependency — including the `dev` extras (pytest). One command, reproducible for
everyone.

## 3. Daily commands

```bash
uv run python -c "import ch4114; print(ch4114.__version__)"  # use the env
uv run pytest                                                # run tests
uv add <package>                                             # add a dependency
uv remove <package>                                          # remove a dependency
uv sync                                                      # re-sync after edits
uv python pin 3.12                                           # change interpreter
```

## 4. SSH — connect your terminal to GitHub (do this once)

```bash
ssh-keygen -t ed25519 -C "you@example.com"   # press Enter for all defaults
eval "$(ssh-agent -s)"                       # start the SSH agent
ssh-add ~/.ssh/id_ed25519                    # add your key to the agent
cat ~/.ssh/id_ed25519.pub                    # copy this line
```

1. Open https://github.com/settings/keys → **New SSH key**
2. Paste the key, give it a name (e.g. "my-laptop"), save.
3. Test: `ssh -T git@github.com` → you should see *"Hi <username>! You've
   successfully authenticated"*.

Now `git clone git@github.com:...`, `git push`, `git pull` need no passwords.
The same `.pub` key can be added to **GitLab** (*Settings → SSH Keys*) or
**Bitbucket** (*Personal settings → SSH keys*).

## 5. Updating dependencies

```bash
uv lock --upgrade        # recompute the lockfile against latest releases
uv sync                  # apply it
```

## 5b. Troubleshooting: the 3D plot window does not open

The plotting scripts auto-detect an interactive backend (TkAgg, QtAgg,
MacOSX) and fall back to the non-interactive `Agg` backend with a printed
message. If you see *"No interactive window available"* on a machine that has
a display:

1. **Stale `TCL_LIBRARY` / `TK_LIBRARY` exports** — recent uv-managed Python
   builds bundle **Tcl 9** and locate their own library automatically. An old
   `export TCL_LIBRARY=/usr/lib/tcl8.6` in `~/.bashrc` / `~/.zshrc` forces a
   version conflict (`have 9.0.4, need exactly 8.6.16`). Comment those lines
   out and open a new terminal.
2. **Python build without a bundled Tcl** — if you still get
   *"Cannot find a usable init.tcl"*, pin a Python whose build bundles the
   Tcl library: `uv python pin 3.12` (this repo's default) and
   `uv sync` again.
3. **No GUI toolkit at all** (headless server) — install one:
   `uv add --dev PySide6` (QtAgg) or use the Jupyter notebook with
   `%matplotlib widget`.

## 6. Where do the tutorials live?

Every session is a date-stamped folder under `tutorials/`:

```
tutorials/
├── tutorial_00_14-08-2026/   # tooling, NumPy & Matplotlib, lattice structures
└── TEMPLATE.md               # copy this to start a new session
```

New sessions are scaffolded with:

```bash
uv run python scripts/new_tutorial.py --number 01 --date 21-08-2026
```

## 7. Session 00 — what is inside

| # | Topic | Markdown | Slides | Code |
|---|-------|----------|--------|------|
| 1 | Git & GitHub | `01_git_and_github.md` | `slides/01_git_and_github/` | — |
| 2 | Project organization | `02_project_organization.md` | `slides/02_project_organization/` | — |
| 3 | uv environments | `03_uv_environment_management.md` | `slides/03_uv_environment_management/` | `examples/uv_demo/` |
| 4 | NumPy & Matplotlib | `04_numpy_and_matplotlib.md` | `slides/04_numpy_and_matplotlib/` | `examples/numpy_matplotlib/` + `notebooks/` |
| 5 | Lattice structures | `05_lattice_structures.md` | `slides/05_lattice_structures/` | `examples/lattice_structures/` + `notebooks/` |

### Notebooks (`.ipynb`)

Run them in Jupyter:

```bash
uv add --dev jupyter ipympl      # once
uv run jupyter notebook notebooks/04_numpy_basics.ipynb
```

| Notebook | Covers |
|----------|--------|
| `notebooks/04_numpy_basics.ipynb` | arrays, `np.random`, `np.linspace`, `np.radians`, `np.zeros_like`, indexing |
| `notebooks/05_matplotlib_plotting.ipynb` | 2D & 3D plots, subplots, colors, titles, legends |
| `notebooks/06_lattice_structures.ipynb` | SCC/BCC/FCC in 2D & 3D, packing fractions, interactive rotation |

### Scripts (`.py`)

Plain Python files you can run directly:

```bash
uv run python examples/numpy_matplotlib/numpy_basics.py
uv run python examples/numpy_matplotlib/matplotlib_plots.py
uv run python examples/lattice_structures/lattice_2d.py
uv run python examples/lattice_structures/lattice_3d.py
uv run python examples/lattice_structures/packing_fraction.py
```

> 💡 **Sign your code.** Every `.py` file starts with
> `__author__ = "Your Name"` and a `"""docstring"""` describing what it does —
> exactly like the files in this repo. This is how professionals credit their work.

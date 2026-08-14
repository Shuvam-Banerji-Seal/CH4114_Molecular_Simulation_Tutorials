# Tutorial 00 — Tooling, NumPy, Matplotlib & Lattices (14-08-2026)

> **Session date:** Friday, 14 August 2026 · **Duration:** ~6 h
>
> **Course Instructor:** Dr. Susmita Roy · **TA:** Shuvam Banerji Seal
>
> **Theme:** *Before we simulate anything, let's build a professional working
> environment.* Every molecular simulation project you will do this semester —
> LAMMPS runs, MD analysis notebooks, Monte Carlo scripts — deserves the same
> discipline as any software project: version control, a clean folder layout,
> reproducible Python environments, and solid NumPy/Matplotlib fundamentals.

---

## 🎯 Learning Outcomes

By the end of this session you will be able to:

- [ ] Explain what **Git** is and why version control is non-negotiable for research code
- [ ] Run the core Git workflow: `init → add → commit → branch → merge → push → pull`
- [ ] Use **GitHub** (web + `gh` CLI) and connect via **SSH keys**
- [ ] Lay out a **professional Python project structure** (`src/`, `tests/`, `docs/`, …)
- [ ] Create and manage **virtual environments with `uv`**
- [ ] Understand `uv init`, `pyproject.toml`, `uv sync`, `uv add`, `uv run`, `uv lock`
- [ ] Use **NumPy** arrays and key functions: `np.random`, `np.linspace`, `np.radians`, `np.zeros_like`, …
- [ ] Make **2D and 3D plots** with **Matplotlib**: subplots, colors, titles, legends
- [ ] Plot **SCC, BCC, FCC lattices** in 2D and 3D and **compute packing fractions**
- [ ] Sign every code file with `__author__` and document it with `"""docstrings"""`

---

## 📖 Session Materials

| Part | Topic | Markdown | Slides |
|------|-------|----------|--------|
| 1 | **Git & GitHub** — version control from zero to push (+ SSH keys) | [`01_git_and_github.md`](01_git_and_github.md) | [`slides/01_git_and_github/`](slides/01_git_and_github/) |
| 2 | **Organizing your project** — the professional folder layout | [`02_project_organization.md`](02_project_organization.md) | [`slides/02_project_organization/`](slides/02_project_organization/) |
| 3 | **uv & Python environments** — virtualenvs without the pain | [`03_uv_environment_management.md`](03_uv_environment_management.md) | [`slides/03_uv_environment_management/`](slides/03_uv_environment_management/) |
| 4 | **NumPy & Matplotlib** — arrays, random numbers, and plotting | [`04_numpy_and_matplotlib.md`](04_numpy_and_matplotlib.md) | [`slides/04_numpy_and_matplotlib/`](slides/04_numpy_and_matplotlib/) |
| 5 | **Lattice structures** — SCC / BCC / FCC in 2D & 3D, packing fractions | [`05_lattice_structures.md`](05_lattice_structures.md) | [`slides/05_lattice_structures/`](slides/05_lattice_structures/) |

## 🎞️ Slides (Beamer, 16:9)

| Deck | Source (`.tex`) | Compiled (`.pdf`) |
|------|-----------------|-------------------|
| 1 — Git & GitHub | [`slides/01_git_and_github/slides_01_git_and_github.tex`](slides/01_git_and_github/slides_01_git_and_github.tex) | [`slides_01_git_and_github.pdf`](slides/01_git_and_github/slides_01_git_and_github.pdf) |
| 2 — Project organization | [`slides/02_project_organization/slides_02_project_organization.tex`](slides/02_project_organization/slides_02_project_organization.tex) | [`slides_02_project_organization.pdf`](slides/02_project_organization/slides_02_project_organization.pdf) |
| 3 — uv environments | [`slides/03_uv_environment_management/slides_03_uv_environment_management.tex`](slides/03_uv_environment_management/slides_03_uv_environment_management.tex) | [`slides_03_uv_environment_management.pdf`](slides/03_uv_environment_management/slides_03_uv_environment_management.pdf) |
| 4 — NumPy & Matplotlib | [`slides/04_numpy_and_matplotlib/slides_04_numpy_and_matplotlib.tex`](slides/04_numpy_and_matplotlib/slides_04_numpy_and_matplotlib.tex) | [`slides_04_numpy_and_matplotlib.pdf`](slides/04_numpy_and_matplotlib/slides_04_numpy_and_matplotlib.pdf) |
| 5 — Lattice structures | [`slides/05_lattice_structures/slides_05_lattice_structures.tex`](slides/05_lattice_structures/slides_05_lattice_structures.tex) | [`slides_05_lattice_structures.pdf`](slides/05_lattice_structures/slides_05_lattice_structures.pdf) |

> Compile with `pdflatex` (two passes). Build artifacts (`.aux`, `.log`, `.nav`, …)
> are git-ignored; only the `.tex` sources and `.pdf` outputs are committed.

## 💻 Code & Notebooks

| Topic | Scripts | Notebook |
|-------|---------|----------|
| NumPy | [`examples/numpy_matplotlib/numpy_basics.py`](examples/numpy_matplotlib/numpy_basics.py) | [`notebooks/04_numpy_basics.ipynb`](notebooks/04_numpy_basics.ipynb) |
| Matplotlib | [`examples/numpy_matplotlib/matplotlib_plots.py`](examples/numpy_matplotlib/matplotlib_plots.py) | [`notebooks/05_matplotlib_plotting.ipynb`](notebooks/05_matplotlib_plotting.ipynb) |
| Lattices | [`examples/lattice_structures/lattice_2d.py`](examples/lattice_structures/lattice_2d.py) · [`lattice_3d.py`](examples/lattice_structures/lattice_3d.py) · [`packing_fraction.py`](examples/lattice_structures/packing_fraction.py) | [`notebooks/06_lattice_structures.ipynb`](notebooks/06_lattice_structures.ipynb) |

Run scripts with uv:

```bash
uv run python examples/numpy_matplotlib/numpy_basics.py
uv run python examples/lattice_structures/lattice_3d.py
```

Run notebooks in Jupyter:

```bash
uv add --dev jupyter ipympl
uv run jupyter notebook notebooks/04_numpy_basics.ipynb
```

> 🖱️ The lattice notebook enables **interactive 3D rotation** (drag with your
> mouse) when run in Jupyter with `ipympl` installed.

## ⏱️ Session Plan

| Time  | Block                          | Material |
|-------|--------------------------------|----------|
| 00:00 | Why tooling matters (motivation) | slides / discussion |
| 00:20 | **Part 1 — Git & GitHub** (+ SSH) | `01_git_and_github.md` |
| 01:30 | **Part 2 — Project organization** | `02_project_organization.md` |
| 02:00 | **Part 3 — uv environments** | `03_uv_environment_management.md` |
| 02:40 | ☕ Break | — |
| 03:00 | **Part 4 — NumPy & Matplotlib** | `04_numpy_and_matplotlib.md` |
| 04:15 | **Part 5 — Lattice structures** | `05_lattice_structures.md` |
| 05:15 | Hands-on exercises | `exercises/` |
| 05:45 | Wrap-up, Q&A, next steps | — |

## ✏️ Exercises (work in pairs)

| # | Exercise | File | Est. |
|---|----------|------|------|
| 1 | Git basics: init → commit → branch → merge (+ SSH setup) | [`exercises/01_git_basics.md`](exercises/01_git_basics.md) | 20 min |
| 2 | Build a professional project skeleton | [`exercises/02_project_structure.md`](exercises/02_project_structure.md) | 15 min |
| 3 | uv workflow: init → add → sync → run | [`exercises/03_uv_workflow.md`](exercises/03_uv_workflow.md) | 25 min |
| 4 | NumPy + Matplotlib mini-project | [`exercises/04_numpy_matplotlib.md`](exercises/04_numpy_matplotlib.md) | 30 min |
| 5 | Lattice + packing-fraction mini-project | [`exercises/05_lattice_structures.md`](exercises/05_lattice_structures.md) | 30 min |

> **How to submit:** create a GitHub repo named `ch4114-tutorial00-<yourname>`,
> push your exercise work to it (via SSH!), and share the link.

## 🧰 Prerequisites

1. **Git** installed — check with `git --version`
2. **uv** installed — check with `uv --version` (install: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
3. A **GitHub account** (free) — create one at https://github.com
4. An **SSH key** added to GitHub (see `01_git_and_github.md`, section 1.7)
5. This repository cloned:

```bash
git clone git@github.com:Shuvam-Banerji-Seal/CH4114_Molecular_Simulation_Tutorials.git
cd CH4114_Molecular_Simulation_Tutorials
```

## 🏁 The whole session in one command

```bash
uv sync && uv run pytest
```

If that passes, your environment is ready — the rest of the session is learning
*why* it works. 🚀

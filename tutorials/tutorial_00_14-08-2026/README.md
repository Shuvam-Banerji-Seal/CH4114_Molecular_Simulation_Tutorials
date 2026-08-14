# Tutorial 00 — Tooling & Project Hygiene (14-08-2026)

> **Session date:** Friday, 14 August 2026 · **Duration:** ~3 h
>
> **Theme:** *Before we simulate anything, let's build a professional working
> environment.* Every molecular simulation project you will do this semester —
> LAMMPS runs, MD analysis notebooks, Monte Carlo scripts — deserves the same
> discipline as any software project: version control, a clean folder layout,
> and reproducible Python environments.

---

## 🎯 Learning Outcomes

By the end of this session you will be able to:

- [ ] Explain what **Git** is and why version control is non-negotiable for research code
- [ ] Run the core Git workflow: `init → add → commit → branch → merge → push → pull`
- [ ] Use **GitHub** (web + `gh` CLI) to host repos, open issues, and open pull requests
- [ ] Lay out a **professional Python project structure** (`src/`, `tests/`, `docs/`, …)
- [ ] Create and manage **virtual environments with `uv`**
- [ ] Understand `uv init`, `pyproject.toml`, `uv sync`, `uv add`, `uv run`, `uv lock`
- [ ] Reproduce someone else's environment with a single command (`uv sync`)

---

## 📖 Session Materials

| Part | Topic | File |
|------|-------|------|
| 1 | **Git & GitHub** — version control from zero to push | [`01_git_and_github.md`](01_git_and_github.md) |
| 2 | **Organizing your project** — the professional folder layout | [`02_project_organization.md`](02_project_organization.md) |
| 3 | **uv & Python environments** — virtualenvs without the pain | [`03_uv_environment_management.md`](03_uv_environment_management.md) |

## 🎞️ Slides (Beamer, 16:9)

| Part | Source (`.tex`) | Compiled (`.pdf`) |
|------|-----------------|-------------------|
| 1 — Git & GitHub | [`slides/01_git_and_github/slides_01_git_and_github.tex`](slides/01_git_and_github/slides_01_git_and_github.tex) | [`slides_01_git_and_github.pdf`](slides/01_git_and_github/slides_01_git_and_github.pdf) |
| 2 — Project organization | [`slides/02_project_organization/slides_02_project_organization.tex`](slides/02_project_organization/slides_02_project_organization.tex) | [`slides_02_project_organization.pdf`](slides/02_project_organization/slides_02_project_organization.pdf) |
| 3 — uv environments | [`slides/03_uv_environment_management/slides_03_uv_environment_management.tex`](slides/03_uv_environment_management/slides_03_uv_environment_management.tex) | [`slides_03_uv_environment_management.pdf`](slides/03_uv_environment_management/slides_03_uv_environment_management.pdf) |

> Compile with `pdflatex` (two passes). Build artifacts (`.aux`, `.log`, `.nav`, …)
> are git-ignored; only the `.tex` sources and `.pdf` outputs are committed.

## ⏱️ Session Plan

| Time  | Block                          | Material |
|-------|--------------------------------|----------|
| 00:00 | Why tooling matters (motivation) | slides / discussion |
| 00:20 | **Part 1 — Git & GitHub**       | `01_git_and_github.md` |
| 01:20 | **Part 2 — Project organization** | `02_project_organization.md` |
| 01:50 | **Part 3 — uv environments**    | `03_uv_environment_management.md` |
| 02:20 | Hands-on exercises              | `exercises/` |
| 02:50 | Wrap-up, Q&A, next steps        | — |

## ✏️ Exercises (work in pairs)

| # | Exercise | File | Est. |
|---|----------|------|------|
| 1 | Git basics: init → commit → branch → merge | [`exercises/01_git_basics.md`](exercises/01_git_basics.md) | 20 min |
| 2 | Build a professional project skeleton | [`exercises/02_project_structure.md`](exercises/02_project_structure.md) | 15 min |
| 3 | uv workflow: init → add → sync → run | [`exercises/03_uv_workflow.md`](exercises/03_uv_workflow.md) | 25 min |

> **How to submit:** create a GitHub repo named `ch4114-tutorial00-<yourname>`,
> push your exercise work to it, and share the link. That push *is* the exercise
> for Part 1.

## 🧰 Prerequisites

1. **Git** installed — check with `git --version`
2. **uv** installed — check with `uv --version` (install: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
3. A **GitHub account** (free) — create one at https://github.com
4. This repository cloned:

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

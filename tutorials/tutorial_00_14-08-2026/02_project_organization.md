# Part 2 — Organizing Your Project Like a Professional

> **Goal:** learn the standard Python project layout so that *anyone* (including
> future-you) can open your repo and know exactly where everything lives.

---

## 2.1 Why folder structure matters

A simulation study generates: scripts, data, figures, notebooks, notes, and
dependencies. Dump them all in one folder and within a week you cannot tell which
script produced which figure, or what packages the environment needs.

**A good structure answers three questions instantly:**

1. *Where is the code?* → `src/`
2. *Where are the tests?* → `tests/`
3. *What does this project need to run?* → `pyproject.toml` + `uv.lock`

---

## 2.2 The canonical layout (what this repo uses)

```
my_project/
├── README.md              # what it is, how to run it (the front page)
├── LICENSE                # who may use it, under what terms
├── pyproject.toml         # metadata + dependencies (the single source of truth)
├── uv.lock                # locked dependency versions (reproducibility)
├── .gitignore             # what Git must ignore (.venv/, caches, ...)
├── .python-version        # interpreter version (used by uv)
├── src/
│   └── my_project/        # importable package — `import my_project`
│       ├── __init__.py
│       ├── potentials.py
│       └── analysis.py
├── tests/                 # tests live OUTSIDE the package
│   └── test_potentials.py
├── docs/                  # prose: guides, notes, reports
├── scripts/               # one-off automation (not part of the package)
├── assets/                # figures, sample data, non-code resources
└── notebooks/             # exploratory Jupyter notebooks (optional)
```

### Why `src/`? (the "src-layout")

Putting your package inside `src/` prevents a classic bug: running Python from
the project root imports the *local* folder instead of the *installed* package,
so your tests may pass locally but fail elsewhere. With `src/`, the only way to
import `my_project` is the properly installed version. This is the layout used
by most modern Python projects.

### Why `tests/` outside the package?

Tests are not shipped code. Keeping them separate makes it obvious what is
*product* and what is *verification*.

---

## 2.3 What goes in each file — the contracts

| File | Contract |
|------|----------|
| `README.md` | 30-second explanation: what, why, how to run. Badges optional. |
| `pyproject.toml` | **Single source of truth** for name, version, Python version, dependencies. |
| `uv.lock` | Machine-generated; **commit it**. Pins every transitive dependency. |
| `.gitignore` | Never commit `.venv/`, `__pycache__/`, caches, secrets. |
| `LICENSE` | MIT for course work is a safe default. |
| `src/<pkg>/__init__.py` | Marks the folder as a package; often holds `__version__`. |

> **Rule of thumb:** if a file is generated (`.venv/`, caches, build artifacts),
> it does not belong in Git. If a file is *needed to reproduce the project*
> (`pyproject.toml`, `uv.lock`, source, tests), it must be committed.

---

## 2.4 Naming conventions (be consistent)

| Thing | Convention | Example |
|-------|-----------|---------|
| Repositories | `kebab-case` or `snake_case` | `CH4114_Molecular_Simulation_Tutorials` |
| Python packages | `snake_case` | `ch4114`, `mdtraj` |
| Python files | `snake_case` | `lj_potential.py` |
| Test files | `test_<module>.py` | `test_lj_potential.py` |
| Branches | `kebab-case` | `fix-neighbor-list` |
| Commit messages | imperative, ≤ 50 chars | `fix neighbor-list indexing` |
| Tutorial folders | `tutorial_<NN>_<DD-MM-YYYY>` | `tutorial_00_14-08-2026` |

### Commit message style

```
<type>: <short imperative summary>

# examples
feat: add Lennard-Jones potential module
fix: correct prefactor in Ewald summation
docs: explain thermostat choice in README
test: cover neighbor-list edge cases
```

---

## 2.5 A simulation-specific example

```
md_project/
├── README.md
├── pyproject.toml
├── uv.lock
├── src/md_project/
│   ├── __init__.py
│   ├── potentials.py      # LJ, Coulomb
│   ├── integrators.py     # Verlet, velocity-Verlet
│   ├── ensembles.py       # NVT/NPT thermostats & barostats
│   └── io.py              # read/write .xyz, .lammpstrj
├── tests/
│   ├── test_potentials.py
│   └── test_integrators.py
├── scripts/
│   └── run_benchmark.py   # one-off timing study
├── docs/
│   └── methodology.md     # what you did and why (write this!)
└── assets/
    └── figures/
```

Notice: **data and figures are not in Git** (they are large and regenerable) —
they live in `assets/` only when small, or outside the repo entirely. Scripts
that *produce* them are committed; the outputs are not.

---

## 2.6 Anti-patterns to avoid

| Anti-pattern | Why it hurts |
|--------------|--------------|
| `analysis_final_v2_really.py` | Version control exists — use it, not filename suffixes |
| Everything in one folder | No one (including you) can find anything |
| Committing `.venv/` | Huge, machine-specific, breaks for everyone else |
| No README | The repo is a black box |
| `pip freeze > requirements.txt` | Pins your *whole* machine, not your project |
| Editing `main` directly | No review, no history of intent |

## ✅ Check yourself

- Why does the package live under `src/` instead of the repo root?
- Which three files answer "what does this project need to run?"
- Name two things that must *never* be committed to Git.
# CH4114 — Molecular Simulation Tutorials

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![UV](https://img.shields.io/badge/uv-0.12%2B-5C9DEE?logo=astral)
![License](https://img.shields.io/badge/License-MIT-green)

Hands-on tutorials for **CH4114: Molecular Simulation**. Each session lives in its own
numbered, date-stamped folder under [`tutorials/`](tutorials/) and is built around a small,
reproducible Python project managed with [`uv`](https://docs.astral.sh/uv/).

---

## 📚 Tutorial Index

| Tutorial | Date | Topic | Status |
|----------|------|-------|--------|
| [`tutorial_00_14-08-2026`](tutorials/tutorial_00_14-08-2026/) | 14 Aug 2026 | Git, GitHub, project organization & UV environments | ✅ Live |
| `tutorial_01_...` | TBD | *Upcoming* | ⏳ |
| `tutorial_02_...` | TBD | *Upcoming* | ⏳ |

> **Naming convention:** `tutorial_<NN>_<DD-MM-YYYY>` — zero-padded session number, then
> the session date. Use [`scripts/new_tutorial.py`](scripts/new_tutorial.py) to scaffold a
> new session (see [`tutorials/TEMPLATE.md`](tutorials/TEMPLATE.md)).

---

## 🗂️ Repository Structure

```
CH4114_Molecular_Simulation_Tutorials/
├── README.md                  # ← you are here
├── pyproject.toml             # project metadata + dependencies (managed by uv)
├── uv.lock                    # locked, reproducible dependency graph
├── .python-version            # Python version used by uv
├── .gitignore                 # what NOT to commit
├── LICENSE                    # MIT
├── src/
│   └── ch4114/                # importable package: `import ch4114`
│       └── __init__.py
├── docs/                      # longer guides (setup, workflows)
├── scripts/                   # one-off automation (e.g. new_tutorial.py)
├── tests/                     # pytest suite
├── assets/                    # non-code resources (figures, data samples)
└── tutorials/
    ├── TEMPLATE.md            # blueprint for future sessions
    └── tutorial_00_14-08-2026/  # session 00: tooling & project hygiene
```

This layout is the **standard Python project convention**:

- `src/` — an installable package (`src`-layout prevents accidental imports of
  uninstalled code).
- `tests/` — tests live *outside* the package.
- `docs/` — prose, not code.
- `tutorials/` — this course's unique content, one folder per session.

---

## 🚀 Quickstart (first 10 minutes)

Everything in this repo is managed with `uv`. If you do not have it yet:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.sh | iex"
```

Then, inside the repository:

```bash
uv sync          # create the .venv + install deps from uv.lock (or resolve fresh)
uv run python -c "import ch4114; print(ch4114.__version__)"
uv run pytest    # run the test suite
```

That is the entire setup. No manual `python -m venv`, no `pip install` one by one —
see [tutorial 00, part 3](tutorials/tutorial_00_14-08-2026/03_uv_environment_management.md)
for the full walkthrough.

---

## 🎓 Session 00 in one screen

**Git & GitHub** — version control for everything you write:

```bash
git init
git add .
git commit -m "first commit"
git push -u origin main
```

**UV** — virtual environments without the pain:

```bash
uv init my_project && cd my_project
uv add numpy mdtraj
uv run python script.py
```

Full command references: [`01_git_and_github.md`](tutorials/tutorial_00_14-08-2026/01_git_and_github.md)
and [`03_uv_environment_management.md`](tutorials/tutorial_00_14-08-2026/03_uv_environment_management.md).

---

## 📄 License

Distributed under the [MIT License](LICENSE).

# Getting Started

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
uv python pin 3.13                                           # change interpreter
```

## 4. Updating dependencies

```bash
uv lock --upgrade        # recompute the lockfile against latest releases
uv sync                  # apply it
```

## 5. Where do the tutorials live?

Every session is a date-stamped folder under `tutorials/`:

```
tutorials/
├── tutorial_00_14-08-2026/   # tooling: Git, GitHub, project layout, uv
├── TEMPLATE.md               # copy this to start a new session
```

New sessions are scaffolded with:

```bash
uv run python scripts/new_tutorial.py --number 01 --date 21-08-2026
```

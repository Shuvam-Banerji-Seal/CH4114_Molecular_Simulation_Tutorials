# Exercise 3 — uv Workflow: init → add → sync → run

**Estimated time:** 25 min · **Work in pairs.**

## Objective

Reproduce the main session commands (`uv init`, `uv add`, `uv sync`) on a
realistic mini-analysis project, then prove reproducibility.

## Steps

### 1. Create the project

```bash
uv init md_analysis && cd md_analysis
ls -la          # inspect what uv scaffolded: pyproject.toml, src/, .gitignore, ...
uv run python src/md_analysis/main.py    # the scaffolded hello-world
```

### 2. Add the simulation stack

```bash
uv add numpy mdtraj matplotlib
uv add --dev pytest
cat pyproject.toml     # look at the dependencies section uv just edited
cat uv.lock | head -20 # look at the lockfile uv generated
```

### 3. Write and run a real script

Create `src/md_analysis/rmsd_report.py`:

```python
import numpy as np
import mdtraj as md

traj = md.load("traj.xtc", top="top.pdb") if False else None
# No trajectory at hand? Simulate a tiny one instead:
x = np.random.default_rng(42).normal(size=(10, 3, 3))  # 10 frames, 3 atoms
print(f"generated {x.shape[0]} frames, shape {x.shape}")
print("numpy + mdtraj + matplotlib all importable ✓")
```

Run it with the project environment:

```bash
uv run python src/md_analysis/rmsd_report.py
```

### 4. Prove reproducibility

- `git init && git add . && git commit -m "feat: md analysis skeleton"`
- Push to a GitHub repo (see Exercise 1).
- Your partner clones it, runs `uv sync`, and runs the script — **no other
  instructions**. If it works, the lockfile did its job.

### 5. (If you finish early)

- `uv add --dev ruff`, then `uvx ruff check .`
- `uv tree` — inspect the full dependency graph
- `uv lock --upgrade-package numpy` — bump just numpy, then `uv sync`

## Check-off

- [ ] `pyproject.toml` lists numpy, mdtraj, matplotlib; `dev` extra has pytest
- [ ] Partner reproduced your environment with only `uv sync`
- [ ] You can name the file that guarantees reproducibility (`uv.lock`)

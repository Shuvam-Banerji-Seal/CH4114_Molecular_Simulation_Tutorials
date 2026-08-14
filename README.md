# CH4114 — Molecular Simulation Tutorials

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![UV](https://img.shields.io/badge/uv-0.12%2B-5C9DEE?logo=astral)
![License](https://img.shields.io/badge/License-MIT-green)

Hands-on, **beginner-first** tutorials for **CH4114: Molecular Simulation**.
Every session lives in its own numbered, date-stamped folder under
[`tutorials/`](tutorials/) and is built around small, reproducible Python
projects managed with [`uv`](https://docs.astral.sh/uv/).

---

## 👩‍🏫 Course Team

| Role | Name |
|------|------|
| **Course Instructor** | **Dr. Susmita Roy** |
| **Teaching Assistant (TA)** | **Shuvam Banerji Seal** |

> Every code file in this repository is signed by its author with the
> `__author__` tag — e.g. `__author__ = "Shuvam Banerji Seal"` — so you can see
> exactly who wrote what. This is a professional habit: **always sign your code.**

---

## 📚 Tutorial Index

| Tutorial | Date | Topics | Status |
|----------|------|--------|--------|
| [`tutorial_00_14-08-2026`](tutorials/tutorial_00_14-08-2026/) | 14 Aug 2026 | Git · GitHub · Project organization · uv · NumPy & Matplotlib · Lattice structures | ✅ Live |
| `tutorial_01_...` | TBD | *Upcoming* | ⏳ |
| `tutorial_02_...` | TBD | *Upcoming* | ⏳ |

> **Naming convention:** `tutorial_<NN>_<DD-MM-YYYY>` — zero-padded session
> number, then the session date. Use [`scripts/new_tutorial.py`](scripts/new_tutorial.py)
> to scaffold a new session (see [`tutorials/TEMPLATE.md`](tutorials/TEMPLATE.md)).

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
├── docs/                      # longer guides (getting started)
├── scripts/                   # one-off automation (new_tutorial.py)
├── tests/                     # pytest suite
├── assets/                    # non-code resources (figures, data samples)
└── tutorials/
    ├── TEMPLATE.md            # blueprint for future sessions
    └── tutorial_00_14-08-2026/  # session 00: tooling + Python essentials
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
uv sync                                    # create .venv + install deps
uv run python -c "import ch4114; print(ch4114.__version__)"
uv run pytest                              # run the test suite
```

> ⚠️ If `uv: command not found`, add it to your `PATH` in `~/.bashrc` / `~/.zshrc`:
> `export PATH="$HOME/.local/bin:$PATH"` (see the
> [uv tutorial](tutorials/tutorial_00_14-08-2026/03_uv_environment_management.md)).

### Connect your terminal to GitHub with SSH (one-time setup)

```bash
ssh-keygen -t ed25519 -C "you@example.com"   # create a key (press Enter for defaults)
cat ~/.ssh/id_ed25519.pub                    # copy the output
```

Paste the key at **GitHub → Settings → SSH and GPG keys → New SSH key**, then
verify:

```bash
ssh -T git@github.com                        # should greet you by name
```

Now `git push` / `git pull` / `git clone git@github.com:...` all work without
passwords. The same key works for **GitLab**, **Bitbucket**, and any SSH server.
Full walkthrough: [`01_git_and_github.md`](tutorials/tutorial_00_14-08-2026/01_git_and_github.md).

---

## 🎓 Session 00 in one screen

**Git & GitHub** — version control for everything you write:

```bash
git init && git add . && git commit -m "first commit"
git push -u origin main
```

**UV** — virtual environments without the pain:

```bash
uv init my_project && cd my_project
uv add numpy mdtraj matplotlib
uv run python script.py
```

**NumPy & Matplotlib** — arrays, random numbers, and plots:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)          # 100 points from 0 to 2π
y = np.sin(x)
plt.plot(x, y, color="crimson")
plt.title("Sine wave")
plt.show()
```

**Lattice structures** — SCC / BCC / FCC unit cells with packing fractions:

```python
# FCC packing fraction = π / (3√2) ≈ 0.7405 — the most efficient packing
import numpy as np
pf_fcc = np.pi / (3 * np.sqrt(2))
print(f"FCC packing fraction = {pf_fcc:.4f}")
```

Full command references live in
[`tutorials/tutorial_00_14-08-2026/`](tutorials/tutorial_00_14-08-2026/).

---

## 📄 License

Distributed under the [MIT License](LICENSE).

# Exercise 1 — Git Basics: init → commit → branch → merge → push

**Estimated time:** 20 min · **Work in pairs.**

## Objective

Go through the complete Git lifecycle, then publish your work to GitHub.

## Steps

### 1. Configure Git (first time only)

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

### 2. Create and commit

```bash
mkdir git-exercise && cd git-exercise
git init
```

Create `potential.py` with a Lennard-Jones function:

```python
def lj_energy(r, epsilon=0.997, sigma=0.34):
    """Lennard-Jones potential energy (kJ/mol) at distance r (nm)."""
    sr = sigma / r
    return 4 * epsilon * (sr**12 - sr**6)
```

```bash
git status                 # file is untracked
git add potential.py
git commit -m "feat: add Lennard-Jones potential"
git log --oneline          # one commit in history
```

### 3. Branch and merge

```bash
git checkout -b feature-coulomb
```

Add a Coulomb term to the file, then:

```bash
git add potential.py
git commit -m "feat: add Coulomb term"
git checkout main
git merge feature-coulomb
git log --oneline --graph  # the merge shows in history
```

### 4. Publish to GitHub

```bash
gh repo create git-exercise --public --source . --push
gh repo view --web
```

### 5. (If you finish early) — trigger a merge conflict

On `main`, change line 2 of `potential.py` and commit. On a new branch, change
the *same* line differently and commit. Merge the branch into `main` and resolve
the conflict by hand. Fix it, `git add` + `git commit`.

## Check-off

- [ ] `git log --oneline --graph` shows at least 3 commits and a merge
- [ ] Your repo is live at `github.com/<you>/git-exercise`
- [ ] You can explain what the staging area is

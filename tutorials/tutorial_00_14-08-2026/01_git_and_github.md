# Part 1 — Git & GitHub

> **Author:** Shuvam Banerji Seal


> **Goal:** understand version control, master the core Git workflow, and publish
> your work to GitHub (web UI **and** `gh` CLI).

---

## 1.1 Why version control? (The research-code argument)

You will write analysis scripts for this course. Without version control, "backup"
means `analysis_final.py`, `analysis_final_v2.py`, `analysis_FINAL_v3_really.py` —
and the moment you delete a good version, it is gone forever.

Git solves this by keeping a **complete history** of every change:

```
commit 9f3a2b1  (HEAD -> main)
    Add MC acceptance criterion plot

commit 4c11e7d
    Fix neighbor-list indexing bug

commit a1b2c3d
    Initial LAMMPS analysis script
```

**What Git gives you:**

| Superpower | Why it matters for simulation work |
|------------|------------------------------------|
| **History** | See exactly what changed, when, and by whom |
| **Undo** | Revert to any past state of your code |
| **Branches** | Try a new idea without breaking working code |
| **Collaboration** | Merge work from multiple people cleanly |
| **Reproducibility** | Tag a commit = a snapshot you can cite/share |

> **Key mental model:** Git takes *snapshots* (commits) of your project. Your
> **working directory** → files you edit; the **staging area** → files you have
> marked for the next snapshot; the **repository** → all committed snapshots.

---

## 1.2 The core workflow (memorize this loop)

```bash
git init                    # 1. turn this folder into a repository (once)
git status                  # 2. what changed? (run this constantly)
git add <file>              # 3. stage changes
git commit -m "message"     # 4. snapshot them into history
```

```
Working dir ──git add──▶ Staging area ──git commit──▶ Repository (history)
      ▲                                                     │
      └────────────────── git checkout ◀────────────────────┘
```

**Do this every time you finish a meaningful chunk of work** — e.g. after a
working LJ potential script, not after every keystroke.

### First-time Git configuration (once per machine)

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

### Inspecting history

```bash
git log --oneline          # compact history: hash + message
git log --oneline --graph  # visualize branches
git status                 # current state
git diff                   # unstaged changes (what did I edit?)
git diff --staged          # staged changes
```

### Undoing (the three levels)

```bash
git restore <file>         # discard *unstaged* edits to a file
git restore --staged <file># unstage a file (keep the edits)
git commit --amend -m "better message"   # fix the last commit's message
```

---

## 1.3 Branching & merging

Branches let you experiment safely. The `main` branch stays clean; feature work
happens on a side branch.

```bash
git branch feature-lj      # create branch
git checkout feature-lj    # switch to it   (or: git switch feature-lj)
# ... work, commit, work, commit ...
git checkout main           # back to main
git merge feature-lj        # fold the branch's commits into main
git branch -d feature-lj    # delete the merged branch
```

```
        feature-lj
            │
    c1 ◀── c2 ◀── c3
    │                │
main                merge (c4)
    └────────────────┘
```

> **Golden rule:** never develop directly on `main` for anything collaborative.
> Short-lived branches + merge = a clean, readable history.

**Merge conflicts** happen when two branches edit the same lines. Git marks them:

```diff
<<<<<<< HEAD
E = 4 * eps * ((sigma/r)**12 - (sigma/r)**6)
=======
E = eps * ((sigma/r)**12 - (sigma/r)**6)   # ← I forgot the 4!
>>>>>>> feature-lj
```

Fix the file by hand, then:

```bash
git add <file>
git commit -m "resolve merge conflict in potential.py"
```

---

## 1.4 GitHub — hosting, sharing, collaborating

GitHub is a hosting service for Git repositories: a backup in the cloud, a
collaboration hub, and a public portfolio.

### Anatomy of a repository page

| Element | Purpose |
|---------|---------|
| **Code** | browse files, see commit history |
| **Issues** | bug reports, feature requests, task tracking |
| **Pull requests** | propose & review changes before merging |
| **Actions** | CI/CD — run tests automatically on every push |
| **README** | the front page of your project |

### Connecting local → remote

```bash
git remote add origin git@github.com:USERNAME/REPO_NAME.git
git push -u origin main        # -u remembers the upstream; push once
git push                       # ...and plain `git push` afterwards
git pull                       # fetch + merge remote changes
git clone <url>                # copy a remote repo to your machine
```

```
local commits ──git push──▶ GitHub (origin)
local commits ◀──git pull── GitHub (origin)
```

### Collaboration loop (issues → branches → PRs)

1. Open (or pick) an **issue** describing the task.
2. Create a branch: `git checkout -b fix-lj-preprint`
3. Commit, push: `git push -u origin fix-lj-preprint`
4. Open a **pull request** on GitHub: *"Closes #12 — fixes LJ prefactor"*
5. Reviewer comments; you push more commits; **merge**.
6. Pull the merged changes locally: `git pull`

---

## 1.5 The `gh` CLI — GitHub from your terminal

No clicking needed. Authenticate once:

```bash
gh auth login        # follow the prompts (SSH recommended)
gh auth status       # verify
```

**Daily commands:**

```bash
gh repo create my-repo --public --source . --push   # create + push current dir
gh repo clone USERNAME/REPO                         # same as git clone
gh issue create --title "Add MC code" --body "..."  # new issue
gh pr create --title "..." --body "..."             # new pull request
gh pr view --web                                    # open PR in browser
gh repo view --web                                  # open repo in browser
```

> 💡 **`gh repo create --source . --push`** is exactly how this repository was
> pushed to GitHub. One command: remote created, code pushed.

### Forking vs cloning

- **Clone** — copy a repo you can push to (you own it or are a collaborator).
- **Fork** — GitHub-side copy of someone else's repo, so you can propose changes
  via PR without write access. Standard for open-source contribution.

---

## 1.6 SSH keys — connect your terminal to GitHub (do this once)

SSH (Secure SHell) lets your terminal talk to GitHub without typing a password
on every push. You create a **key pair**: a *private* key that stays on your
machine (never share it!) and a *public* key that you upload to GitHub.

### Step 1 — generate the key

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

- `-t ed25519` → use the modern, secure Ed25519 algorithm
- `-C "you@example.com"` → a comment/label so you remember whose key it is
- Press **Enter** for the default location (`~/.ssh/id_ed25519`)
- Optionally set a passphrase (recommended); or press Enter twice for none

### Step 2 — start the SSH agent and add your key

```bash
eval "$(ssh-agent -s)"        # start the agent (macOS/Linux)
ssh-add ~/.ssh/id_ed25519     # register your key with the agent
```

### Step 3 — copy the PUBLIC key

```bash
cat ~/.ssh/id_ed25519.pub     # the .pub file is the public key — safe to share
```

### Step 4 — add it to GitHub

1. Go to **https://github.com/settings/keys**
2. Click **New SSH key**
3. Title: e.g. `my-laptop`
4. Paste the public key, click **Add SSH key**

### Step 5 — test the connection

```bash
ssh -T git@github.com
# Hi <your-username>! You've successfully authenticated, but GitHub does not
# provide shell access.
```

Now clone over SSH and push without passwords:

```bash
git clone git@github.com:USERNAME/REPO.git
```

> 🔑 **The same key works everywhere:** GitLab → *Settings → SSH Keys*,
> Bitbucket → *Personal settings → SSH keys*, any server with
> `ssh-copy-id user@server`. One key, many services.
>
> ⚠️ **Never** commit, email, or paste your *private* key (`id_ed25519`).
> Only the `.pub` file is meant to be shared.

---

## 1.7 Cheat sheet (print this)

```bash
# setup
git config --global user.name "Name"
git config --global user.email "mail@example.com"

# everyday
git status | git diff | git log --oneline
git add <file> | git add .        # stage one / stage all
git commit -m "msg"
git push | git pull

# branches
git branch <name>                 # create
git checkout -b <name>            # create + switch
git switch <name>                 # switch
git merge <name>                  # merge into current
git branch -d <name>              # delete (safe)

# undo
git restore <file>                # discard working-dir changes
git restore --staged <file>       # unstage
git commit --amend -m "msg"       # rewrite last commit message

# remote
git remote -v
git remote add origin <url>
git clone <url>

# github
gh auth login
gh repo create NAME --public --source . --push
gh pr create | gh issue create
```

## ✅ Check yourself

- What is the difference between `git add` and `git commit`?
- Your collaborator changed `main` while you worked on a branch — what two
  commands bring their changes into your branch?
- You committed a file with a typo'd message. One command fixes it — which?

# uv_demo

A tiny, fully `uv`-managed project used in [Tutorial 00](../) Part 3. It
calculates Lennard-Jones energies — the same potential you will meet in the
simulation sessions.

## Try it

```bash
uv sync
uv run python -m uv_demo
```

## What this demonstrates

| Command | File it touches | Result |
|---------|----------------|--------|
| `uv init uv_demo` | creates `pyproject.toml`, `src/`, `.gitignore`, `.python-version` | project scaffold |
| `uv add numpy` | edits `pyproject.toml` + `uv.lock` | dependency declared |
| `uv sync` | creates `.venv/` | environment ready |
| `uv run ...` | — | command runs in the env, no activation needed |

# Exercise 2 — Build a Professional Project Skeleton

**Estimated time:** 15 min · **Work in pairs.**

## Objective

Scaffold a clean `src`-layout Python project by hand — no generator allowed.
You will type every file so the structure sticks.

## Steps

Create this tree inside a new folder `my_sim_project`:

```
my_sim_project/
├── README.md
├── pyproject.toml
├── .gitignore
├── src/
│   └── my_sim_project/
│       └── __init__.py
└── tests/
    └── test_placeholder.py
```

1. **`pyproject.toml`** — name, version, `requires-python = ">=3.12"`, one
   dependency of your choice, and a dev extra with `pytest`.
2. **`.gitignore`** — ignore `.venv/`, `__pycache__/`, `.pytest_cache/`.
3. **`src/my_sim_project/__init__.py`** — a docstring and `__version__ = "0.1.0"`.
4. **`tests/test_placeholder.py`** — one trivial test (e.g. import the package
   and assert the version is a non-empty string).
5. **`README.md`** — 3 lines: what it is, how to set up, how to test.

Then swap partners: **without any explanation**, your partner must find, in under
2 minutes: (a) the dependencies, (b) the tests, (c) the install command. If they
can, your structure is good.

## Check-off

- [ ] Tree matches the spec exactly
- [ ] Partner found all three items in < 2 min
- [ ] You can say why `tests/` is outside the package

# Exercise 5 — Lattice Structures + Packing Fractions

**Estimated time:** 30 min · **Work in pairs.**
**Author:** Shuvam Banerji Seal

## Objective

Plot **BCC** and **FCC** unit cells in 3D (with the unit-cell cube drawn),
compute their packing fractions from the formulas, and verify with a tiny
Monte Carlo simulation.

## Steps

### 1. Setup

```bash
cd ~/git-exercise
uv init lattice_ex && cd lattice_ex
uv add numpy matplotlib
```

### 2. Write `lattice.py`

1. Define `unit_cell_atoms(kind)` — reuse the helper from
   `examples/lattice_structures/lattice_3d.py` (BCC: 8 corners + 1 center;
   FCC: 8 corners + 6 face centers).
2. Draw both unit cells side by side in **one figure** with two 3D subplots,
   including the 12 cube edges (`ax.plot`).
3. Compute the packing fractions from the formulas:
   - BCC: `(2 * (4/3) * pi * (a*sqrt(3)/4)**3) / a**3`
   - FCC: `(4 * (4/3) * pi * (a*sqrt(2)/4)**3) / a**3`
4. Verify **BCC** with Monte Carlo:
   - `np.random.seed(42)`, throw `200_000` points in the cube,
   - count points closer than `r` to any atom center,
   - print the fraction (should be ≈ 0.6802).
5. Print a table of formula vs Monte Carlo values.

> 💡 Sign your file with `__author__` and explain the code with comments —
> every line, just like the examples in this tutorial.

### 3. Submit

Commit and push to your `ch4114-tutorial00-<yourname>` repo.

## Check-off

- [ ] Script runs with `uv run python lattice.py`
- [ ] BCC Monte Carlo ≈ 0.6802 (± 0.005)
- [ ] Both 3D plots show the cube edges and correct atom positions
- [ ] File signed with `__author__` and a docstring

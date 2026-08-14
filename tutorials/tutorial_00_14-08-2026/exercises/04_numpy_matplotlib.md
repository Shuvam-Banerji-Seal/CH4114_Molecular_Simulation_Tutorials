# Exercise 4 — NumPy + Matplotlib Mini-Project

**Estimated time:** 30 min · **Work in pairs.**
**Author:** Shuvam Banerji Seal

## Objective

Use `np.linspace`, `np.random`, `np.radians`, `np.zeros_like` and Matplotlib
2D/3D plots to visualize a physical quantity — a **Lennard-Jones potential**.

## Steps

### 1. Setup

```bash
cd ~/git-exercise        # or your own project folder
uv init lj_plot && cd lj_plot
uv add numpy matplotlib
```

### 2. Write `lj_potential.py`

Create a script that:

1. Sets `np.random.seed(42)` and generates **50 random distances** with
   `np.random.uniform(0.3, 1.0, 50)`.
2. Builds a smooth distance axis with `np.linspace(0.3, 1.2, 200)`.
3. Computes the Lennard-Jones energy on both arrays:
   `E = 4 * eps * ((sigma/r)**12 - (sigma/r)**6)` with `sigma = 0.34`,
   `epsilon = 0.997`.
4. Plots:
   - the smooth curve (crimson, label `"LJ (smooth)"`),
   - the 50 random points (`scatter`, green, label `"random samples"`),
   - a legend, title **"Lennard-Jones potential"**, axis labels, grid.
5. Adds a **second subplot** showing the well region only:
   `r_well = np.linspace(0.32, 0.5, 100)`.
6. Prints `E.min()` and the distance at the minimum
   (`r[np.argmin(E)]`).

> 💡 Every file you write must start with a `"""docstring"""` and
> `__author__ = "Your Name"`.

### 3. Bonus (3D)

Add a third figure: a 3D scatter of 200 random points in a cube
(`np.random.rand(200, 3)`), colored by z with `cmap="viridis"`. Rotate it
with your mouse.

### 4. Submit

Commit and push to your `ch4114-tutorial00-<yourname>` repo.

## Check-off

- [ ] Script runs with `uv run python lj_potential.py`
- [ ] Both subplots + legend + title present
- [ ] The minimum matches the known well depth ≈ −0.997 kJ/mol
- [ ] File signed with `__author__` and a docstring

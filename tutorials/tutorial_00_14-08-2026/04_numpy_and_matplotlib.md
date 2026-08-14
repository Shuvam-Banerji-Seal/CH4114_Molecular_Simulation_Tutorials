# Part 4 — NumPy & Matplotlib: The Two Pillars of Scientific Python

> **Course Instructor:** Dr. Susmita Roy · **TA:** Shuvam Banerji Seal
> · **Author:** Shuvam Banerji Seal

> **Goal:** learn the NumPy functions you will use every single day in this
> course — `np.random`, `np.linspace`, `np.radians`, `np.zeros_like`, … — and
> how to turn numbers into beautiful 2D and 3D plots with Matplotlib.

---

## 4.1 Why these two packages?

- **NumPy** (Numerical Python) gives us *arrays* — fast, memory-efficient
  containers for numbers — plus a huge toolbox of math functions. Every
  simulation you run this semester will be built on NumPy arrays.
- **Matplotlib** turns arrays into figures. Molecular simulations produce
  *lots* of numbers; a plot is how you understand them.

```python
import numpy as np            # the standard short name
import matplotlib.pyplot as plt   # pyplot = the plotting interface
```

> 📌 **Rule:** these two imports are the first two lines of almost every
> scientific Python script you will ever write.

---

## 4.2 NumPy arrays — the basic data container

A NumPy **array** is like a list, but faster and math-aware:

```python
a = np.array([1, 2, 3, 4, 5])   # 1D array from a Python list
print(a)
print(a.shape)                  # (5,)  → 5 elements, one dimension
print(a.dtype)                  # int64 → the data type of the elements
```

**Indexing and slicing** (same rules as lists/strings):

```python
print(a[0])      # first element  → 1
print(a[-1])     # last element   → 5
print(a[1:4])    # elements 1..3  → [2 3 4]
```

**2D arrays** — a matrix, `shape = (rows, columns)`:

```python
m = np.array([[1, 2], [3, 4]])   # 2 rows, 2 columns
print(m.shape)                   # (2, 2)
print(m[0, 1])                   # row 0, column 1 → 2
```

---

## 4.3 Creating arrays: the big five

| Function | What it does | Example output |
|----------|--------------|----------------|
| `np.array([...])` | array from a list | `[1 2 3]` |
| `np.arange(start, stop, step)` | evenly spaced *integers* | `np.arange(0, 10, 2)` → `[0 2 4 6 8]` |
| `np.linspace(a, b, n)` | **n evenly spaced values** from a to b (inclusive) | `np.linspace(0, 1, 5)` → `[0. 0.25 0.5 0.75 1.]` |
| `np.zeros(shape)` / `np.ones(shape)` | array filled with 0 or 1 | `np.zeros((2, 3))` |
| `np.zeros_like(x)` / `np.ones_like(x)` | zeros/ones with the **same shape as x** | `np.zeros_like(positions)` |

```python
x = np.linspace(0, 2 * np.pi, 100)   # 100 points from 0 to 2π — ideal for plotting
zero_grid = np.zeros_like(x)         # same length as x, all zeros
print(len(x), x[0], x[-1])           # 100 0.0 6.283185307179586
```

> 🎯 **`np.linspace` is the single most-used NumPy function in this course.**
> Whenever you plot a curve, you generate x-values with `linspace`.

---

## 4.4 Random numbers: `np.random`

Simulations are full of randomness (Monte Carlo!). NumPy's random module covers
everything:

```python
np.random.seed(42)                    # ← set the seed for REPRODUCIBLE results!
```

| Function | What it gives you | Example |
|----------|-------------------|---------|
| `np.random.rand(n)` | n values uniform in [0, 1) | `[0.37 0.95 0.15]` |
| `np.random.randint(a, b, n)` | n random *integers* in [a, b) | `np.random.randint(0, 10, 5)` |
| `np.random.normal(mean, std, n)` | n values from a Gaussian | `np.random.normal(0, 1, 1000)` |
| `np.random.uniform(a, b, n)` | n values uniform in [a, b) | `np.random.uniform(-1, 1, 10)` |
| `np.random.choice(x, n)` | n random picks from x | `np.random.choice([0, 1], 10)` |

```python
np.random.seed(7)
positions = np.random.rand(3, 3)      # 3x3 grid of random numbers
print(positions)
```

> 🎯 **Always set the seed** (`np.random.seed(...)`) at the top of a script so
> your "random" results can be reproduced — the heart of scientific computing.

---

## 4.5 Angles: `np.radians` and `np.degrees`

Simulation code usually works in **radians**, but humans think in **degrees**:

```python
deg = 90
rad = np.radians(deg)     # degrees → radians   (90° = π/2 ≈ 1.5708)
back = np.degrees(rad)    # radians → degrees   (back to 90.0)

angles = np.linspace(0, 360, 37)          # 37 angles in degrees
x = np.cos(np.radians(angles))            # cos needs radians!
```

Useful constants & friends: `np.pi` (≈ 3.14159), `np.sqrt(2)`, `np.exp(1)`,
`np.sin`, `np.cos`, `np.tan`, `np.abs`, `np.sum`, `np.mean`, `np.max`, `np.min`.

---

## 4.6 Math on arrays (element-wise)

NumPy applies math to **every element at once** — no loops needed:

```python
r = np.linspace(0.3, 1.0, 50)                 # distances in nm
sigma, epsilon = 0.34, 0.997                  # LJ parameters
sr = sigma / r                                # divide EVERY element by r
lj = 4 * epsilon * (sr**12 - sr**6)           # the Lennard-Jones potential
print(lj.min(), lj.max())                     # quick stats of the whole array
```

This is the exact pattern you will use in the simulation sessions: generate a
range of values with `linspace`, then apply a formula to the whole array.

---

## 4.7 Matplotlib — your first 2D plot

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)                 # draw the curve
plt.title("Sine wave")         # title
plt.xlabel("angle (rad)")      # x-axis label
plt.ylabel("sin(x)")           # y-axis label
plt.grid(True)                 # grid lines
plt.show()                     # display the figure
```

**Colors, markers, and legend:**

```python
plt.plot(x, np.sin(x), color="crimson", label="sin")          # named color
plt.plot(x, np.cos(x), color="#2E86AB", linestyle="--", label="cos")  # hex color
plt.scatter(x[::10], np.sin(x[::10]), color="green", s=30)    # scatter points
plt.legend()                  # show the labels
plt.title("sin vs cos")
plt.show()
```

| Color ways | Examples |
|------------|----------|
| named color | `"red"`, `"blue"`, `"crimson"`, `"forestgreen"` |
| hex code | `"#2E86AB"`, `"#FF5733"` |
| RGB tuple | `(0.1, 0.4, 0.9)` |
| single letter | `'r'`, `'g'`, `'b'`, `'k'` (black) |

---

## 4.8 Two figures side by side: subplots

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))   # 1 row, 2 columns

axes[0].plot(x, np.sin(x), color="crimson")
axes[0].set_title("sin")                           # note: set_title inside axes
axes[0].set_xlabel("x")

axes[1].plot(x, np.cos(x), color="#2E86AB")
axes[1].set_title("cos")
axes[1].set_xlabel("x")

plt.tight_layout()     # fix overlapping labels
plt.show()
```

Grid of subplots: `plt.subplots(2, 2, figsize=(8, 8))` gives `axes[0,0]`,
`axes[0,1]`, `axes[1,0]`, `axes[1,1]`.

---

## 4.9 3D plots — surfaces and scatter

```python
from mpl_toolkits.mplot3d import Axes3D   # enables 3D axes (import once)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")   # ← projection="3d" makes it 3D!

# a surface: evaluate z = f(x, y) on a grid
u = np.linspace(-2, 2, 60)
X, Y = np.meshgrid(u, u)              # 2D grids of x and y coordinates
Z = np.exp(-(X**2 + Y**2))            # Gaussian "hill"

ax.plot_surface(X, Y, Z, cmap="viridis")   # color map for the surface
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_title("3D Gaussian")
plt.show()
```

- `np.meshgrid(x, y)` builds the full grid of (x, y) pairs for surfaces.
- `cmap="viridis"` (or `"plasma"`, `"coolwarm"`, `"magma"`) colors the surface.
- **3D scatter** (points, not surfaces): `ax.scatter(xs, ys, zs, s=50)`.

---

## 4.10 Rotating 3D plots with your mouse 🖱️

Matplotlib's 3D axes are **interactive by default** in any window/notebook:

- **Drag** with the left mouse button → rotate
- **Right-drag** → zoom
- **Scroll wheel** → zoom in/out

In a **script**, `plt.show()` opens a window you can rotate — the example
scripts in this repo auto-detect an interactive backend (TkAgg, QtAgg,
MacOSX) and fall back to the non-interactive Agg backend on headless servers.
In a **Jupyter notebook**, run the first cell with the widget backend:

```python
%matplotlib widget        # interactive figures in Jupyter (needs: uv add --dev ipympl)
```

If you prefer static images in the notebook, keep `%matplotlib inline`.

---

## 4.11 Script & notebook companion

| File | What it does |
|------|--------------|
| `examples/numpy_matplotlib/numpy_basics.py` | every NumPy command above, runnable |
| `examples/numpy_matplotlib/matplotlib_plots.py` | every plot above, runnable |
| `notebooks/04_numpy_basics.ipynb` | NumPy, with mermaid diagrams & explanations |
| `notebooks/05_matplotlib_plotting.ipynb` | Matplotlib, with mermaid diagrams & explanations |

```bash
uv run python examples/numpy_matplotlib/numpy_basics.py
uv run python examples/numpy_matplotlib/matplotlib_plots.py
```

---

## ✅ Check yourself

1. What is the difference between `np.arange(0, 10, 2)` and `np.linspace(0, 10, 2)`?
2. Why do we always call `np.random.seed(...)` before using `np.random`?
3. Which function converts degrees to radians? Why do we need it for `np.sin`?
4. What does `np.zeros_like(x)` return, and why is it useful?
5. How do you make a 1×3 grid of subplots? How do you make a 3D axes object?

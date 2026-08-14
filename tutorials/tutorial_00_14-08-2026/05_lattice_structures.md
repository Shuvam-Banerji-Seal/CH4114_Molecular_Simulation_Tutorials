# Part 5 — Lattice Structures: SCC, BCC, FCC in 2D & 3D

> **Course Instructor:** Dr. Susmita Roy · **TA:** Shuvam Banerji Seal
> · **Author:** Shuvam Banerji Seal

> **Goal:** draw the three classic crystal lattices — **SCC** (simple cubic),
> **BCC** (body-centered cubic), **FCC** (face-centered cubic) — in 2D and 3D
> with Matplotlib, and compute their **packing fractions** by hand and by code.

---

## 5.1 What is a crystal lattice?

A crystal is atoms arranged in a repeating pattern. The smallest repeating unit
is the **unit cell** — a cube of side length `a` (the *lattice constant*).

```
      unit cell (cube of side a)
      ┌─────────┐
     /│        /│
    / │       / │
   ┌─────────┐  │
   │  │      │  │
   │  └──────│──┘
   │ /       │ /
   │/        │/
   └─────────┘
```

| Lattice | Atoms per unit cell | Atom radius `r` (in units of `a`) | Coordination number |
|---------|--------------------:|----------------------------------:|--------------------:|
| **SCC** | 1 (8 corners × ⅛) | `a/2` | 6 |
| **BCC** | 2 (8 corners × ⅛ + 1 center) | `a√3/4` | 8 |
| **FCC** | 4 (8 corners × ⅛ + 6 faces × ½) | `a√2/4` | 12 |

> **Why these radii?** Neighboring atoms just touch. In SCC the corner atoms
> touch along the cube edge → `2r = a`. In BCC they touch along the body
> diagonal → `4r = a√3`. In FCC along the face diagonal → `4r = a√2`.

---

## 5.2 2D views of the unit cells

We plot the **top view** (looking down the z-axis) of each unit cell:

- **SCC** → one atom at each corner of a square.
- **BCC** → same corners, plus the center atom (the body center, seen from above).
- **FCC** → corners plus the four side-face centers (seen as edge midpoints)
  and the top-face center.

```python
import numpy as np
import matplotlib.pyplot as plt

a = 1.0                                   # lattice constant (nm)
corners = np.array([[0, 0], [a, 0], [a, a], [0, a]])   # 4 corners of the square

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, name in zip(axes, ["SCC", "BCC", "FCC"]):
    ax.scatter(corners[:, 0], corners[:, 1], s=200, color="steelblue")
    if name == "BCC":
        ax.scatter([a/2], [a/2], s=200, color="crimson")          # body center
    if name == "FCC":
        ax.scatter([a/2, a/2, 0, a], [0, a, a/2, a/2], s=200, color="crimson")  # face centers
    ax.set_title(f"{name} — top view")
    ax.set_xlim(-0.2, 1.2); ax.set_ylim(-0.2, 1.2)
    ax.set_aspect("equal")
plt.tight_layout()
plt.show()
```

---

## 5.3 Packing fraction in 2D

**Packing fraction** = *area occupied by atoms* ÷ *total area*. In 2D we treat
atoms as **circles** of radius `r`.

### Square lattice (SCC-like) → π/4 ≈ 0.7854

One square cell of side `a = 2r` contains one full circle (4 quarter-circles):

```
packing fraction = (π r²) / (2r)² = π/4 ≈ 0.7854
```

### Hexagonal lattice (FCC-like) → π/(2√3) ≈ 0.9069

The densest 2D packing — each hexagon cell of area `2√3 r²` holds one circle:

```
packing fraction = (π r²) / (2√3 r²) = π/(2√3) ≈ 0.9069
```

```python
import numpy as np

pf_square = np.pi / 4
pf_hex    = np.pi / (2 * np.sqrt(3))
print(f"square lattice : {pf_square:.4f}")
print(f"hexagonal      : {pf_hex:.4f}")
```

---

## 5.4 3D unit cells with Matplotlib

Now the real thing: scatter the atom positions inside a cube, then draw the
cube edges so the cell is visible.

```python
import numpy as np
import matplotlib.pyplot as plt

a = 1.0

def unit_cell_atoms(kind):
    """Return (x, y, z) atom coordinates for SCC, BCC or FCC."""
    corners = [(x, y, z) for x in (0, a) for y in (0, a) for z in (0, a)]
    if kind == "SCC":
        return np.array(corners)
    if kind == "BCC":
        return np.array(corners + [(a/2, a/2, a/2)])
    if kind == "FCC":
        faces = [(0, a/2, a/2), (a, a/2, a/2),   # x = 0 and x = a faces
                 (a/2, 0, a/2), (a/2, a, a/2),   # y = 0 and y = a faces
                 (a/2, a/2, 0), (a/2, a/2, a)]   # z = 0 and z = a faces
        return np.array(corners + faces)

fig = plt.figure(figsize=(14, 5))
for i, kind in enumerate(["SCC", "BCC", "FCC"], start=1):
    ax = fig.add_subplot(1, 3, i, projection="3d")
    atoms = unit_cell_atoms(kind)
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], s=120, color="steelblue")
    # draw the 12 edges of the cube
    for x in (0, a):
        for y in (0, a):
            ax.plot([x, x], [y, y], [0, a], color="black", lw=1)
    for x in (0, a):
        for z in (0, a):
            ax.plot([x, x], [0, a], [z, z], color="black", lw=1)
    for y in (0, a):
        for z in (0, a):
            ax.plot([0, a], [y, y], [z, z], color="black", lw=1)
    ax.set_title(f"{kind} unit cell")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
plt.tight_layout()
plt.show()
```

> 🖱️ **Drag the 3D plot with your mouse** to rotate it and inspect the atom
> positions from every angle. The example scripts automatically try to open
> an interactive window (TkAgg/QtAgg/MacOSX); on a headless server they fall
> back to the non-interactive Agg backend and print a message. In Jupyter use
> `%matplotlib widget` (see 4.10).

---

## 5.5 Packing fraction in 3D — the formulas

**Packing fraction** = *volume of atoms in the cell* ÷ *volume of the cell*.

| Lattice | Atoms/cell | Radius `r` | Packing fraction | Value |
|---------|-----------:|------------|------------------|------:|
| SCC | 1 | `a/2` | `(1 · 4/3 π r³) / a³ = π/6` | **0.5236** |
| BCC | 2 | `a√3/4` | `(2 · 4/3 π r³) / a³ = √3π/8` | **0.6802** |
| FCC | 4 | `a√2/4` | `(4 · 4/3 π r³) / a³ = π/(3√2)` | **0.7405** |

```python
import numpy as np

a = 1.0
pf_scc = (1 * (4/3) * np.pi * (a/2)**3)      / a**3
pf_bcc = (2 * (4/3) * np.pi * (a*np.sqrt(3)/4)**3) / a**3
pf_fcc = (4 * (4/3) * np.pi * (a*np.sqrt(2)/4)**3) / a**3

print(f"SCC: {pf_scc:.4f}   BCC: {pf_bcc:.4f}   FCC: {pf_fcc:.4f}")
# SCC: 0.5236   BCC: 0.6802   FCC: 0.7405
```

> 🏆 **FCC is the most efficient packing** (74.05%) — that is why many metals
> (copper, gold, aluminum) crystallize in FCC: it packs atoms most densely.

---

## 5.6 Verify the packing fraction numerically (Monte Carlo)

We can *check* the formulas with random numbers — a tiny Monte Carlo
simulation, and a perfect use of `np.random`:

```python
np.random.seed(42)
N = 200_000                                   # random points in the cube
pts = np.random.rand(N, 3) * a                # N points, each (x, y, z) in [0, a]

def inside_any(pts, centers, r):
    """True for points closer than r to ANY atom center."""
    inside = np.zeros(len(pts), dtype=bool)
    for c in centers:
        d = np.sqrt(((pts - c)**2).sum(axis=1))   # distance to this center
        inside |= d < r                           # mark points inside the sphere
    return inside

atoms = unit_cell_atoms("FCC")
r = a * np.sqrt(2) / 4
frac = inside_any(pts, atoms, r).mean()           # fraction of points inside
print(f"Monte Carlo FCC packing fraction ≈ {frac:.4f}  (formula: {pf_fcc:.4f})")
```

The random-point fraction matches the formula — the simulation agrees with the
math. This is exactly how Monte Carlo methods work in molecular simulation!

---

## 5.7 Script & notebook companion

| File | What it does |
|------|--------------|
| `examples/lattice_structures/lattice_2d.py` | 2D top views of SCC/BCC/FCC + 2D packing fractions |
| `examples/lattice_structures/lattice_3d.py` | 3D unit cells, interactive rotation |
| `examples/lattice_structures/packing_fraction.py` | formulas + Monte Carlo verification |
| `notebooks/06_lattice_structures.ipynb` | everything, with mermaid diagrams & explanations |

```bash
uv run python examples/lattice_structures/lattice_2d.py
uv run python examples/lattice_structures/lattice_3d.py
uv run python examples/lattice_structures/packing_fraction.py
```

---

## ✅ Check yourself

1. How many atoms does an FCC unit cell contain? Why 4, not 14?
2. Why is the BCC atom radius `a√3/4` and not `a/2`?
3. Which lattice has the highest packing fraction — SCC, BCC, or FCC?
4. What is the 2D packing fraction of a square lattice?
5. Why do we set `np.random.seed(...)` before the Monte Carlo check?
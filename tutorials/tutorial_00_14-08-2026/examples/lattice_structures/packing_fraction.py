"""
packing_fraction.py — packing fractions of SCC, BCC and FCC (CH4114).

We compute the packing fraction two ways:
  1. From the textbook formulas (atom volume / cell volume).
  2. With a tiny Monte Carlo simulation using np.random — random points
     are thrown into the unit cell and we count how many fall inside atoms.

How to run:
    uv run python examples/lattice_structures/packing_fraction.py

Author: Shuvam Banerji Seal
"""

__author__ = "Shuvam Banerji Seal"   # always sign your code!

# --- interactive window setup (so 3D plots can be rotated) ------------------
# matplotlib needs a "GUI backend" to open a window. We try the common ones
# in order (TkAgg uses tkinter, QtAgg uses PyQt/PySide, MacOSX is for macOS).
# Each candidate is TESTED by creating a real figure; if none works (e.g. on
# a headless server), we fall back to the non-interactive "Agg" backend.
import matplotlib

_interactive = False
for _backend in ("TkAgg", "QtAgg", "MacOSX", "GTK3Agg"):
    try:
        matplotlib.use(_backend, force=True)
        import matplotlib.pyplot as _plt
        _fig = _plt.figure()          # test: can a figure really be created?
        _plt.close(_fig)
        _interactive = True
        print(f"Interactive backend: {_backend} - drag 3D plots to rotate!")
        break
    except Exception:
        continue                      # this backend did not work, try the next

if not _interactive:
    print("No interactive window available - using the Agg backend (no popup).")
    matplotlib.use("Agg")
# ---------------------------------------------------------------------------

import numpy as np                # for the math
import matplotlib.pyplot as plt   # for the bar chart

A = 1.0   # lattice constant (nm)


def radius(kind: str) -> float:
    """Return the atom radius r (in units of a) for the given lattice."""
    if kind == "SCC":
        return A / 2              # atoms touch along the cube EDGE: 2r = a
    if kind == "BCC":
        return A * np.sqrt(3) / 4  # atoms touch along the BODY diagonal: 4r = a*sqrt(3)
    if kind == "FCC":
        return A * np.sqrt(2) / 4  # atoms touch along the FACE diagonal: 4r = a*sqrt(2)
    raise ValueError(f"Unknown lattice kind: {kind}")


def atoms_per_cell(kind: str) -> int:
    """Return how many FULL atoms a unit cell contains."""
    if kind == "SCC":
        return 1   # 8 corners x 1/8
    if kind == "BCC":
        return 2   # 8 corners x 1/8 + 1 center
    if kind == "FCC":
        return 4   # 8 corners x 1/8 + 6 faces x 1/2
    raise ValueError(f"Unknown lattice kind: {kind}")


def packing_fraction_formula(kind: str) -> float:
    """Packing fraction = (atoms_per_cell * volume_of_one_atom) / cell_volume."""
    n = atoms_per_cell(kind)              # how many atoms
    r = radius(kind)                      # radius of one atom
    atom_volume = (4 / 3) * np.pi * r**3  # volume of a sphere: 4/3 * pi * r^3
    return (n * atom_volume) / A**3       # divide by the cube's volume


def monte_carlo_packing(kind: str, n_points: int = 200_000) -> float:
    """Estimate the packing fraction by throwing random points at the cell."""
    np.random.seed(42)                    # reproducible "random" numbers

    # n_points random (x, y, z) positions, each between 0 and A.
    points = np.random.rand(n_points, 3) * A

    # Rebuild the atom centers inside the cell (same logic as lattice_3d.py).
    corners = [(x, y, z) for x in (0, A) for y in (0, A) for z in (0, A)]
    centers = list(corners)
    if kind == "BCC":
        centers.append((A / 2, A / 2, A / 2))
    if kind == "FCC":
        centers += [
            (0, A / 2, A / 2), (A, A / 2, A / 2),   # x = 0 and x = A faces
            (A / 2, 0, A / 2), (A / 2, A, A / 2),   # y = 0 and y = A faces
            (A / 2, A / 2, 0), (A / 2, A / 2, A),   # z = 0 and z = A faces
        ]

    r = radius(kind)
    inside = np.zeros(n_points, dtype=bool)   # which points are inside an atom?

    for c in centers:
        # Distance from every point to this atom center (Euclidean distance).
        distance = np.sqrt(((points - c) ** 2).sum(axis=1))
        inside = inside | (distance < r)      # mark points inside this sphere

    return inside.mean()   # fraction of points inside = packing fraction


def main() -> None:
    """Print both packing-fraction estimates and draw a bar chart."""
    kinds = ["SCC", "BCC", "FCC"]

    print("Packing fractions (volume of atoms / volume of unit cell):")
    print(f"{'lattice':<6} {'formula':>10} {'Monte Carlo':>12}")
    for kind in kinds:
        f_formula = packing_fraction_formula(kind)
        f_mc = monte_carlo_packing(kind)
        print(f"{kind:<6} {f_formula:>10.4f} {f_mc:>12.4f}")

    # A simple bar chart of the three formulas.
    values = [packing_fraction_formula(k) for k in kinds]
    plt.bar(kinds, values, color=["steelblue", "orange", "crimson"])
    plt.ylabel("packing fraction")
    plt.title("Packing fractions: SCC vs BCC vs FCC")
    plt.ylim(0, 0.9)
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v:.4f}", ha="center")   # value on top of each bar
    plt.show()

    print("FCC packs atoms most efficiently (74%) — the densest of the three!")


if __name__ == "__main__":
    main()

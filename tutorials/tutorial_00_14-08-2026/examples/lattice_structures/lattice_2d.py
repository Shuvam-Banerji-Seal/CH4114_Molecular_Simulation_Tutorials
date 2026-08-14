"""
lattice_2d.py — 2D views of the SCC, BCC and FCC unit cells (CH4114).

We draw the top view (looking down the z-axis) of each unit cell and
compute the 2D packing fractions of the square and hexagonal lattices.

How to run:
    uv run python examples/lattice_structures/lattice_2d.py

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
import matplotlib.pyplot as plt   # for the plotting


def main() -> None:
    """Draw the three 2D top views and print the 2D packing fractions."""
    a = 1.0   # lattice constant (we use 1 for simplicity)

    # The 4 corners of the unit cell square, as an array of (x, y) pairs.
    corners = np.array([[0, 0], [a, 0], [a, a], [0, a]])

    # One figure with 3 panels side by side.
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    # Loop over the three lattice types, drawing each one in its own panel.
    for ax, name in zip(axes, ["SCC", "BCC", "FCC"]):
        # Draw the corner atoms first (blue).
        ax.scatter(corners[:, 0], corners[:, 1], s=200, color="steelblue")

        if name == "BCC":
            # The body-centered atom sits at the middle of the square (seen from above).
            ax.scatter([a / 2], [a / 2], s=200, color="crimson")

        if name == "FCC":
            # Face-centered atoms: the 4 edge midpoints (side faces seen from
            # above) plus the center atom (the top face's center).
            ax.scatter([a / 2, a / 2, 0, a, a / 2], [0, a, a / 2, a / 2, a / 2],
                       s=200, color="crimson")

        ax.set_title(f"{name} — top view")
        ax.set_xlim(-0.2, 1.2)   # keep the atom circles fully visible
        ax.set_ylim(-0.2, 1.2)
        ax.set_aspect("equal")   # don't stretch the square into a rectangle

    plt.tight_layout()
    plt.show()

    # ------------------------------------------------------------------
    # 2D packing fractions: (area of one atom circle) / (area of the cell)
    # ------------------------------------------------------------------

    # Square lattice: cell side = 2r, one circle per cell -> pi/4.
    pf_square = np.pi / 4

    # Hexagonal lattice: the densest 2D packing -> pi / (2*sqrt(3)).
    pf_hex = np.pi / (2 * np.sqrt(3))

    print(f"2D packing fraction — square lattice : {pf_square:.4f}")
    print(f"2D packing fraction — hexagonal      : {pf_hex:.4f}")


if __name__ == "__main__":
    main()

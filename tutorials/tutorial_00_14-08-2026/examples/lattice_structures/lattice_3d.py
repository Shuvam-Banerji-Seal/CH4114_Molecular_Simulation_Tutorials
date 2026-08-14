"""
lattice_3d.py — 3D unit cells of the SCC, BCC and FCC lattices (CH4114).

We scatter the atom positions inside a cube and draw the 12 edges of the
cube so the unit cell is clearly visible.

How to run:
    uv run python examples/lattice_structures/lattice_3d.py

The figure opens in a window: DRAG with the mouse to rotate the 3D view,
scroll to zoom. (In a Jupyter notebook use %matplotlib widget instead.)

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

from mpl_toolkits.mplot3d import Axes3D   # enables 3D axes (import once)

A = 1.0   # lattice constant (nm) — we use 1 for simplicity


def unit_cell_atoms(kind: str) -> np.ndarray:
    """Return (x, y, z) atom coordinates inside the unit cell.

    kind: "SCC", "BCC" or "FCC".
    """
    # The 8 corners of the cube: every combination of x, y, z in {0, a}.
    corners = [(x, y, z) for x in (0, A) for y in (0, A) for z in (0, A)]

    if kind == "SCC":
        # Simple cubic: only the 8 corners.
        return np.array(corners)

    if kind == "BCC":
        # Body-centered cubic: corners + 1 atom at the cube center.
        return np.array(corners + [(A / 2, A / 2, A / 2)])

    if kind == "FCC":
        # Face-centered cubic: corners + 1 atom at the center of each of the
        # 6 cube faces. Face centers: (0, A/2, A/2) is the center of the
        # x=0 face, (A, A/2, A/2) of the x=A face, and so on.
        faces = [
            (0, A / 2, A / 2), (A, A / 2, A / 2),   # x = 0 and x = A faces
            (A / 2, 0, A / 2), (A / 2, A, A / 2),   # y = 0 and y = A faces
            (A / 2, A / 2, 0), (A / 2, A / 2, A),   # z = 0 and z = A faces
        ]
        return np.array(corners + faces)

    raise ValueError(f"Unknown lattice kind: {kind}")


def draw_cube_edges(ax) -> None:
    """Draw the 12 edges of the unit cell cube on the given 3D axes."""
    # 4 vertical edges: at each (x, y) corner, a line from z=0 to z=a.
    for x in (0, A):
        for y in (0, A):
            ax.plot([x, x], [y, y], [0, A], color="black", lw=1)

    # 4 edges along y: at each (x, z) corner.
    for x in (0, A):
        for z in (0, A):
            ax.plot([x, x], [0, A], [z, z], color="black", lw=1)

    # 4 edges along x: at each (y, z) corner.
    for y in (0, A):
        for z in (0, A):
            ax.plot([0, A], [y, y], [z, z], color="black", lw=1)


def main() -> None:
    """Draw the SCC, BCC and FCC unit cells side by side in 3D."""
    fig = plt.figure(figsize=(14, 5))

    # One 3D subplot per lattice type.
    for i, kind in enumerate(["SCC", "BCC", "FCC"], start=1):
        ax = fig.add_subplot(1, 3, i, projection="3d")
        atoms = unit_cell_atoms(kind)

        # Scatter the atoms. Column 0 = x, column 1 = y, column 2 = z.
        ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], s=120, color="steelblue")

        draw_cube_edges(ax)   # make the unit cell visible

        ax.set_title(f"{kind} unit cell")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

    plt.tight_layout()
    plt.show()

    # Quick summary of the atom counts.
    for kind in ["SCC", "BCC", "FCC"]:
        n = len(unit_cell_atoms(kind))
        print(f"{kind}: {n} atom positions plotted")

    print("Drag the 3D plot with your mouse to rotate it!")


if __name__ == "__main__":
    main()

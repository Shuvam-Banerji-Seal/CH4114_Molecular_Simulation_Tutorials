"""
matplotlib_plots.py — 2D and 3D plotting with Matplotlib for CH4114.

This script shows the plotting skills you need for this course:
a basic 2D line plot, colors + legend, subplots, a 3D surface,
and a 3D scatter plot.

How to run:
    uv run python examples/numpy_matplotlib/matplotlib_plots.py

A window will open for each figure. You can drag 3D plots with your mouse
to rotate them.

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


# ---------------------------------------------------------------------------
# 1. A basic 2D line plot
# ---------------------------------------------------------------------------

x = np.linspace(0, 2 * np.pi, 100)   # 100 x-values from 0 to 2*pi
y = np.sin(x)                        # sine of every x-value

plt.plot(x, y)                       # draw the curve
plt.title("Sine wave")               # give the figure a title
plt.xlabel("angle (radians)")        # label the x axis
plt.ylabel("sin(x)")                 # label the y axis
plt.grid(True)                       # add grid lines
plt.show()                           # display the figure

# ---------------------------------------------------------------------------
# 2. Colors, line styles, scatter points, and a legend
# ---------------------------------------------------------------------------

plt.plot(x, np.sin(x), color="crimson", label="sin")            # named color
plt.plot(x, np.cos(x), color="#2E86AB", linestyle="--", label="cos")  # hex color
plt.scatter(x[::10], np.sin(x[::10]), color="green", s=30)      # every 10th point
plt.legend()                       # show the labels in a legend box
plt.title("sin vs cos")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.show()

# ---------------------------------------------------------------------------
# 3. Subplots: two figures side by side
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(10, 4))   # 1 row, 2 columns of axes

axes[0].plot(x, np.sin(x), color="crimson")       # draw in the left axes
axes[0].set_title("sin")                          # note: set_title on the axes
axes[0].set_xlabel("x")

axes[1].plot(x, np.cos(x), color="#2E86AB")       # draw in the right axes
axes[1].set_title("cos")
axes[1].set_xlabel("x")

plt.tight_layout()    # stop labels from overlapping
plt.show()

# ---------------------------------------------------------------------------
# 4. A 3D surface plot
# ---------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D   # enables 3D axes (import once)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")   # projection="3d" makes it 3D!

u = np.linspace(-2, 2, 60)               # 60 values from -2 to 2
X, Y = np.meshgrid(u, u)                 # full grid of (x, y) pairs
Z = np.exp(-(X**2 + Y**2))               # Gaussian "hill" at every grid point

ax.plot_surface(X, Y, Z, cmap="viridis") # draw the colored surface
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("3D Gaussian surface")
plt.show()

# ---------------------------------------------------------------------------
# 5. A 3D scatter plot (points, not a surface)
# ---------------------------------------------------------------------------

np.random.seed(7)                        # reproducible random points
n = 50                                   # number of points
xs = np.random.rand(n)                   # random x coordinates
ys = np.random.rand(n)                   # random y coordinates
zs = np.random.rand(n)                   # random z coordinates

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(xs, ys, zs, s=50, c=zs, cmap="plasma")   # color by z value
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("3D scatter — drag to rotate!")
plt.show()

# ---------------------------------------------------------------------------
# 6. Done!
# ---------------------------------------------------------------------------

print("\nAll Matplotlib examples ran successfully!")
print("Tip: drag the 3D plots with your mouse to rotate them.")
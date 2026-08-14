"""
numpy_basics.py — the essential NumPy commands for CH4114.

This script demonstrates the NumPy functions used most often in this course:
np.array, np.arange, np.linspace, np.zeros, np.zeros_like, np.random,
np.radians, np.degrees, and element-wise math on arrays.

How to run:
    uv run python examples/numpy_matplotlib/numpy_basics.py

Author: Shuvam Banerji Seal
"""

__author__ = "Shuvam Banerji Seal"   # always sign your code!

import numpy as np   # import numpy with its standard short name


# ---------------------------------------------------------------------------
# 1. Creating arrays
# ---------------------------------------------------------------------------

# np.array builds an array from a Python list.
a = np.array([1, 2, 3, 4, 5])
print("a =", a)
print("shape:", a.shape)          # (5,)  -> 5 elements in one dimension
print("dtype:", a.dtype)          # int64 -> the type of the elements

# Indexing and slicing work exactly like lists.
print("first element:", a[0])     # 1
print("last element :", a[-1])    # 5
print("slice 1:4    :", a[1:4])   # elements at positions 1, 2, 3

# A 2D array (a matrix): shape = (rows, columns).
m = np.array([[1, 2], [3, 4]])
print("2D array:\n", m)
print("2D shape:", m.shape)       # (2, 2)
print("row 0, col 1:", m[0, 1])   # 2

# ---------------------------------------------------------------------------
# 2. The big five array creators
# ---------------------------------------------------------------------------

# np.arange(start, stop, step) -> evenly spaced integers.
print("arange(0, 10, 2):", np.arange(0, 10, 2))   # [0 2 4 6 8]

# np.linspace(a, b, n) -> n evenly spaced values from a to b (inclusive).
# This is THE function for generating x-values before plotting.
x = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", x)    # [0. 0.25 0.5 0.75 1.]

# np.zeros / np.ones -> arrays filled with 0 or 1.
print("zeros((2, 3)):\n", np.zeros((2, 3)))

# np.zeros_like(x) -> zeros with the SAME shape as x.
zero_grid = np.zeros_like(x)
print("zeros_like(x):", zero_grid)   # same length as x, all zeros

# ---------------------------------------------------------------------------
# 3. Random numbers: np.random
# ---------------------------------------------------------------------------

# ALWAYS set the seed first so results are reproducible.
np.random.seed(42)

print("rand(5)      :", np.random.rand(5))            # uniform in [0, 1)
print("randint(0,10):", np.random.randint(0, 10, 5))  # random integers
print("normal(0,1)  :", np.random.normal(0, 1, 5))    # Gaussian
print("uniform(-1,1):", np.random.uniform(-1, 1, 5))  # uniform in [-1, 1)

# A 3x3 grid of random positions (like atom coordinates!).
positions = np.random.rand(3, 3)
print("random positions (3x3):\n", positions)

# ---------------------------------------------------------------------------
# 4. Angles: degrees <-> radians
# ---------------------------------------------------------------------------

deg = 90
rad = np.radians(deg)          # 90 degrees = pi/2 radians
print("radians(90) =", rad)    # ~1.5708
print("degrees(rad) =", np.degrees(rad))   # back to 90.0

# Trig functions expect radians — always convert first!
angles = np.linspace(0, 360, 37)          # 37 angles in degrees
cos_vals = np.cos(np.radians(angles))     # cos needs radians
print("cos at 0, 90, 180 deg:", cos_vals[0], cos_vals[9], cos_vals[18])

# ---------------------------------------------------------------------------
# 5. Element-wise math on arrays (no loops needed!)
# ---------------------------------------------------------------------------

# Lennard-Jones potential: the formula you will use in the simulation sessions.
r = np.linspace(0.3, 1.0, 50)          # 50 distances in nm
sigma = 0.34                           # LJ sigma parameter (nm)
epsilon = 0.997                        # LJ epsilon parameter (kJ/mol)

sr = sigma / r                         # divide EVERY element by r
lj = 4 * epsilon * (sr**12 - sr**6)    # apply the formula to the whole array

print("LJ energy: min =", round(lj.min(), 4), " max =", round(lj.max(), 4))
print("mean of lj:", round(lj.mean(), 4))   # quick statistics
print("sum of lj:", round(lj.sum(), 4))

# ---------------------------------------------------------------------------
# 6. Done!
# ---------------------------------------------------------------------------

print("\nAll NumPy basics ran successfully!")
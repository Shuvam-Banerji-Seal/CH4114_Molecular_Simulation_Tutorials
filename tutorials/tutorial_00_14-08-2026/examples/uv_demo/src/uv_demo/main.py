"""Lennard-Jones potential demo.

Usage: uv run python -m uv_demo
"""

__author__ = "Shuvam Banerji Seal"

from __future__ import annotations

import numpy as np


def lj_energy(r: np.ndarray, epsilon: float = 0.997, sigma: float = 0.34) -> np.ndarray:
    """Lennard-Jones potential energy (kJ/mol) at distance(s) r (nm)."""
    sr = sigma / r
    return 4.0 * epsilon * (sr**12 - sr**6)


def main() -> None:
    r = np.linspace(0.32, 1.2, 50)
    e = lj_energy(r)
    r_min = r[np.argmin(e)]
    print(f"numpy version: {np.__version__}")
    print(f"LJ well depth : {e.min():.4f} kJ/mol at r = {r_min:.3f} nm")
    print("uv environment works ✓")


if __name__ == "__main__":
    main()

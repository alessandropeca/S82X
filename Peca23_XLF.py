import numpy as np
import pandas as pd
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
ax.set_xlabel("log Lx")
ax.set_ylabel("z")
ax.set_zlabel("log $\Phi$")

phi = np.load("Peca23_XLF.npy")
lum = np.linspace(42, 47, 101)
z = np.linspace(0, 4, 101)
X, Y = np.meshgrid(lum, z, indexing='ij')
surf = ax.plot_wireframe(X, Y, phi)
interp = RegularGridInterpolator((lum, z), phi, method='linear', bounds_error=False, fill_value=None)

ax.scatter(46,3,interp([46, 3]), marker='o', color='red', s=50)
plt.show()
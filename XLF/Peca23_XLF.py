import numpy as np
import pandas as pd
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt


phi_mat = np.load("Peca23_XLF.npy")
lum = np.linspace(42, 47, 101)
z = np.linspace(0, 4, 101) # these are the buondaries determined in the paper
interp = RegularGridInterpolator((lum, z), phi_mat, method='linear', 
                                 bounds_error=False, fill_value=0) 
                                 # use fill_value=None to extrapolate outside lum and z ranges determined in the paper

# Call the function to obtain the phi value (log10 of [Mpc^-3]) for any lum and z,
# eg., the XLF in lum=46 and z=3:
phi = interp([46, 3])
print(phi)

# this is for plotting purposes
fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
ax.set_xlabel("log Lx")
ax.set_ylabel("z")
ax.set_zlabel("log $\Phi$")
X, Y = np.meshgrid(lum, z, indexing='ij')
surf = ax.plot_wireframe(X, Y, phi_mat)
ax.scatter(46, 3, interp([46, 3]), marker='o', color='red', s=50)
plt.show()

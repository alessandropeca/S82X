# S82X

This repository contains some of the n-dim array used in Peca et al. 2023 (see full paper for details):
- The `Corrections` folder contains the corrections to derive intrinsic AGN distributions.
- The `XLF` folder contains the derived X-ray luminosity function. `Peca23_XLF.py` shows how to use the XLF and obtain the number density of AGN [Mpc-3] for a given luminosity and redshift.

These files are free to use, but if you use them, please cite our paper [at this link](https://ui.adsabs.harvard.edu/abs/2023ApJ...943..162P/abstract).

### To use the XLF:

This script (Peca23_XLF.py) computes and plots the X-ray Luminosity Function (XLF) based on a provided dataset. It can evaluate the XLF at specific points or integrate over specified luminosity and redshift ranges.

#### Evaluating XLF at a specific luminosity and redshift

To evaluate the XLF at a specific luminosity (`Lx`) and redshift (`z`):

`python Peca23_XLF.py <log Lx> <z>`

#### Evaluating XLF in luminosity and redshift bins

To integrate the XLF over a range of luminosities (Lx_min to Lx_max) and redshifts (z_min to z_max):

`python Peca23_XLF.py <log Lx_min> <log Lx_max> <z_min> <z_max>`

NOTE: The script will print a warning if the provided values are outside the predefined ranges (log Lx [42-47], z [0,4]) derived in [Peca et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...943..162P/abstract). For larger ranges, the code will compute a linear extrapolation, so use it with caution.

#### Plotting control

The script will automatically print the 3D XLF with the requested volume density in red. To disallow the plotting option just add `--plot=False`



# S82-XL
The catalog of S82-XL is available (Xray_15_comb4_slim45_ZBEST_7_HR_map.zip) for internal use only (password required). The catalog will be publicly available once the paper is published (Peca et al. 2024, in prep.).


# S82-XL
The X-ray catalog of S82-XL is available for download (S82-XL_FINAL_XRAY.fits.zip). Information on each column is stored in the header file. If you use the catalog, please cite our paper [Peca et al. 2024](https://ui.adsabs.harvard.edu/abs/2024arXiv240709617P/abstract)



# S82X

This repository contains some of the n-dim array used in Peca et al. 2023 (see full paper for details):
- The `Corrections` folder contains the corrections to derive intrinsic AGN distributions.
- The `XLF` folder contains the derived X-ray luminosity function. To use `Peca23_XLF.py` you need to also download `Peca23_XLF.npy` in the same folder. See below how to use the XLF and obtain the number density of AGN [Mpc-3] for a given luminosity and redshift bins or single values.

These files are free to use, but if you use them, please cite our paper [at this link](https://ui.adsabs.harvard.edu/abs/2023ApJ...943..162P/abstract).

### To use the XLF:

This script (Peca23_XLF.py) computes and plots the X-ray Luminosity Function (XLF) based on a provided dataset. It can evaluate the XLF at specific points or integrate over specified luminosity and redshift ranges.

Tu run the XLF, you can:
1. Use the examples below.
2. Open the Jupyter notebook: [`Peca23_XLF_Usage.ipynb`](XLF/Peca23_XLF_Usage.ipynb).
3. **NEW:** Launch the XLF Tool directly in Binder:  
   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alessandropeca/S82X/HEAD?filepath=XLF/Peca23_XLF_Usage.ipynb)

#### Evaluating XLF at a specific luminosity and redshift

To evaluate the XLF at a specific luminosity (`Lx`) and redshift (`z`):

`python Peca23_XLF.py <log Lx> <z>`

The result will be printed in the terminal.
<img width="683" alt="Screenshot 2024-06-27 at 4 45 14 PM" src="https://github.com/alessandropeca/S82X/assets/30237963/8412c9ad-226f-439d-87ea-3962848e9be1">

#### Evaluating XLF in luminosity and redshift bins

To integrate the XLF over a range of luminosities (Lx_min to Lx_max) and redshifts (z_min to z_max):

`python Peca23_XLF.py <log Lx_min> <log Lx_max> <z_min> <z_max>`

The result will be printed in the terminal.
<img width="681" alt="Screenshot 2024-06-27 at 4 45 59 PM" src="https://github.com/alessandropeca/S82X/assets/30237963/adaed85c-e0ac-48ff-8f55-ad5abbea57af">

#### Evaluating XLF in luminosity and fixed redshift

To integrate the XLF over a range of luminosities (Lx_min to Lx_max) and fixed redshift:

`python Peca23_XLF.py <log Lx_min> <log Lx_max> <z>`

NOTE: The script will print a warning if the provided values are outside the predefined ranges (log Lx [42-47], z [0,4]) derived in [Peca et al. 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...943..162P/abstract). For larger ranges, the code will compute a linear extrapolation, so use it with caution.

NOTE: A very small number of C-thick AGN were discovered in Peca+23, therefore this XLF has to be considered reliable up to $\log N_H \sim 24\ \ cm^2$.

#### Plotting control

The script will automatically print the 3D XLF with the requested volume density in red. To disallow the plotting option just add `--plot=False`



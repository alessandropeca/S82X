import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
import argparse
import sys

def main(args, plot):
    phi_mat = np.load("Peca23_XLF.npy")
    
    def check_extrapolation1(l, z):
        extrapolated = False
        if z < 0 or z > 4 or l < 42 or l > 47:
            extrapolated = True
            print("Warning: the LF is being extrapolated for z > 4 and log Lx < 42 or > 47")
        return extrapolated

    def check_extrapolation2(l1, l2, z1, z2):
        extrapolated = False
        if z1 < 0 or z2 > 4 or l1 < 42 or l2 > 47:
            extrapolated = True
            print("Warning: the LF is being extrapolated for z > 4 and log Lx < 42 or > 47\n")
        return extrapolated


    min_lum = 42 # These are the boundaries determined in the paper
    max_lum = 47
    max_z = 4
    
    if len(args) == 2:
        if check_extrapolation1(float(args[0]), float(args[1])):
            lum_value = float(args[0])
            if lum_value > 47:
                max_lum = lum_value
            else:
                min_lum = lum_value
            
            z_value = float(args[1])
            if z_value > 4:
                max_z = z_value
            else:
                if z_value < 0:
                    print("z < 0 not allowed.")
                    sys.exit()
    
    elif len(args) == 4:
        if check_extrapolation2(float(args[0]), float(args[1]), float(args[2]), float(args[3])):
            lum_min = float(args[0])
            lum_max = float(args[1])
            z_min = float(args[2])
            z_max = float(args[3])
            
            if lum_max > 47:
                max_lum = lum_max
            if lum_min < 42:
                min_lum = lum_min
            if z_max > 4:
                max_z = z_max
            if z_min < 0 or z_max < 0:
                print("z < 0 not allowed.")
                sys.exit()
    
    else:
        print("Wrong number of parameters.")
        sys.exit()

    
    lum = np.linspace(min_lum, max_lum, 101)
    z = np.linspace(0, max_z, 101)
    
    interp = RegularGridInterpolator((lum, z), phi_mat, method='linear', bounds_error=False, fill_value=None)

    if len(args) == 2:
        # Get the phi value for the specified luminosity and redshift
        lum_value = float(args[0])
        z_value = float(args[1])
        phi = interp([lum_value, z_value])
        print(f"log Phi/Mp3 at Lx={lum_value} and z={z_value}: {phi[0]}")

        if plot.lower() == 'yes':
            # Plotting the interpolated function and the specified point
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.set_xlabel("log Lx")
            ax.set_ylabel("z")
            ax.set_zlabel("log $\Phi$")
            X, Y = np.meshgrid(lum, z, indexing='ij')
            surf = ax.plot_wireframe(X, Y, phi_mat)
            ax.scatter(lum_value, z_value, phi, marker='o', color='red', s=50)
            plt.show()

    elif len(args) == 4:
        # Define the integration bounds
        lum_min = float(args[0])
        lum_max = float(args[1])
        z_min = float(args[2])
        z_max = float(args[3])

        # Define the function to integrate
        def integrand(l, z):
            return 10**interp([l, z])  # Convert from log10 to linear scale for integration

        # Perform the double integration
        total_phi, error = dblquad(integrand, z_min, z_max, lambda z: lum_min, lambda z: lum_max)

        print(f"Total space density: {total_phi:.3e} Mpc^-3")
        print(f"Integration error estimate: {error:.3e}")

        if plot.lower() == 'yes':
            # Plotting the interpolated function and the integration region
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.set_xlabel("log Lx")
            ax.set_ylabel("z")
            ax.set_zlabel("log $\Phi$")
            X, Y = np.meshgrid(lum, z, indexing='ij')
            surf = ax.plot_wireframe(X, Y, phi_mat)

            # Highlighting the integration region
            lum_range = np.linspace(lum_min, lum_max, 10)
            z_range = np.linspace(z_min, z_max, 10)
            L, Z = np.meshgrid(lum_range, z_range, indexing='ij')
            Phi_integration_region = interp((L, Z))
            ax.plot_surface(L, Z, Phi_integration_region, color='red', alpha=0.5)

            plt.show()

if __name__ == "__main__":
    print()
    parser = argparse.ArgumentParser(description='Compute and plot X-ray luminosity function.')
    parser.add_argument('args', nargs='+', help='Luminosity and redshift values or ranges (2 or 4 values)')
    parser.add_argument('--plot', type=str, default='yes', help='Plot the graph (yes or no)')
    args = parser.parse_args()

    main(args.args, args.plot)
    print("\nPlease cite Peca et al. 2023 (Bibcode:2023ApJ...943..162P)\n")

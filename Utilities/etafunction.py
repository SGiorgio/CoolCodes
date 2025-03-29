## eta function 
## function defined as y(n) = prod(Pi)_i=0^n

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import make_interp_spline
from scipy.interpolate import Akima1DInterpolator
import numpy as np

def generate_primes(n=100):
    """Generate the first n prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

def Pn(n):
    P = generate_primes(n)
    Prod = 1
    for i in range(n):  # Fix indexing to iterate correctly
        Prod *= P[i]
    return Prod

def ycompile(n):
    y = []  # Initialize y as an empty list
    for i in range(n):
        y.append(Pn(i+1))  # Use append to add elements to the list
    return y

def print_table(x, y):
    """Print a table of prime numbers and their corresponding computed values."""
    print(f"{'Index':<10}{'Prime':<10}{'Computed Value (y)':<20}")
    print("-" * 40)
    for i, (prime, value) in enumerate(zip(x, y), start=1):
        print(f"{i:<10}{prime:<10}{value:<20}")

def plot_scatter(x, y):
    """Plot a scatter plot of the data."""
    plt.figure()  # Create a new figure
    plt.scatter(x, y, color='red', label='Data')
    plt.title("Scatter Plot of Primes vs. Computed Values")
    plt.xlabel("Prime Numbers")
    plt.ylabel("Computed Values (y)")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_akima_interpolation(x, y):
    """Plot Akima interpolation for the given data and print its analytic expression."""
    akima = Akima1DInterpolator(x, y)
    x_akima = np.linspace(min(x), max(x), 500)
    y_akima = akima(x_akima)

    # Print the analytic expression of the interpolator
    print("Akima Interpolator Coefficients:")
    print(akima.c)  # Coefficients of the Akima interpolator

    plt.figure()  # Create a new figure
    plt.scatter(x, y, color='red', label='Data')  # Scatter plot for data points
    plt.plot(x_akima, y_akima, color='green', label='Akima Curve')  # Akima curve
    plt.title("Scatter Plot with Akima Interpolation")
    plt.xlabel("Prime Numbers")
    plt.ylabel("Computed Values (y)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_logarithmic(x, y, x_akima, y_akima):
    """Plot a logarithmic plot of the data and Akima interpolation."""
    plt.figure()  # Create a new figure
    plt.scatter(x, y, color='red', label='Data')  # Scatter plot for data points
    plt.plot(x_akima, y_akima, color='green', label='Akima Curve')  # Akima curve

    # Set logarithmic scales
    plt.xscale('log')
    plt.yscale('log')

    # Add title, labels, legend, and grid
    plt.title("Logarithmic Plot with Akima Interpolation")
    plt.xlabel("Prime Numbers (log scale)")
    plt.ylabel("Computed Values (y) (log scale)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate data
n = 20
x = generate_primes(n)
y = ycompile(n)

# Print the table
print_table(x, y)

# Plot scatter
plot_scatter(x, y)

# Plot Akima interpolation
plot_akima_interpolation(x, y)

# Prepare data for logarithmic plot
akima = Akima1DInterpolator(x, y)
x_akima = np.linspace(min(x), max(x), 500)
y_akima = akima(x_akima)

# Plot logarithmic
#plot_logarithmic(x, y, x_akima, y_akima)



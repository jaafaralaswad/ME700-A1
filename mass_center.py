# Bisection method solver used for numerical example 5 - ME700 Assignment 1 "warm-up"
# Author: Jaafar Alaswad (jalaswad@bu.edu)

import numpy as np

def mass_center():

    """
    Implements the bisection method to find the of the center of mass for a number of masses in 1D.
    The method iteratively halves the interval [x_1,x_n] until a root is found within specified tolerances.
    """

    # Prompt user for the number of masses
    n = int(input("Enter the number of masses (n): "))

    # Initialize lists to store masses and positions
    masses = []
    positions = []

    # Loop to collect masses and positions
    for i in range(n):
        m = float(input(f"Enter mass m[{i+1}]: "))  # Get mass
        x = float(input(f"Enter position x[{i+1}]: "))  # Get position
        masses.append(m)
        positions.append(x)

    # Formulate the equation
    f = lambda x: sum(m * (x_i - x) for m, x_i in zip(masses, positions))

    # The initial bounds are always a = x_1 and b = x_n
    a = positions[0]
    b = positions[-1]

    # Loop to ensure the valid is interval: in this example, this is certain
    while True:
        
        # Check if f(a) * f(b) < 0
        if f(a) * f(b) < 0:
            break  # Exit the loop as interval is valid

    # Prompt user for tolerances
    tol_x = float(input("Enter the tolerance with respect to |c-a|: "))
    tol_f = float(input("Enter the tolerance with respect to |f(c)|: "))
    
    # Initialize iteration counter
    iteration = 0

    # Print table header for displaying iteration results
    print(f"\n{'Iteration':<10} {'a':<15} {'b':<15} {'c':<15} {'|f(c)|':<15}")
    
    while True:
        # Compute the midpoint of the interval
        c = (a + b) / 2
        fc = f(c) # Evaluate function at midpoint
        
        # Display current iteration results
        iteration += 1
        print(f"{iteration:<10} {a:<15.6f} {b:<15.6f} {c:<15.6f} {abs(fc):<15.6e}")
        
        # Check stopping criteria: if interval width or function value is below tolerance
        if abs(c - a) < tol_x or abs(fc) < tol_f:
            print(f"\nCenter of mass at x = {c:.6f} after {iteration} iterations.")
            return
        
        # Update interval for next iteration
        if f(a) * fc < 0: # Opposite signs indicate root in [a, c]
            b = c
        else: # Otherwise, root is in [c, b]
            a = c

# Execute the bisection method
mass_center()
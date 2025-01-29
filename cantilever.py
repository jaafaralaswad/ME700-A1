# Bisection method solver used for numerical example 4 - ME700 Assignment 1 "warm-up"
# Author: Jaafar Alaswad (jalaswad@bu.edu)

import numpy as np

def cantilever():

    """
    Implements the bisection method to find the location a balance force is applied in a cantilever beam.
    The method iteratively halves the interval [0,L] until a root is found within specified tolerances.
    """

    # Prompt user for the length of the cantilever beam
    L = float(input("Enter the length of the cantilever beam (L): "))

    # Prompt user for the uniformly distributed load
    w = float(input("Enter the value of the uniformly distributed force (w): "))

    # Prompt user for the balance force
    P = float(input("Enter the value of the balance force (F): "))

    # Formulate the equation
    f = lambda x: x - w*L**2/(2*P)

    # The initial bounds are always a = 0 and b = L as the force acts on the beam
    a = 0
    b = L

    # Ensure the user enters valid parameters
    while True:
        
        # Check if f(a) * f(b) < 0
        if f(a) * f(b) < 0:
            break  # Exit the loop as parameters are valid
        else:
            print("Static balance with the entered parameters is impossible. Please try different values.")

            # Prompt user to update the length of the cantilever beam
            L = float(input("Update the length of the cantilever beam (L): "))

            # Prompt user to update the uniformly distributed load
            w = float(input("Update the value of the uniformly distributed force (w): "))

            # Prompt user to update the balance force
            P = float(input("Update the value of the balance force (F): "))

    # Prompt user for tolerances
    tol_x = float(input("Enter the tolerance with respect to |c-a|: ")) # Tolerance for interval width
    tol_f = float(input("Enter the tolerance with respect to |f(c)|: ")) # Tolerance for function value
    
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
            print(f"\nBalance force should be applied at x = {c:.6f} after {iteration} iterations.")
            return
        
        # Update interval for next iteration
        if f(a) * fc < 0: # Opposite signs indicate root in [a, c]
            b = c
        else: # Otherwise, root is in [c, b]
            a = c

# Execute the bisection method
cantilever()
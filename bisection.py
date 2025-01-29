# Bisection method solver used for numerical examples 1-3 - ME700 Assignment 1 "warm-up"
# Author: Jaafar Alaswad (jalaswad@bu.edu)

import numpy as np

def bisection():

    """
    Implements the bisection method to find a root of a user-defined function within a specified interval.
    The method iteratively halves the interval until a root is found within specified tolerances.
    """

    # Prompt user for the equation and define it as a NumPy function
    f_expr = input("Enter the equation as a function of x, f(x): ")
    f = eval(f"lambda x: {f_expr}", {"np": np})
    
    # Ensure the user enters a valid interval
    while True:

        # Check if the interval contains a root using the Intermediate Value Theorem
        a = float(input("Enter the lower limit (a): "))
        b = float(input("Enter the upper limit (b): "))
        
        # Check if f(a) * f(b) < 0
        if f(a) * f(b) < 0: 
            break  # Valid interval found
        else:
            print("A root in this interval is not guaranteed. Please try another interval.")
    
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
            print(f"\nRoot found at c = {c:.6f} after {iteration} iterations.")
            return
        
        # Update interval for next iteration
        if f(a) * fc < 0: # Opposite signs indicate root in [a, c]
            b = c
        else: # Otherwise, root is in [c, b]
            a = c

# Execute the bisection method
bisection()
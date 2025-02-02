import sys
from pathlib import Path

# Add the project folder to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from bisection import bisection, validate_b_greater_a, validate_interval, update_interval_a_b
import numpy as np
from pathlib import Path
import pytest
import re

# Test function examples
def test_bisection_finds_root():
    # Test for a simple quadratic function x^2 - 4 = 0 (roots at x = -2, 2)
    result = bisection(lambda x: x**2 - 4, 0, 3, 1e-6, 1e-6, 100)
    assert abs(result['root'] - 2) < 1e-6
    assert result['converged'] is True
    assert result['iterations'] <= 100

def test_bisection_no_root_in_interval():
    # Test for no root in interval [3, 5] for x^2 - 4 = 0
    with pytest.raises(ValueError, match=r"A root in interval.*is not guaranteed."):
        bisection(lambda x: x**2 - 4, 3, 5, 1e-6, 1e-6, 100)

def test_bisection_max_iterations():
    # Test to ensure max iterations are handled correctly
    with pytest.raises(ValueError, match=r"Procedure terminated.*without convergence."):
        bisection(lambda x: x**3 - 2, 0, 1, 1e-15, 1e-15, 5)

def test_validate_b_greater_a():
    # Test that validate_b_greater_a raises an error when a >= b
    with pytest.raises(ValueError, match="Invalid input: 2.0 is equal to 2.0."):
        validate_b_greater_a(2.0, 2.0)
    with pytest.raises(ValueError, match="Invalid input: 3.0 is greater than 2.0."):
        validate_b_greater_a(3.0, 2.0)

def test_update_interval_a_b():
    # Test interval updating with function x^2 - 4
    a, b, fa, fb = update_interval_a_b(0, 3, 1.5, -4, 5, -1.75)
    assert a == 1.5
    assert b == 3
    assert fa == -1.75
    assert fb == 5

def test_bisection_with_negative_root():
    # Test for finding negative root in [-3, 0]
    result = bisection(lambda x: x**2 - 4, -3, 0, 1e-6, 1e-6, 100)
    assert abs(result['root'] + 2) < 1e-6
    assert result['converged'] is True

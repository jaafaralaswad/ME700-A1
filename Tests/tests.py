import sys
sys.path.append('..')  # '..' points to the parent directory
import bisection
import numpy as np
from pathlib import Path
import pytest
import re

def test_middle_point():
    a = 10.0
    b = 20.0
    found = bisection.evaluate_middle_point(a, b)
    known = 15.0
    assert np.isclose(known, found)
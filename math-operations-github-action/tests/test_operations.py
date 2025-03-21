"""
Unit tests for the mathematical operations.
"""

import sys
import os

# Insert the project root into sys.path so that local modules are found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# The following imports must come after the sys.path modification.
import pytest  # pylint: disable=wrong-import-position
from src.operations import add, subtract, multiply, divide  # pylint: disable=wrong-import-position

def test_add() -> None:
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract() -> None:
    """Test the subtract function."""
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply() -> None:
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide() -> None:
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0)

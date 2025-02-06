# tests/test_main.py

import pytest
from src.main import add, subtract  # Import functions from main.py

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(-3, -3) == 0

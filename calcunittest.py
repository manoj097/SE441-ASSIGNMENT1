# calcunittest.py

import calculator  # Assuming the name of your module with math operations
import pytest

# Test addition function
def test_add():
    assert calculator.add(5, 3) == 8
    assert calculator.add(12, 5) == 17
    assert calculator.add(1, 1) != 3

# Test subtraction function
def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-5, 5) == -10
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(10, 3) != 6

if __name__ == "__main__":
    pytest.main()


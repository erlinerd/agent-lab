import pytest
from src.calc import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(12, 3) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError, match="^division by zero$"):
        divide(12, 0)

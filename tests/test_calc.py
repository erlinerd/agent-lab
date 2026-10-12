import pytest
from src.calc import add, subtract, multiply, clamp


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(3, 4) == 12


def test_clamp_above_range():
    assert clamp(5, 0, 3) == 3


def test_clamp_below_range():
    assert clamp(-1, 0, 3) == 0


def test_clamp_within_range():
    assert clamp(2, 0, 3) == 2


def test_clamp_low_greater_than_high_raises():
    with pytest.raises(ValueError):
        clamp(1, 3, 0)

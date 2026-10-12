import pytest
from src.calc import add, average, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(3, 4) == 12


def test_average():
    result = average([1, 2, 3])

    assert result == 2.0
    assert isinstance(result, float)


def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])

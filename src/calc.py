"""Tiny calculator module used as the Multica + GitHub lab target."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def clamp(value: float, low: float, high: float) -> float:
    """Restrict value to the inclusive range [low, high].

    Raise ValueError if low is greater than high.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value

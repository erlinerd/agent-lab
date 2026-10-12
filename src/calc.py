"""Tiny calculator module used as the Multica + GitHub lab target."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b

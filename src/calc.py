"""Tiny calculator module used as the Multica + GitHub lab target."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of numbers."""
    if not numbers:
        raise ValueError("average() requires at least one number")
    return sum(numbers) / len(numbers)

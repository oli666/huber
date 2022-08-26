"""Test functions."""
from huber.math import factorial
from huber.math import gcd
from huber.math import sum_r


def test_factorial() -> None:
    """Test facorial."""
    assert factorial(4) == 24
    assert factorial(1) == 1


def test_gcd() -> None:
    """Get gcd."""
    assert gcd(24, 8) == 8


def test_sum_r() -> None:
    """Test sum."""
    assert sum_r([1, 3]) == 4

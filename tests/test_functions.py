import pytest

from huber.functions import factorial
from huber.functions import gcd


def test_factorial() -> None:
    assert factorial(4) == 24
    assert factorial(1) == 1


def test_gcd() -> None:
    assert gcd(24, 8) == 8

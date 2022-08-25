import typing
from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    """Get facorial of n (recursive version)

    :n: Integer to calculate factorial for
    :returns: Factorial of n

    """
    if n == 1:
        # Basecase
        return 1
    else:
        # Recursive Case
        return n * factorial(n - 1)


@lru_cache(maxsize=None)
def gcd(a: int, b: int) -> int:
    """Get greatest common divisor

    :a: First int
    :b: Second int
    :returns: Greatest common divisor as int

    """
    if b <= 1:
        return a
    else:
        return gcd(b, a % b)

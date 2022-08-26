"""General Functions."""
from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    """Get facorial of n (recursive version).

    :n: Integer to calculate factorial for
    :returns: Factorial of n

    >>> factorial(4)
    24

    """
    if n == 1:
        # Basecase
        return 1
    else:
        # Recursive Case
        return n * factorial(n - 1)


@lru_cache(maxsize=None)
def gcd(a: int, b: int) -> int:
    """Get greatest common divisor.

    :a: First int
    :b: Second int
    :returns: Greatest common divisor as int

    """
    if b <= 1:
        return a
    else:
        return gcd(b, a % b)


def sum_r(a_list: List[int]) -> int:
    """Get sum of a list of integers.

    :l: List of integers
    :returns: Sum of items of l

    """
    if len(a_list) == 0:
        return 0
    else:
        return a_list[0] + sum_r(a_list[1:])

"""CLI functions."""
import click

from huber.math import factorial
from huber.math import gcd


@click.command()
@click.argument("number", required=1)
@click.version_option()
def get_factorial(number: str) -> None:
    """Get facorial CLI."""
    print(factorial(int(number)))


@click.command()
@click.argument("num1", required=1)
@click.argument("num2", required=1)
@click.version_option()
def get_gcd(num1: str, num2: str) -> None:
    """Get gcd CLI."""
    print(gcd(int(num1), int(num2)))

"""CLI functions."""
import click

from huber.functions import factorial
from huber.functions import gcd


@click.command()
@click.argument("number", required=1)
@click.version_option()
def get_factorial(number):
    """Get facorial CLI."""
    print(factorial(int(number)))


@click.command()
@click.argument("num1", required=1)
@click.argument("num2", required=1)
@click.version_option()
def get_gcd(num1, num2):
    """Get gcd CLI."""
    print(gcd(int(num1), int(num2)))

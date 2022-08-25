import click
from recursion.functions import factorial, gcd

@click.command()
@click.argument('number', required=1)
@click.version_option()
def get_factorial(number):
    print(factorial(int(number)))


@click.command()
@click.argument('num1', required=1)
@click.argument('num2', required=1)
@click.version_option()
def get_gcd(num1, num2):
    print(gcd(int(num1), int(num2)))


"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Oliver_Huber."""


if __name__ == "__main__":
    main(prog_name="huber")  # pragma: no cover

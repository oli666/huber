"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Stardog Performance."""


if __name__ == "__main__":
    main(prog_name="stardog-performance")  # pragma: no cover

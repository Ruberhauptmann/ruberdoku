import click

from ruberdoku.main import main


@click.command()
def cli():
    main()


if __name__ == "__main__":
    cli()

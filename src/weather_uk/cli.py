import click

from weather_uk.config import setup_config_if_none_exists, update_config


@click.group()
def main():
    setup_config_if_none_exists()


@main.command()
@click.option("--apikey", help="Your Met Office Datapoint API key")
def config(apikey):
    if apikey:
        update_config(apikey)

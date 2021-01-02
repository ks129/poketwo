import asyncio
import logging

import click
import uvloop
import yoyo

from classes.bot import Bot
from config import Config

uvloop.install()
logging.basicConfig(level=logging.INFO)


def run_bot(config):
    bot = Bot(
        command_prefix=config.prefix,
        case_insensitive=True,
        help_command=None,
        config=config,
    )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start())


@click.group()
def main():
    pass


@main.command(help="Run the bot.")
@click.option("--token", envvar="TOKEN")
@click.option("--prefix", envvar="PREFIX")
@click.option("--cogs", envvar="COGS", type=click.Choice(("bot",)), multiple=True)
@click.option("--amqp-uri", envvar="AMQP_URI")
@click.option("--redis-uri", envvar="REDIS_URI")
@click.option("--db-uri", envvar="DB_URI")
def run(token, prefix, cogs, amqp_uri, redis_uri, db_uri):
    config = Config(token, prefix, cogs, amqp_uri, redis_uri, db_uri)
    run_bot(config)


@main.command(help="Apply any outstanding database migrations.")
@click.option("--db-uri", envvar="DB_URI")
def migrate(db_uri):
    backend = yoyo.get_backend(db_uri)
    migrations = yoyo.read_migrations("migrations")
    to_apply = backend.to_apply(migrations)

    if click.confirm(f"Running {len(to_apply)} migrations... will lock the db"):
        with backend.lock():
            backend.apply_migrations(to_apply)
        click.echo("Successfully applied migrations.")
    else:
        click.echo("Aborted.")


if __name__ == "__main__":
    main()

import asyncio
import logging

import config
from classes.bot import Bot

logging.basicConfig(level=logging.INFO)

bot = Bot(
    command_prefix=config.prefix,
    case_insensitive=True,
    help_command=None,
    config=config,
)

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.start())

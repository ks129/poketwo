import io
import logging
import textwrap
import traceback
from contextlib import redirect_stdout

from discord.ext import commands
from utils.time import strfdelta

log = logging.getLogger(__name__)


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """View the bot's latency."""

        message = await ctx.send("Pong!")
        delta = message.created_at - ctx.message.created_at
        await message.edit(content=f"Pong! **{strfdelta(delta)}**")

    @commands.is_owner()
    @commands.command(name="eval")
    async def _eval(self, ctx, *, code: str):
        """Evaluate code and play around."""

        env = {"bot": self.bot, "ctx": ctx}
        env.update(globals())
        stdout = io.StringIO()

        try:
            exec(f"async def func():\n{textwrap.indent(code, '  ')}", env)
        except Exception as e:
            await ctx.send(f"```py\n{e.__class__.__name__}: {e}\n```")
            return

        try:
            with redirect_stdout(stdout):
                result = await env["func"]()
        except Exception:
            await ctx.send(f"```py\n{stdout.getvalue()}{traceback.format_exc()}\n```")
        else:
            await ctx.send(f"```py\n{stdout.getvalue()}{result}\n```")


def setup(bot):
    bot.add_cog(General(bot))

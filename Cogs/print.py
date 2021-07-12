import discord
from discord.ext import commands

class Print(commands.Cog, name='Print'):
    """Send a screenshot of the replyed message"""

    def __init__(self, bot: commands.Bot):
        self.bot= bot

@commands.command()
async def print(self, ctx):
    await ctx.reply('Testando')


def setup(bot: commands.Bot):
    bot.add_cog(Print(bot))
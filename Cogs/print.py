import discord
from discord.ext import commands

class Print(commands.Cog, name='Print'):
    """Send a screenshot of the replyed message"""

    def __init__(self, bot):
        self.bot= bot

    @commands.command()
    async def print(self, ctx):
        await ctx.reply('Testando')


def setup(bot):
    bot.add_cog(Print(bot))
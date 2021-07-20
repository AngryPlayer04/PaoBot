import discord
from discord.ext import commands

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    @commands.command()
    async def print(self, ctx, *, expressao):
        cal = eval(expressao)
        await ctx.reply(cal)


def setup(bot):
    bot.add_cog(Calc(bot))
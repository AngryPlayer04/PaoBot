import discord
from discord.ext import commands
import math

class Calculators(commands.Cog, name = "calculator"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.command()
    async def calc(self, ctx, *, express):
        soma = eval(express)
        await ctx.reply(":abacus: **|** O resultado é: {}".format(soma))

def setup(bot):
    bot.add_cog(Calculators(bot))

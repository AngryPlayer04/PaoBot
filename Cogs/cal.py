import discord 
import os 
import math 
from discord.ext import commands 

class Cal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command(name = "Cal", help = "Calculadora")
    async def cal(self, ctx, *, expression):
        c = float(eval(expression))
        await ctx.reply(":abacus:  **|**  {} é igual a: `{:.3}`".format(expression, c))


def setup(bot):
    pass

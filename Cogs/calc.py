import discord 
import os 
import math 
from discord.ext import commands 

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command(name = "Calc", help = "Calculadora")
    async def calc(self, ctx, *, expression):
        c = float(eval(expression))
        await ctx.reply(":abacus:  **|**  {} é igual a: `{:.3}`".format(expression, c))

def setup(bot):
    bot.add_cog(Calc(bot))
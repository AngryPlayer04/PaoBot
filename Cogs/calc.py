import discord 
import os 
import math 
from discord.ext import commands 

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command()
    async def calc(ctx, *, expression):
        c = eval(expression)
        await ctx.reply(c)

def setup(bot):
    bot.add_cog(Calc(bot))
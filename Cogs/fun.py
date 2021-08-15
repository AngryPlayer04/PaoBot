import discord 
from discord.ext import commands 
import random 

class Funny(commands.Cog, name = "Funny Commands"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot 
    @commands.command()
    async def flip(self, ctx):
        moeda = random.randrange(1,3)
        if moeda == 1:
            await ctx.reply(":slight_smile: Cara!")
        else:
            await ctx.reply(":crown: Coroa!")


def setup(bot):
    bot.add_cog(Funny(bot))
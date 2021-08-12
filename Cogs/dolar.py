import discord
from discord.ext import commands
import PyCurrency_Converter as pcc

class Economy(commands.Cog, name="Economia"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot 
    @commands.command()
    async def dolar(ctx):
        dol = pcc.convert(1, 'USD', 'R$')
        await ctx.reply("A cotação do dólar atualmente é de R${:4}".format(dol))

def setup(bot):
    bot.add_cog(Economy(bot))
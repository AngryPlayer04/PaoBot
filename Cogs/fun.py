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

    @commands.command(name= 'receita', help='this command send a random recipe')
    async def receita(ctx):
        lin = "https://www.tudogostoso.com.br/receita/72313-pao-caseiro-facil.html",\
        "https://www.tudogostoso.com.br/receita/79996-pao-de-queijo-3-ingredientes.html", \
        "https://www.tudogostoso.com.br/receita/83-pao-de-batata.html", \
        "https://www.tudogostoso.com.br/receita/105067-pao-recheado.html"
        await ctx.reply(random.choice(lin))


def setup(bot):
    bot.add_cog(Funny(bot))
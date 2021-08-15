import discord 
from discord.ext import commands 
from random import choice

class Funny(commands.Cog, name = "Funny Commands"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot 
    @commands.command()
    async def flip(self, ctx):
        moeda = ["cara", "coroa"]
        lado_coroa = ["coroa"]
        jogadas = 1000
        numero_coroas = 0
        for _ in range(1, jogadas + 1):
            evento = choice(moeda)
            if evento in lado_coroa:
                numero_coroas += 1
        probabilidade = numero_coroas / jogadas
        await ctx.reply("Foram feitos %d lançamentos." % jogadas + "\nCaiu coroa %d vezes" % numero_coroas + "\nA chance de cair coroa foi de %.2f." % probabilidade )


def setup(bot):
    bot.add_cog(Funny(bot))
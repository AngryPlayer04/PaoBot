import discord
from discord.ext import commands
import numexpr as ne
from currency_converter import CurrencyConverter as c

class Calculators(commands.Cog, name = "calculator"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.command()
    async def calc(self, ctx, *, express):
        try:
            soma = ne.evaluate(express)
            await ctx.reply(":abacus: **|** O resultado é:`{}`".format(soma))

        except (RuntimeError, OverflowError, ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await ctx.reply("Desculpe, eu não posso calcular `{}` ou ocorreu um erro desconhecido.".format(express))
    
    @commands.command()
    async def dolar(self, ctx, currencies):
        cambio = c.convert(1, 'USD', 'BRL')
        await ctx.reply ("O dólar está {} do Real.".format(cambio))



def setup(bot):
    bot.add_cog(Calculators(bot))

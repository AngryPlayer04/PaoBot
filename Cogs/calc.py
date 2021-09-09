import discord
from discord.ext import commands
import json
import numexpr as ne
import requests
import speedtest

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
    async def dolar(self, ctx):
        apiKey = 'czd1bJ0ZcKoIOKAyaiL5sfqghTsDaIdvncQQDH8'
        baseCurrency = 'USD'
        url = 'https://currencyapi.net/api/v1/rates?key='+apiKey+'&base='+baseCurrency
        r = requests.get(url)
        response = r.json()
        await ctx.reply('Um dólar equivale atualmente a R$'+'%.2f' % response ['rates']['BRL'])


def setup(bot):
    bot.add_cog(Calculators(bot))

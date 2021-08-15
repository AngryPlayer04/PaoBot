import discord
from discord.ext import commands
import numexpr as ne
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

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
    async def dolar(self,url, ctx, from_currency, to_currency, amount = 1):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = CurrencyConverter(url)
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        cambio = round(amount * self.currencies[to_currency], 4)
        await ctx.reply ("O dólar está {} do Real.".format(cambio))



def setup(bot):
    bot.add_cog(Calculators(bot))

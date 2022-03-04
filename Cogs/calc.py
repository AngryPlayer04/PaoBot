import disnake
from disnake.ext import commands
import json
import numexpr as ne
from forex_python.converter import CurrencyRates
import speedtest

class Calculators(commands.Cog, name = "calculator"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(help = 'Calcula a expressão dada (Use `/` para divisão, `*` para multiplicação e `**`para potência)', 
    aliases = ['calculadora', 'calcular'])
    async def calc(self, ctx, *, express):
        try:
            soma = ne.evaluate(express)
            await ctx.reply(":abacus: **|** O resultado é:`{}`".format(soma))
        except (RuntimeError, OverflowError, ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await ctx.reply("Desculpe, eu não posso calcular `{}` ou ocorreu um erro desconhecido.".format(express))

    @commands.command(help = 'Diz a cotação do dólar em real(Infelizmente a API só atualiza uma vez ao dia', aliases = ['dol'])
    async def dolar(self, ctx):
        async with ctx.typing():
            c = CurrencyRates(force_decimal = True)
            result = c.convert ('USD', 'BRL', 1)
            await ctx.reply(content = f'Um dólar equivale atualmente a R${result:.3}')

    @commands.command(help = 'Comando de ping(criado apenas para efeitos de teste)', aliases = ['p'])
    async def pingnet(self, ctx):
        async with ctx.typing():
            servers = []
            threads = 1

            s = speedtest.Speedtest()
            s.get_servers(servers)
            s.get_best_server()
            s.download(threads=threads)
            s.upload(pre_allocate=False,threads=threads)
            results_dict = s.results.dict()
            await ctx.reply (s.results)


def setup(bot):
    bot.add_cog(Calculators(bot))

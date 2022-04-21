from forx import get_price
import decimal
from disnake.ext import commands
import numexpr as ne


class Calculators(commands.Cog, name = "Calculators"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(help = 'Calcula a expressão dada (Use `/` para divisão, `*` para multiplicação e `**`para potência)', 
    aliases = ['calculadora', 'calcular'])
    async def calc(self, ctx, *, express):
        try:
            soma = ne.evaluate(express)
            await ctx.reply(f":abacus: **|** O resultado é:`{soma}`")
        except (RuntimeError, OverflowError, ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await ctx.reply(f"Desculpe, eu não posso calcular `{express}` ou ocorreu um erro desconhecido.")

    @commands.command(help = 'Diz a cotação do dólar', aliases = ['dol'])
    async def dolar(self, ctx):
        async with ctx.typing():
            g = str(get_price('USD', 'BRL', None)) 
            val = decimal.Decimal(f'{g}').quantize(decimal.Decimal('0.01'))
            vt = val.replace('.',",")

            await ctx.reply(content = f'Um dólar equivale atualmente a R${vt}')

    @commands.command(help = 'Ping do bot com a API do Discord', aliases = ['p'])
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Calc carregado!')

def setup(bot):
    bot.add_cog(Calculators(bot))

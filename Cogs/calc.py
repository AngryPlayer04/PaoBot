from disnake.ext import commands
import numexpr as ne
from datetime import date
import aiohttp

dia = date.today()
diacerto = dia.strftime('%m-%d-%y')

class Calculators(commands.Cog, name = "Calculators"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='calculadora',description = 'Calcula a expressão dada (Use `/` para divisão, `*` para multiplicação e `**`para potência)')
    async def calc(self, inter, express):
        try:
            soma = ne.evaluate(express)
            await inter.response.send_message(f":abacus: **|** O resultado é:`{soma}`")
        except (RuntimeError, OverflowError, ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await inter.response.send_message(f"Desculpe, eu não posso calcular `{express}` ou ocorreu um erro desconhecido.")


    @commands.slash_command(name='ping',description = 'Ping do bot com a API do Discord')
    async def ping(self, inter):
        latency = round(self.bot.latency * 1000)
        await inter.response.send_message(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Calc carregado!')

def setup(bot):
    bot.add_cog(Calculators(bot))

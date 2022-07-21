from disnake.ext import commands
import numexpr as ne
from datetime import date
import aiohttp

dia = date.today()
diacerto = dia.strftime('%m-%d-%y')

class Calculators(commands.Cog, name = "Calculators"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = 'Calcula a expressão dada (Use `/` para divisão, `*` para multiplicação e `**`para potência)', 
    aliases = ['calculadora', 'calcular'])
    async def calc(self, ctx, *, express):
        try:
            soma = ne.evaluate(express)
            await ctx.reply(f":abacus: **|** O resultado é:`{soma}`")
        except (RuntimeError, OverflowError, ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await ctx.reply(f"Desculpe, eu não posso calcular `{express}` ou ocorreu um erro desconhecido.")

    #colocar um if response = 200: continue

    #@commands.command(help = 'Diz a cotação do dólar', aliases = ['dol'])
    #async def dolar(self, ctx):
        #async with ctx.typing():
            #async with aiohttp.ClientSession() as session:
                #async with session.get(f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{diacerto}'&$top=100&$format=json&$select=cotacaoCompra") as res:
                    #data = await res.json()
                    
                    #data = js['cotacaoCompra']
                    #await ctx.reply(f'Um dólar equivale atualmente a R${res}')
                #await session.close()


    @commands.command(help = 'Ping do bot com a API do Discord', aliases = ['p'])
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Calc carregado!')

def setup(bot):
    bot.add_cog(Calculators(bot))

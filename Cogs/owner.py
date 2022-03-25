from wsgiref import headers
from disnake.ext import commands
import requests

token = '5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM'

class OwnerOnly(commands.Cog, name = "Owner Only"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/status/bot/850123093077917716/restart", headers={"api-token": token}).json()
        
    @commands.command(help = 'Busca pelo significado de uma palavra no dicionário.', aliases = ['dicionário', 'dicionario'])
    async def dicio(self, ctx, *, palavra):
        d = requests.get('https://significado.herokuapp.com/v2/', palavra).json()
        await ctx.reply(d)



    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')


def setup(bot):
    bot.add_cog(OwnerOnly(bot))
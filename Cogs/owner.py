from urllib import request
from disnake.ext import commands
import requests


token = 'wwfoQpGct2wHrth7S3eCQbI2wgOT6rv6BydbPn14WVEqTz1GmnOP9opHxP7TKK'

class OwnerOnly(commands.Cog, name = "Owner Only"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/api/v2/app/850123093077917716/restart", headers={"api-token": token}).json()
        
    @commands.command(help = 'Status do bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def status(self, ctx):
        result = requests.get("https://discloud.app/api/v2/app/850123093077917716/status", headers={"api-token": token}).json()
        await ctx.reply(result)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')


def setup(bot):
    bot.add_cog(OwnerOnly(bot))
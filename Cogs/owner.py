import disnake
from disnake.ext import commands
from disnake.utils import format_dt
import requests
import pathlib
import zipfile
import os
import aiohttp
from datetime import datetime, timedelta

token = 'wwfoQpGct2wHrth7S3eCQbI2wgOT6rv6BydbPn14WVEqTz1GmnOP9opHxP7TKK'

class Owner(commands.Cog, name = "Owner"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = 'Logs do bot', aliases = ['log'])
    @commands.is_owner()
    async def logs(self, ctx):
        async with ctx.typing():
            
            re = requests.get("https://discloud.app/api/v2/app/850123093077917716/logs", headers={"api-token": token}).json()
            res = re['logs'][:1018]
            li = re['link']

            oEmbed = disnake.Embed(title = 'Log:', color = 0xffb354, description = f'[Link do log]({li})')
            oEmbed.set_author(name = 'Pão Bot', icon_url = 'https://cdn.discordapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png')
            oEmbed.add_field(name ='\u200b', value = f'```{res}```', inline=False)
            oEmbed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/2125/2125009.png')

            await ctx.reply(embed = oEmbed)


    @commands.command(help = 'Status do bot')
    @commands.is_owner()
    async def status(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://discloud.app/api/v2/app/850123093077917716", headers={"api-token": token}) as res:
                st = await res.json()
                cont = st['container']
                cpu = st['cpu']
                mem = st['memory']
                restart = st['last_restart']
                embed = disnake.Embed(title= 'Status:', color= 0xffb354, description= f'{cont}\n{cpu}\n{mem}\n{restart}')
                await ctx.reply(embed = embed)
            await session.close()


    @commands.command(help = 'Status do plano')
    @commands.is_owner()
    async def user(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://discloud.app/api/v2/user", headers={"api-token": token}) as res:
                st = await res.json()
                plano = st['plan']
                lt = st['lastDataLeft']
                dias = lt['days']
                hour = lt['hours']
                minutos = lt['minutes']
                sec = lt['seconds']
                dt = datetime.now()
                td = timedelta(days= dias, hours= hour, minutes= minutos, seconds= sec)
                planoend = format_dt(dt + td, style='R')
                embed = disnake.Embed(title= 'Info do plano:', color= 0xffb354, description= f'Plano: {plano}\nTermina em {planoend}')
                await ctx.reply(embed = embed)
            await session.close()


    @commands.command(help = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/api/v2/app/850123093077917716/restart", headers={"api-token": token}).json()


    @commands.command(help = 'Faz o backup do bot e envia em zip', aliases = ['b','bk'])
    @commands.is_owner()
    async def backup(self, ctx):

        dire = pathlib.Path('./')
        with zipfile.ZipFile('backup.zip', mode = 'w') as archive:
            for file_path in dire.rglob('*'):
                archive.write(file_path, arcname=file_path.relative_to(dire))
        await ctx.author.send(file = disnake.File(r'backup.zip'))
        os.remove('backup.zip')
        await ctx.message.add_reaction('✅')
        


    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')


def setup(bot):
    bot.add_cog(Owner(bot))

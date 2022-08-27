import disnake
from disnake.ext import commands
from disnake.utils import format_dt
import requests
import pathlib
import zipfile
import os
import aiohttp
from datetime import datetime, timedelta
import pytz

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6InM2STVhbXoydiJ9.KDsWoIwx9sAZUlj9AONK8ArHENl0TQTb68Pf5_wau8Y'

class owner(commands.Cog, name = "Owner"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.slash_command(name='logs',description = 'Logs do bot')
    @commands.is_owner()
    async def logs(self, inter):
        re = requests.get("https://api.discloud.app/v2/app/850123093077917716/logs", headers={"api-token": token}).json()
        #res = re['logs'][:1018]
        #li = re['link']

        oEmbed = disnake.Embed(title = 'Log:', color = 0xffb354, description = f'[Link do log]()')
        oEmbed.set_author(name = 'Pão Bot', icon_url = 'https://cdn.disnakeapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png')
        oEmbed.add_field(name ='\u200b', value = f'```{re#}```', inline=False)
        oEmbed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/2125/2125009.png')

        await inter.response.send_message(embed = oEmbed)


    @commands.slash_command(name='status',description = 'Status do bot')
    @commands.is_owner()
    async def status(self, inter):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.discloud.app/v2/app/850123093077917716", headers={"api-token": token}) as res:
                st = await res.json()
                #cont = st['container']
                #cpu = st['cpu']
                #mem = st['memory']
                #restart = st['last_restart']
                embed = disnake.Embed(title= 'Status:', color= 0xffb354, description= f'{st}')
                await inter.response.send_message(embed = embed)
            await session.close()


    @commands.slash_command(name='usuário',description = 'Status do plano')
    @commands.is_owner()
    async def user(self, inter):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.discloud.app/v2/user", headers={"api-token": token}) as res:
                st = await res.json()
                #plano = st['plan']
                #lt = st['lastDataLeft']
                #dias = lt['days']
                #hour = lt['hours']
                #minutos = lt['minutes']
                #sec = lt['seconds']
                #dt = datetime.now()
                #td = timedelta(days= dias, hours= hour, minutes= minutos, seconds= sec)
                #planoend = format_dt(dt + td, style='R')
                embed = disnake.Embed(title= 'Info do plano:', color= 0xffb354, description= f'Plano: {st}')
                await inter.response.send_message(embed = embed)
            await session.close()


    @commands.slash_command(name='restart',description = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)')
    @commands.is_owner()
    async def restart(self, inter):
        await inter.response.send_message('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://api.discloud.app/v2/app/850123093077917716/restart", headers={"api-token": token}).json()


    @commands.slash_command(name='backup',description = 'Faz o backup do bot e envia em zip', aliases = ['b','bk'])
    @commands.is_owner()
    async def backup(self, inter):

        dire = pathlib.Path('./')
        with zipfile.ZipFile('backup.zip', mode = 'w') as archive:
            for file_path in dire.rglob('*'):
                archive.write(file_path, arcname=file_path.relative_to(dire))
        await inter.author.send(file = disnake.File(r'backup.zip'))
        os.remove('backup.zip')
        await inter.message.add_reaction('✅')
        



    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')



def setup(bot):
    bot.add_cog(owner(bot))

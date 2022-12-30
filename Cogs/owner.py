import disnake
import discloud
from disnake.ext import commands
import requests
import asyncio
import aiohttp

client = discloud.Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6ImgwNzZIVTNsaTJSIn0.dAbllqTlgGyhxJZdJBXPYZcVPULtPNmNBbK0E8Cx39c')
token= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6ImgwNzZIVTNsaTJSIn0.dAbllqTlgGyhxJZdJBXPYZcVPULtPNmNBbK0E8Cx39c'

class owner(commands.Cog, name = "Owner"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.slash_command(name='logs',description = 'Logs do bot')
    @commands.is_owner()
    async def logs(self, inter):
        re = requests.get("https://api.discloud.app/v2/app/850123093077917716/logs", headers={"api-token": token}).json()
        ret = re['apps']
        rei = ret['terminal']
        res = rei['small'][:1018]
        li = rei['url']

        oEmbed = disnake.Embed(title = 'Log:', color = 0xffb354, description = f'[Link do log]({li})')
        oEmbed.set_author(name = 'Pão Bot', icon_url = 'https://cdn.disnakeapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png')
        oEmbed.add_field(name ='\u200b', value = f'```{res}```', inline=False)
        oEmbed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/2125/2125009.png')

        await inter.response.send_message(embed = oEmbed, ephemeral = True)


    @commands.slash_command(name='status',description = 'Status do bot')
    @commands.is_owner()
    async def status(self, inter):
        app = await client.app_info('850123093077917716')
        cont = app.status
        cpu = app.cpu
        mem = app.memory
        restart = app.start_date
        embed = disnake.Embed(title= 'Status:', color= 0xffb354, description= f'{cont}\n{cpu}\n{mem}\n{restart}')
        await inter.response.send_message(embed = embed)
            


    @commands.slash_command(name='usuario',description = 'Status do plano')
    @commands.is_owner()
    async def user(self, inter):
        user = await client.user_info()
        plano = user.plan
        dias = plano.expire_date
        planoend = plano.expires_in
        embed = disnake.Embed(title= 'Info do plano:', color= 0xffb354, description= f'Plano: {plano}\nTermina {planoend}')
        await inter.response.send_message(embed = embed, ephemeral = True)


    @commands.slash_command(name='restart',description = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)')
    @commands.is_owner()
    async def restart(self, inter):
        await inter.response.defer(ephemeral= True)
        await inter.response.send_message('Reiniciando', ephemeral =True)
        await client.restart('850123093077917716')


    @commands.slash_command(name='backup',description = 'Faz o backup do bot e envia em zip')
    @commands.is_owner()
    async def backup(self, inter):

        session = aiohttp.ClientSession()
        resposta = await session.get('https://api.discloud.app/v2/app/850123093077917716/backup').json()

        bac = (resposta['backups'])
        link = bac['url']
        await inter.response.send_message(f'Aqui está o backup:\n{link}', ephemeral = True)
        await session.close()

        
        
    

def setup(bot):
    bot.add_cog(owner(bot))

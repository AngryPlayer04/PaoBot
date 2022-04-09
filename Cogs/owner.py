import disnake
from disnake.ext import commands
import requests


token = 'wwfoQpGct2wHrth7S3eCQbI2wgOT6rv6BydbPn14WVEqTz1GmnOP9opHxP7TKK'

class Owner(commands.Cog, name = "Owner"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = 'Logs do bot', aliases = ['log'])
    @commands.is_owner()
    async def logs(self, ctx):
        async with ctx.typing():
            
            re = requests.get("https://discloud.app/api/v2/app/850123093077917716/logs", headers={"api-token": token}).json()
            res = re['logs']
            li = re['link']

            oEmbed = disnake.Embed(title = '\u200b', color = 0xffb354, description = f'[Link do log]({li})')
            oEmbed.set_author(name = 'Pão Bot logs', icon_url = 'https://cdn.discordapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png')
            oEmbed.add_field(name ='\u200b', value = f'```py \n {res} \n ```', inline=False)
            oEmbed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/2125/2125009.png')

            await ctx.reply(embed = oEmbed)

    @commands.command(help = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/api/v2/app/850123093077917716/restart", headers={"api-token": token}).json()


    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')


def setup(bot):
    bot.add_cog(Owner(bot))
import disnake
from disnake.ext import commands

class help(commands.Cog, name = "Help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='help',description='Ajuda')
    async def ajuda(inter):
        embed = disnake.Embed(color=0xffb354)
        embed.set_author(name="Pão Bot", icon_url="https://cdn.discordapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png")
        embed.add_field(name= 'Ajuda',value="Servidor do bot: https://discord.gg/ZECYSxMjSY \nSite: https://paobot.discloud.app/")
        embed.set_footer(text="*Comando em desenvolvimento",icon_url="https://discord.com/assets/289673858e06dfa2e0e3a7ee610c3a30.svg")
        await inter.response.send_message(embed=embed) 



def setup(bot):
    bot.add_cog(help(bot))







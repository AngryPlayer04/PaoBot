import disnake
from disnake.ext import commands

class HelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = disnake.Embed(description=page, color = 0xffb354)
            mes = 'Sabia que o bot agora tem um servidor? E um site também! \nServidor: https://discord.gg/ZECYSxMjSY \nSite: https://paobot.netfly.app'
            await destination.send(embed=emby)
            await destination.send(mes)


    

class HelpCog(commands.Cog, name = 'Help'):
    '''Mostra os comandos e suas funções'''

    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = HelpCommand()
        bot.help_command.cog = self
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command



def setup(bot):
    bot.add_cog(HelpCog(bot))

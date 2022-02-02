import disnake
from disnake.ext import commands

class HelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{1.qualified_name} {1.signature}'.format(self, command)


    

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

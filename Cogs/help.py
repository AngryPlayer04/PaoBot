import disnake
from disnake.ext import commands

class HelpCommand(commands.MinimalHelpCommand):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    async def send_pages(self,ctx):
        for page in self.paginator.pages:
            emby = disnake.Embed(description=page)
            await ctx.reply(embed=emby)


    



def setup(bot):
    bot.add_cog(HelpCommand(bot))

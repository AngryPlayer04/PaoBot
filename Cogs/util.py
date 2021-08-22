import discord
from discord.ext import commands
import lyricsfinder as lf

class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    

    

def seup(bot):
    bot.add_cog(Utiliies(bot))
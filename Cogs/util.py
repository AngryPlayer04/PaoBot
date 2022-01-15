import discord
from discord.ext import commands


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    




def setup(bot):
    bot.add_cog(Utiliies(bot))
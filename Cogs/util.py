from email import message
from tabnanny import check
import discord
from discord.ext import commands
import lyricsgenius as genius
import aiohttp

api = genius.Genius("Us6gcFcURe9Y85HL6hPY7TRJWQBdVq8WXYiGnJEKokQFobG0v5bzO8MM2Kjy04xU")


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    
    


    




def setup(bot):
    bot.add_cog(Utiliies(bot))
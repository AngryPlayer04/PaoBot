import discord
from discord.ext import commands
from lyricsgenius import Genius 

class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def lyrics(self, ctx, title, artist):
        TOKEN = 'e-jVTE4L7DSjxhi2r8K4hbEw88c0m_BOBLp-6kMozrfWyVyuxdp4mBbbUUzu24l9'
        genius = Genius(TOKEN)
        song = genius.search_song(title, artist)
        await ctx.reply(song.lyrics['lyrics'])




def setup(bot):
    bot.add_cog(Utiliies(bot))
import discord
from discord.ext import commands
from lyricsgenius import Genius 

class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def lyrics(self, ctx, *, artist, name):
        TOKEN = 'e-jVTE4L7DSjxhi2r8K4hbEw88c0m_BOBLp-6kMozrfWyVyuxdp4mBbbUUzu24l9'
        genius = Genius(TOKEN)
        song = genius.search_song(name, artist)
        embed=discord.Embed(title=name, description=song, color=0x0067c2)
        embed.set_author(name=artist)
        embed.set_thumbnail(url='https://camo.githubusercontent.com/2f1afecef9033d21cc42b61763e9de2f28dcebfde75576d317c9dce72eb5c592/68747470733a2f2f696d616765732e67656e6975732e636f6d2f38656436363963616464393536343433653239633730333631656334663337322e31303030783130303078312e706e67')
        embed.add_field(name=None, value=None, inline=False)
        await ctx.reply(embed=embed)




def setup(bot):
    bot.add_cog(Utiliies(bot))
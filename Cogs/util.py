import discord
from discord.ext import commands
import lyricsfinder as lf

class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    

    @commands.command()
    async def lyrics(self, ctx, *, sn):
        api_key = "AIzaSyD_OyEXeF5KCLTN8PjnPxh_XRQMUyfZsBg"
        lyrics = lf.search_lyrics("sn", google_api_key=api_key)
        embed=discord.Embed(title=sn, description=lyrics, color=0x0067c2)
        embed.add_field(name=lf.author, value=None, inline=False)
        await ctx.reply(embed=embed)


def seup(bot):
    bot.add_cog(Utiliies(bot))
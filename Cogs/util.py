import discord
from discord.ext import commands
import lyricsgenius as genius
import aiohttp

api = genius.Genius("Us6gcFcURe9Y85HL6hPY7TRJWQBdVq8WXYiGnJEKokQFobG0v5bzO8MM2Kjy04xU")


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, artist,*, title):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.lyrics.ovh/v1/{artist}/{title}") as response:
                data = await response.json()
                lyrics = data['lyrics']
                if lyrics is None:
                    await ctx.send("Song not found! Please enter correct Artist and Song title")
                if len(lyrics) > 2048:
                    lyrics = lyrics[:2048]
                emb = discord.Embed(title = f"{title}", description = f"{lyrics}", color = 0xa3a3ff)
                await ctx.send(embed=emb)
        await session.close()


    




def setup(bot):
    bot.add_cog(Utiliies(bot))
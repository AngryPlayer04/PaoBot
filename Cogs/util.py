import discord
from discord.ext import commands
import lyricsgenius as genius

api = genius.Genius("Us6gcFcURe9Y85HL6hPY7TRJWQBdVq8WXYiGnJEKokQFobG0v5bzO8MM2Kjy04xU")


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self,ctx, name="Lyrics", aliases=["letras"]):
        try:
            await ctx.reply("Diga o nome do artista")
            a = await self.bot.wait_for('message', check=lambda message: message.author==ctx.author)
            await ctx.send('Qual o nome da música?')
            s = await self.bot.wait_for('message', check=lambda message: message.author==ctx.author)
            lyrics = api.search_song(s, a).lyrics
            await ctx.send(lyrics)

        except:
            await ctx.send('Não encontrei a música solicitada, verifque se digitou corretamente.')


    




def setup(bot):
    bot.add_cog(Utiliies(bot))
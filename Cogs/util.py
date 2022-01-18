import discord
from discord.ext import commands
import lyricsgenius as genius

api = genius.Genius("Us6gcFcURe9Y85HL6hPY7TRJWQBdVq8WXYiGnJEKokQFobG0v5bzO8MM2Kjy04xU")


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self,ctx, name="Lyrics", alias="letras"):
        try:
            a = input(await ctx.reply('Diga o nome do artista'))
            a
            s = input(await ctx.send('Qual o nome da música?'))
            s 
            lyrics = api.search_song(s, a).lyrics
            await ctx.send(lyrics)

        except:
            await ctx.send('Não encontrei a música solicitada, verifque se digitou corretamente.')


    




def setup(bot):
    bot.add_cog(Utiliies(bot))
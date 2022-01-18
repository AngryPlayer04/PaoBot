import discord
from discord.ext import commands
import lyricsgenius as genius

api = genius.Genius("Us6gcFcURe9Y85HL6hPY7TRJWQBdVq8WXYiGnJEKokQFobG0v5bzO8MM2Kjy04xU")


class Utiliies(commands.Cog, name = "Utilities"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, name="Lyrics", alias="letras"):
        try:
            a = input(self.bot.reply('Diga o nome do artista'))
            a
            s = input(self.bot.send('Qual o nome da música?'))
            s 
            lyrics = api.search_song(s, a).lyrics
            await self.bot.send(lyrics)

        except:
            await self.bot.send('Não encontrei a música solicitada, verifque se digitou corretamente.')


    




def setup(bot):
    bot.add_cog(Utiliies(bot))
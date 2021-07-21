import discord
from discord.ext import commands
import wikipedia
import wikipedia

current_language = "pt"

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    @commands.command()
    async def wiki(self, ctx):
        global current_language
        msg = ctx.message.content.split()
        request = msg[2:]
        request = "".join(request)
        error = None
        
        wikicontent = wikipedia.search(request, results=20, suggestion = False )

        if 'wikipedia' in query:
            speak("Searching")
            query = ("wikipedia","")
            result = wikipedia.summary(f'{query}', sentences=2)
            print(result)

        if not wikicontent:
            wikicontent = "Desculpe, não há resultados para `{}`.".format(request)
            embed = discord.Embed(title = "Resultados da pesquisa no Wikipedia:", color = "#e8cda2", descriptionn = wikicontent)
            embed.set_thumbnail(url = "https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
            await ctx.reply(embed = embed)

        elif wikicontent:
            embed = discord.Embed(title = "Resultado da pesquisa no Wikipedia", color = 0, description = "\n".join(wikicontent))
            embed.set_thumbnail(url = "https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
            await ctx.reply(embed=embed)




def setup(bot):
    bot.add_cog(Wiki(bot))
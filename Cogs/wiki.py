import discord
import wikipedia
from discord.ext import commands

current_language = "pt-BR"

class Calc(commands.Cog):
  def __init__(self, bot):
    |
        self.bot = bot 
    @commands.command()
    async def wiki(self, ctx):
      global current_language
      
      msg = ctx.message.content.split(" ")
      request = msg[2:]
      request = " ".join(request)
      error = None

      try:
        
        wikicontent = wikipedia.search(request, results = 20, suggestion = False)
        
        if not wikicontent:
          wikicontent = "Desculpe, não há resultados para '{}'. ".format(request)
           embed = discord.Embed(title = "Resultado da pesquisa do Wikipédia:", color = e8cda2, description = wikicontent)
          embed.set_thumbnail(url = "https://www.wikipedia.org/static/images/project-logos/{}wiki.png").format(current_language))
            await ctx.reply(embed=embed)
            
          else:
            embed = discord.Embed(title = "Resultado da pesquisa do Wikipedia:",color = 0, description = "\n".join(wikicontent)
            embed.set_thumbnail(url = "https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
               await ctx.reply(embed=embed)
              
            except Exception as error:
              error = str(error)
              await ctx.reply("Desculpe, ocorreu um erro aleatório. Por favor tente novamente")
              print (error)
             
def setup(bot):
  bot.add_cog(Wiki(bot)
            
          

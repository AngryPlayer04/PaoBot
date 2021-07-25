import discord 
from discord.ext import commands
import wikipedia


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def wiki(ctx, userInput):
        try: 
            await ctx.send(format(wikipedia.summary(userInput, sentences = 5)))
        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.send(format("Erro: {0}".format(e)))
            await ctx.send ("Erro: muitos resultados, tente novamente com mais detalhes.")





def setup(bot):
    bot.add_cog(Wiki(bot))
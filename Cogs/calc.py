import discord
from discord.ext import commands
import numexpr as ne

class Calculators(commands.Cog, name = "calculator"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.command()
    async def calc(self, ctx, *, express):
        try:
            soma = ne.evaluate(express)
            await ctx.reply(":abacus: **|** O resultado é:`{:2}`".format(soma))

        except (ValueError, SyntaxError, NameError, TypeError, ZeroDivisionError):
            await ctx.reply("Desculpe, eu não posso fazer isso ou ocorreu um erro desconhecido.")


def setup(bot):
    bot.add_cog(Calculators(bot))

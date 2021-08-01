
import discord
from discord.ext import commands
import math
class Calculators(commands.Cog, name="calculator"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
	@commands.command(ctx, *, expression (name = 'calc',usage="(commandName)",description = "Calculator")):
	  soma = eval(expression)
	  await ctx.reply (soma)
	  
	  
def setup(bot):
  bot.add_cog(Calculators)
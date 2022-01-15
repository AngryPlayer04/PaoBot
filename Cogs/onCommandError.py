import disnake as discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
import time


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, CommandNotFound):
			return

		if isinstance(error, CheckFailure):
			await ctx.reply("Desculpe, mas você não tem as permissões necessárias para usar esse comando.")
			print (error)
		if isinstance(error, MissingPermissions):
			print(error)
		raise error

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))

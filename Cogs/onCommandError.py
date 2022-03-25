from disnake.ext import commands
from disnake.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, MemberNotFound


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, CommandNotFound):
			return
		if isinstance(error, MemberNotFound):
			await ctx.reply('Não pude encontar esse membro, certifique-se que usou o ID ouu menção correta e que o membro está neste servidor.')

		if isinstance(error, CheckFailure):
			await ctx.reply("Desculpe, mas você não tem as permissões necessárias para usar esse comando.")
			print (error)
		if isinstance(error, MissingPermissions):
			print(error)
		raise error

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))

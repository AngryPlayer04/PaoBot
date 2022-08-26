from disnake.ext import commands
from disnake.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, MemberNotFound, CommandInvokeError


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, inter, error:commands.CommandError):
		if isinstance(error, CommandNotFound):
			return
		if isinstance(error, MemberNotFound):
			await inter.response.send_message('Não pude encontar esse membro, certifique-se que usou o ID ouu menção correta e que o membro está neste servidor.')
			print(error)

		if isinstance(error, CheckFailure):
			await inter.response.send_message("Desculpe, mas você não tem as permissões necessárias para usar esse comando.")
			print (error)

		if isinstance(error, MissingPermissions):
			print(error)
		
		if isinstance(error, CommandInvokeError):
			await inter.response.send_message('Certifique-se que digitou corretamente.')
			print(error)

		raise error

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))

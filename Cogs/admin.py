from disnake.ext import commands


class AdminOnly(commands.Cog, name = "Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='clear', description = 'Limpa a quantidade indicada de mensagens do canal, sendo 1 por padrão')
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, inter, amount = 1):
        await inter.channel.purge(limit = int(amount) + 1)
        await inter.response.send_message(f'Foram excluídas {amount} mensagens!', ephemeral = True)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin carregado!')


def setup(bot):
    bot.add_cog(AdminOnly(bot))

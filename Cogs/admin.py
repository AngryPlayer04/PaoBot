from disnake.ext import commands


class AdminOnly(commands.Cog, name = "Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(help = 'Limpa a quantidade indicada de mensagens do canal, sendo 5 por padrão', aliases = ['limpar', 'clean'])
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, inter, amount = 5):
        await inter.channel.purge(limit = amount + 1)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin carregado!')




def setup(bot):
    bot.add_cog(AdminOnly(bot))

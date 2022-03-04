import disnake
from disnake.ext import commands
import json
from datetime import datetime
import pytz


current_time = datetime.now()
tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]
    


class PermOnly(commands.Cog, name = "Permonly"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(help = 'Limpa a quantidade indicada de mensagens do canal, sendo 5 por padrão', aliases = ['limpar', 'clean'])
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)





def setup(bot):
    bot.add_cog(PermOnly(bot))

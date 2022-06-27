from disnake import Guild, User
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
    

class AdminOnly(commands.Cog, name = "Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = 'Limpa a quantidade indicada de mensagens do canal, sendo 5 por padrão', aliases = ['limpar', 'clean'])
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command(help = 'Comando para abrir Tickets')
    async def ticket(self, ctx):
        await Guild.create_text_channel(name = ctx.author, overwrites= ctx.author)
        await ctx.send(f'{User.mention}Envie aqui a sua dúvida ou sugestão')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin carregado!')




def setup(bot):
    bot.add_cog(AdminOnly(bot))

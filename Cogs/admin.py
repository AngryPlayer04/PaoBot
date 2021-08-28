import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json
import time


with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

bot = commands.Bot(prefix, owner_id = 319963626108878848)

class AdminOnly(commands.Cog, name = "adminonly"):
    def __init__(self, ctx,):
        self.bot = bot 

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):
        tr = discloud.total_ram()
        ur = discloud.using_ram()
        await ctx.reply("Usando {}/{} de ram".format(ur, tr)) 

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.reply('Calculando...')
        before = time.monotonic()
        await msg.edit(content = "Pong!")
        ping = (time.monotonic() - before) * 1000
        await msg.edit(content = "Pong! <a:paopula:858815343072903178> \n Bot:`{int(ping)}ms`\n API: `{int(self.bot.latency * 1000)}`")

def setup(bot):
    bot.add_cog(AdminOnly(bot))
import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json
import time


with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

bot = commands.Bot(prefix, owner_id = "mydiscordID")

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
        latency = round(bot.latency * 1000, 1)
        await ctx.reply(f'Pong! :paopula: `{latency}ms`')

def setup(bot):
    bot.add_cog(AdminOnly(bot))

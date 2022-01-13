from asyncio import tasks
from unittest import result
import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json
import time
import requests

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]
    


class PermOnly(commands.Cog, name = "Permonly"):
    def __init__(self, bot,):
        self.bot = bot 

    @commands.command()
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5, name = "Clear"):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):
        tr = discloud.total_ram()
        ur = discloud.using_ram()
        await ctx.reply(f'Usando {ur}/{tr} de ram')

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')

    

def setup(bot):
    bot.add_cog(PermOnly(bot))

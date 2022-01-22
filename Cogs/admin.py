from asyncio import tasks
from unittest import result
import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json
import time
import requests
import aiohttp

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
    @commands.is_owner()
    async def restart(self,ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/status/bot/850123093077917716/restart", headers={"api-token": "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM"}).json()

    async def get_data():
        async with aiohttp.ClientSession() as ses:
            async with ses.post("https://discloud.app/status/bot/850123093077917716/restart", headers={"api-token": "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM"}) as res:
                return await res.json()
                
    @commands.command()
    @commands.is_owner()
    async def status(self,ctx):
        result = requests.post("https://discloud.app/status/bot/850123093077917716/status", headers={"api-token": "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM"}).json()
        await ctx.reply('status')

    async def get_data():
        async with aiohttp.ClientSession() as ses:
            async with ses.post("https://discloud.app/status/bot/850123093077917716/status", headers={"api-token": "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM"}) as res:
                return await res.json()

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')



    

def setup(bot):
    bot.add_cog(PermOnly(bot))

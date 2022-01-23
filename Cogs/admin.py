from ast import Mod
from asyncio import tasks
from unittest import result
import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands, tasks
import sys
import os
sys.path.append(os.path.abspath("Mod"))
from discloudapi import *
import json
import time
import requests
from datetime import datetime
import pytz
import aiohttp

current_time = datetime.now()
tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]
    


class PermOnly(commands.Cog, name = "Permonly"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5, name = "Clear"):
        await ctx.channel.purge(limit = amount + 1)


    
    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/status/bot/850123093077917716/restart", headers={"api-token": "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM"}).json()

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        resultado = BotStatus(bot_id = 850123093077917716, api_token = "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM")
        await ctx.reply(f"Uso de CPU: {resultado.cpu}\nUso de memória: {resultado.memory}")
        await ctx.send(f"{resultado.ratelimit_remaining}/{resultado.ratelimit}")


    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    async def on_ready():
        ligado.start()
        ligado.stop()



    @tasks.loop(seconds=10)
    async def ligado(self, ctx):
        user = [319963626108878848]
        resultado = BotRestart(bot_id = 850123093077917716, api_token="5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM")
        for id in user:
            member = await self.bot.fetch_user(id)
            try:
                await member.send(f"Logs completas: {resultado.link}\nÚltimos 1800 caracteres: {resultado.logs}\n Rate Limit:{resultado.ratelimit_remaining}/{resultado.ratelimit} ")
            except:
                pass



def setup(bot):
    bot.add_cog(PermOnly(bot))
def setup(bot):
    bot.add_cog(Events(bot))

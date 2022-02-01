from ast import Mod
from asyncio import tasks
from unittest import result
import disnake
from disnake.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from disnake.ext import commands, tasks
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
        async with ctx.typing():
            resultado = BotStatus(bot_id = 850123093077917716, api_token = "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM")
            embed=disnake.Embed(title='Status', description=(f"Uso de CPU: **{resultado.cpu}**\n Uso de memória: **{resultado.memory}**"), color= 0xffb43b)
            embed.set_author(name='Pão Bot', icon_url= 'https://cdn-icons.flaticon.com/png/512/3226/premium/3226045.png?token=exp=1643694397~hmac=71f7bb1fb6214ecd11e6d2239a6f27f0')
            embed.set_footer(text='Data by Discloud.com')
            await ctx.reply(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def log(self, ctx):
        async with ctx.typing():
            resultado = BotLogs(bot_id = 850123093077917716, api_token = "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM")
            embed=disnake.Embed(title='Log:', url = resultado.link, description=(f" \n {resultado.logs} "), color= 0xffb43b)
            embed.set_author(name='Pão Bot', icon_url= 'https://cdn-icons.flaticon.com/png/512/3226/premium/3226045.png?token=exp=1643694397~hmac=71f7bb1fb6214ecd11e6d2239a6f27f0')
            embed.set_footer(text='Data by Discloud.com')
            await ctx.reply(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Pong! <a:paopula:858815343072903178> `{latency}ms` ')



def setup(bot):
    bot.add_cog(PermOnly(bot))

import disnake
from disnake.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from disnake.ext import commands, tasks
from datetime import datetime
import requests
import sys
import os
sys.path.append(os.path.abspath("Mod"))
from discloudapi import *


token = '5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM'

class OwnerOnly(commands.Cog, name = "Owner Only"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)', aliases = ['reiniciar', 'r'])
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.reply('Reiniciando <a:digitando:931267989033082901>')
        result = requests.post("https://discloud.app/status/bot/850123093077917716/restart", headers={"api-token": token}).json()

def setup(bot):
    bot.add_cog(OwnerOnly(bot))
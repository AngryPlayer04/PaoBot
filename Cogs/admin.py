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
        r = discloud.ram()
        await ctx.reply("Usando {} de ram".format(r)) 

    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.reply("Testing Ping...")
        end_time = time.time()
        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")
        #msg = await ctx.reply('Calculando...')
        #before = time.monotonic()
        #await msg.edit(content = "Pong!")
        #ping = (time.monotonic() - before) * 1000
        #await msg.edit(content = f"Pong!  `{int(ping)}ms`")
        #await ctx.reply("Comando em manutenção!")


def setup(bot):
    bot.add_cog(AdminOnly(bot))
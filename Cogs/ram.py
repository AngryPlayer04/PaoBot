import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json
import platform
import numpy

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

bot = commands.Bot(prefix, owner_id = 319963626108878848)

class AdminOnly(commands.Cog, name = "adminonly"):
    def __init__(self, ctx,):
        self.bot = bot 

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp"]:
            bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960'
            await message.reply(bread)
            await bot.process_commands(message)

    @commands.command()
    async def ping(self, ctx):
        msg = "Pong <a:paopula:858815343072903178> `{0} ms`!".format(numpy.nan_to_num(bot.latency) * 1000)
        await ctx.reply(msg)

    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):
        r = discloud.ram()
        await ctx.reply("Usando {} de ram".format(r)) 



def setup(bot):
    bot.add_cog(AdminOnly(bot))
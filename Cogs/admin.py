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
        await ctx.channel.purge(limit = amount)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp"]:
            bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960'
            await message.reply(bread)
            await bot.process_commands(message)

    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):
        r = discloud.ram()
        await ctx.reply("Usando {} de ram".format(r)) 

    @commands.command()
    async def ping(ctx):
        start_time = time.time()
        message = ctx.reply('Ping:')
        end_time = time.time()
        apiping = round((end_time - start_time) * 1000)
        await message.edit('Ping: {}'.format(apiping))
        print(apiping)


def setup(bot):
    bot.add_cog(AdminOnly(bot))
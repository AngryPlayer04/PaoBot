import discord
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
from discord.ext import commands
import discloud
import json

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

bot = commands.Bot(prefix, owner_id = 319963626108878848)
error = commands.CommandError

class AdminOnly(commands.Cog, name = "adminonly"):
    def __init__(self, ctx,):
        self.bot = bot 
    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):        
            r = discloud.ram()
            await ctx.reply("Usando {} de ram".format(r)) 

    @commands.command(name='clear', help=' this command will clear msgs')
    async def clear(ctx, amount = 5):
        await ctx.channel.purge(limit=amount)
        
    @commands.Cog.listener()
    async def on_message(message):
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp"]:
            bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960'
            await message.reply(bread, mention_author=True)
        await bot.process_commands(message)
    
    @commands.command()
    async def ping(self,ctx):
        msg = "Pong <a:paopula:858815343072903178> `{0} ms`!".format(int(bot.latency * 1000))
        await ctx.reply(msg)

def setup(bot):
    bot.add_cog(AdminOnly(bot))
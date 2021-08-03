import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
import discloud
import json

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]

bot = commands.Bot(prefix, owner_id = 319963626108878848)
error = commands.CommandError

class Owneronly(commands.Cog, name = "owneronly"):
    def __init__(self, ctx,):
        self.bot = bot 
    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):        
        if ctx.message.author.id == 319963626108878848:
            r = discloud.ram()
            # 10
            # dados do us
            ur = discloud.using_ram()
            # dados do total de RAM dis
            tr = discloud.total_ram()
            await ctx.reply("Usando {} de ram".format(r)) 

        if isinstance(error, CheckFailure):
            await ctx.reply("Desculpe,  mas você não é o meu dono.")
def setup(bot):
    bot.add_cog(Owneronly(bot))
import discord
from discord.ext import commands
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
            r = discloud.ram()
            ur = discloud.using_ram()
            tr = discloud.total_ram()
            await ctx.reply("Usando {} de ram.".format(r)) 
def setup(bot):
    bot.add_cog(Owneronly(bot))
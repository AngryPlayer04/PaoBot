import discord
from discord.ext import commands
import discloud
import json

with open("configuration.json", "r") as config: 
	data = json.load(config)
	prefix = data["prefix"]
owner_id = 319963626108878848
bot = commands.Bot(prefix, owner_id)

class Owneronly(commands.Cog, name = "owneronly"):
    def __init__(self, ctx,):
        self.bot = bot 
    @commands.command()
    @commands.is_owner()
    async def ram(self, ctx):
        if ctx.message.author.id == owner_id:
            r = discloud.ram()
            # 100/1024MB
            # dados do uso de RAM
            ur = discloud.using_ram()
            # 100MB
            # dados do total de RAM disponÃ­vel
            tr = discloud.total_ram()
            await ctx.reply("Usando {} de ram".format(r)) # 1GB

        else:
            await ctx.reply("Desculpe, mas você não é o meu dono.")

    #@owneronly.error
    #async def owneronly_error(error, ctx):
        i#f isinstance(error, isnot)
        

def setup(bot):
    bot.add_cog(Owneronly(bot))
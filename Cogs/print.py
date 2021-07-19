import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageFile

class Print(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    @commands.command()
    async def print(self, ctx):
        await ctx.reply("Print")


def setup(bot):
    bot.add_cog(Print(bot))
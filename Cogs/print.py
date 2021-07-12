import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw

class Print(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
    @commands.command()
    async def print(self, ctx):
        imagem = Image.new('RGBA', (700, 200), 'grey')
        fonte = ImageFont.truetype('unisans.ttf', 24)
        text = 'Pão de Açúcar'
        w, h = fonte.getsize(text)
        draw = ImageDraw.Draw(imagem)
        draw.text(((500-w)/2, (500-h)/2), text, font=fonte, fill='white')
        await ctx.reply(Image.show)


def setup(bot):
    bot.add_cog(Print(bot))
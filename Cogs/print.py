import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageFile

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
        ImageFi.save('/Paes/print.png')
        await ctx.reply(file=discord.File('/Paes/print.png'))


def setup(bot):
    bot.add_cog(Print(bot))
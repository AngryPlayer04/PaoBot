import disnake
from disnake.ext import commands 
from random import choice, randrange
import requests


class Util(commands.Cog, name = "Utility Commands"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot 
    @commands.command()
    async def flip(self, ctx):
        moeda = randrange(1,3)
        if moeda == 1:
            await ctx.reply(":slight_smile: Cara!")
        else:
            await ctx.reply(":crown: Coroa!")

    @commands.command()
    async def receita(self, ctx):
        lin = "https://www.tudogostoso.com.br/receita/72313-pao-caseiro-facil.html",\
        "https://www.tudogostoso.com.br/receita/79996-pao-de-queijo-3-ingredientes.html", \
        "https://www.tudogostoso.com.br/receita/83-pao-de-batata.html", \
        "https://www.tudogostoso.com.br/receita/105067-pao-recheado.html"
        await ctx.reply(choice(lin))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp","🍞"]:
            bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960',\
                'https://tenor.com/view/cat-bread-gif-9824952',\
                'https://tenor.com/view/toasty-the-walking-toast-bread-gif-7333840',\
                'https://tenor.com/view/dogebred-bread-dog-spin-gif-14407769'
            await message.reply(choice(bread))
            
    @commands.command(help = 'Envia o avatar de um usuário, podendo ser uma menção ou ID', aliases = ['pfp','icon', 'icone', 'ícone'])
    async def avatar(self,ctx, *, usuario: disnake.Member = None):

        if usuario is None:
            usuario = ctx.author
        memberAvatar = usuario.avatar.url
        aEmbed = disnake.Embed(title = usuario.name, color=0xffb354, description= f'[Avatar:]({memberAvatar})')
        aEmbed.set_image(url=memberAvatar)
        await ctx.reply(embed = aEmbed)
        
    @commands.command(help = 'Busca pelo significado de uma palavra no dicionário.', aliases = ['dicionário', 'dicionario'])
    async def dicio(self, ctx, *, palavra):
        async with ctx.typing():
            d = requests.get(f'https://significado.herokuapp.com/v2/{palavra}').json()

            res = str(d[0]['meanings'])[1:-1]
            gen = str(d[0]['partOfSpeech'])
            eti = str(d[0]['etymology'])
            ult = res.replace('[','**').replace(']',':**').replace("'","").replace('.,','.').replace('.', '.\n')

            dEmbed = disnake.Embed(title = palavra.capitalize(), color = 0xffb354, description = gen.capitalize())
            dEmbed.set_thumbnail(url = 'https://purepng.com/public/uploads/large/purepng.com-dictionary-icon-android-lollipopsymbolsiconsgooglegoogle-iconsandroid-lollipoplollipop-iconsandroid-50-721522597173cj5xd.png')
            dEmbed.add_field(name = 'Etimologia:', value = eti + "\n\u200b", inline = False)
            dEmbed.add_field(name = 'Significado:', value = ult, inline = False) 

            await ctx.reply(embed = dEmbed) 


    @commands.Cog.listener()
    async def on_ready(self):
        print ('Fun carregado!')
        print('===============================')


def setup(bot):
    bot.add_cog(Util(bot))

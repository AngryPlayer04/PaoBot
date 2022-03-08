import disnake
from disnake.ext import commands 
from random import choice, randrange


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
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp"]:
            bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960',\
                'https://tenor.com/view/cat-bread-gif-9824952',\
                'https://tenor.com/view/toasty-the-walking-toast-bread-gif-7333840',\
                'https://tenor.com/view/dogebred-bread-dog-spin-gif-14407769'
            await message.reply(choice(bread))
            
    @commands.command()
    async def avatar(self,ctx, usuario: disnake.Member = None):
        avaEmbed = disnake.Embed(title = f"Avatar de {usuario.name}", color=0xfafafa)
        avaEmbed.set_footer(text=f"Pão Bot, todos os direitos reservados.")
        avaEmbed.set_image(url=memberAvatar)

        if usuario == None:
            usuario = ctx.author

            memberAvatar = usuario.avatar.url
            await ctx.reply(embed = avaEmbed)
        



    @commands.Cog.listener()
    async def on_ready(self):
        print ('Fun carregado!')


def setup(bot):
    bot.add_cog(Util(bot))

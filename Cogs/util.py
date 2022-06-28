from async_timeout import timeout
import disnake 
from disnake.ext import commands
from random import choice, randrange, randint
import requests
from translate import Translator
import aiohttp
import json
import asyncio


class Util(commands.Cog, name = "Utility"):
    def __init__(self, bot):
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
        session = aiohttp.ClientSession()
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp","🍞"]:
            if message.author.bot:
                return
            
            else:
                response = await session.get('http://api.giphy.com/v1/gifs/search?q=bread&api_key=GiIoyyWzwxGb4h8VOw62xA3mqano25E9&limit=50')
                data = json.loads(await response.text())
                gifch = randint(0, 49)
                bread = (data['data'][gifch]['images']['original']['url'])
            
                bembed = disnake.Embed(color=0xffb354)
                bembed.set_image(bread)
                bembed.set_author(name="Pão Bot", icon_url="https://images-ext-2.discordapp.net/external/lK0peJ7nECCGR6-5ND3L1ysNwT1Iq1DVkHJoF19Pwcg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png")
                bembed.set_footer(text='Powered by GIPHY', icon_url='https://giphy.com/static/img/about/stickers/logo-spin.gif')
                await message.reply(embed = bembed)
            
        await session.close()

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

    @commands.command(help = 'Traduz do inglês para o português', aliases = ['translate', 'tl', 'tradutor'])
    async def traduzir(self, ctx, *, origem):
        if '@everyone' in origem:
            await ctx.reply('Nada de mencionar todo mundo')

        else:
            async with ctx.typing():
                tl = Translator(to_lang = 'pt-br')
                tn = tl.translate(origem)
                await ctx.reply(tn)

    @commands.command(help = 'Comando para abrir Tickets')
    async def ticket(self, ctx):
        permissao1 = {
        ctx.guild.default_role: disnake.PermissionOverwrite(read_messages = False),
        ctx.guild.me: disnake.PermissionOverwrite(read_messages = True),
        ctx.author: disnake.PermissionOverwrite(read_messages = True)
        }

        permissao2 = {
        ctx.guild.default_role: disnake.PermissionOverwrite(read_messages = False),
        ctx.guild.me: disnake.PermissionOverwrite(read_messages = True),
        }

        chan = await disnake.Guild.create_text_channel(ctx.guild, name = f'{ctx.author}', overwrites= permissao1)
        await ctx.reply(f'Envie no {chan.mention} a sua dúvida ou sugestão')
        await chan.send(f'{ctx.author.mention} envie aqui a sua dúvida ou sugestão dentro de uma única mensagem')
        await asyncio.sleep(20)
        
        if disnake.utils.get(disnake.Guild.text_channels, name = 'Ticket-Logs'):
            mensagem = await chan.fetch_message(chan.last_message_id)
            await lg.send(f'De <@{mensagem.id}>: \n{mensagem.content}')
            await chan.delete()

        else:
            lg = await disnake.Guild.create_text_channel(ctx.guild, name = 'Ticket-Logs', overwrites= permissao2)
            mensagem = await chan.fetch_message(chan.last_message_id)
            await lg.send(f'De <@{mensagem.id}>: \n{mensagem.content}')
            await chan.delete()


    @commands.Cog.listener()
    async def on_ready(self):
        print ('Fun carregado!')
        print('===============================')


def setup(bot):
    bot.add_cog(Util(bot))

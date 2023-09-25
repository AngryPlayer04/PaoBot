from async_timeout import timeout
import disnake
from disnake import app_commands, message
from disnake.ext import commands
from random import choice, randrange, randint
import requests
from translate import Translator
import aiohttp
import json
import asyncio
from mongo.mongomain import get_database
from random import randint


with open("configuration.json", "r") as config: 
    data = json.load(config)
    giphykey = data["giphykey"]


class util(commands.Cog, name = "Utility"):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.slash_command(name='flip',description='Cara ou coroa')
    async def flip(inter):
        moeda = randrange(0,6)
        if moeda >= 3:
            await inter.response.send_message(":slight_smile: Cara!")
        if moeda < 3:
            await inter.response.send_message(":crown: Coroa!")


    @commands.slash_command(name='receitas',description='Envia receitas de pão')
    async def receitas(inter):

        minhadb = get_database()
        collecion_name = minhadb['receitas_links']
        count = collecion_name.count_documents({})
        random_index = randint(0, count -1)
        aleatorio = collecion_name.find().limit(1).skip(random_index)
        resultado = aleatorio[0]
        link = resultado['link']

        await inter.response.send_message(link)

    @commands.Cog.listener()
    async def on_message(self, message):
        session = aiohttp.ClientSession()
        if message.content in ["Pão", "pão", "bread", "Bread", "Oãp","🍞"]:
            if message.author.bot:
                return
            
            else:
                response = await session.get(f'http://api.giphy.com/v1/gifs/search?q=bread&api_key={giphykey}&limit=50')
                data = json.loads(await response.text())
                gifch = randint(0, 49)
                bread = (data['data'][gifch]['images']['original']['url'])
            
                bembed = disnake.Embed(color=0xffb354)
                bembed.set_image(bread)
                bembed.set_author(name="Pão Bot", icon_url="https://images-ext-2.disnakeapp.net/external/lK0peJ7nECCGR6-5ND3L1ysNwT1Iq1DVkHJoF19Pwcg/%3Fsize%3D1024/https/cdn.disnakeapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png")
                bembed.set_footer(text='Powered by GIPHY', icon_url='https://giphy.com/static/img/about/stickers/logo-spin.gif')
                await message.reply(embed = bembed)
        await session.close()

    @commands.slash_command(name='avatar',description='Envia o avatar de um usuário, podendo ser uma menção ou ID')
    async def avatar(inter, usuario: disnake.Member = None):

        if usuario is None:
            usuario = inter.author
        memberAvatar = usuario.avatar.url
        print(usuario)
        aEmbed = disnake.Embed(title = usuario.name, color=0xffb354, description= f'[Avatar:]({memberAvatar})')
        aEmbed.set_image(url=memberAvatar)
        await inter.response.send_message(embed = aEmbed)
        
    @commands.slash_command(name='dicionário',description = 'Busca pelo significado de uma palavra no dicionário.')
    async def dicio( inter, palavra):

        d = requests.get(f'https://significado.herokuapp.com/v2/{palavra}').json()

        res = str(d[0]['meanings'])[1:-1]
        gen = str(d[0]['partOfSpeech'])
        eti = str(d[0]['etymology'])
        ult = res.replace('[','**').replace(']',':**').replace("'","").replace('.,','.').replace('.', '.\n')

        dEmbed = disnake.Embed(title = palavra.capitalize(), color = 0xffb354, description = gen.capitalize())
        dEmbed.set_thumbnail(url = 'https://purepng.com/public/uploads/large/purepng.com-dictionary-icon-android-lollipopsymbolsiconsgooglegoogle-iconsandroid-lollipoplollipop-iconsandroid-50-721522597173cj5xd.png')
        dEmbed.add_field(name = 'Etimologia:', value = eti + "\n\u200b", inline = False)
        dEmbed.add_field(name = 'Significado:', value = ult, inline = False) 

        await inter.response.send_message(embed = dEmbed) 

    @commands.slash_command(name='tradutor',description = 'Traduz do inglês para o português')
    async def traduzir( inter, origem):
        if '@everyone' in origem:
            await inter.response.send_message('Nada de mencionar todo mundo')

        else:
            tl = Translator(to_lang = 'pt-br')
            tn = tl.translate(origem)
            await inter.response.send_message(tn)

    @commands.slash_command(name='ticket',description = 'Comando para abrir Tickets')
    async def ticket(self, inter):

        permissao1 = {
        inter.guild.default_role: disnake.PermissionOverwrite(read_messages = False),
        inter.guild.me: disnake.PermissionOverwrite(read_messages = True),
        inter.author: disnake.PermissionOverwrite(read_messages = True)
        }

        permissao2 = {
        inter.guild.default_role: disnake.PermissionOverwrite(read_messages = False),
        inter.guild.me: disnake.PermissionOverwrite(read_messages = True),
        }

        chan = await disnake.Guild.create_text_channel(inter.guild, name = f'{inter.author}', overwrites= permissao1)
        await inter.response.send_message(f'Envie no {chan.mention} a sua dúvida ou sugestão')
        await chan.send(f'{inter.author.mention} envie aqui a sua dúvida ou sugestão dentro de uma única mensagem')
        await asyncio.sleep(30) #mudar pra 30 ou mais após dar certo
        
        canal = disnake.utils.get(inter.guild.text_channels, name = 'ticket-logs')
        
        if canal:
            mensagem = await chan.fetch_message(chan.last_message_id)
            if mensagem.author.bot:
                await chan.delete()
            else:
                await canal.send(f'De {mensagem.author.id}({mensagem.author}): \n{mensagem.content}')
                await chan.delete()

        else:
            lg = await disnake.Guild.create_text_channel(inter.guild, name = 'ticket-logs', overwrites= permissao2)
            mensagem = await chan.fetch_message(chan.last_message_id)
            await lg.send(f'De {mensagem.author.id}({mensagem.author}): \n```{mensagem.content}```')
            await chan.delete()
    

    @commands.slash_command(name='clima', description='Mostra o clima da cidade que o usuário pedir')
    async def clima(inter):#, cidade, estado):
        
        #colocar todas as opções dos estados seguindo a documentação do climatempo
        #colocar também ratelimit no comando

        #city = cidade.casefold()
        #cembed = disnake.Embed(title = f"Clima em {cidade}", color = 0xffb354, description = f'[Resultado completo](https://wttr.in/{city})')
        #cembed.set_image(url=f"https://wttr.in/{city}_m_0pq_transparency=300_lang=pt.png")
        #await inter.response.send_message(embed = cembed)
        
        await inter.response.send_message("Comando em manutenção!!")
        

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Fun carregado!')
        print('===============================')


def setup(bot):
    bot.add_cog(util(bot))


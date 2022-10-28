import disnake
import discloud
from disnake.ext import commands
import requests
import pathlib
import zipfile
import os
import json
import tweepy as twitter
import time
import datetime
import asyncio

client = discloud.Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6InM2STVhbXoydiJ9.KDsWoIwx9sAZUlj9AONK8ArHENl0TQTb68Pf5_wau8Y')
token= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6InM2STVhbXoydiJ9.KDsWoIwx9sAZUlj9AONK8ArHENl0TQTb68Pf5_wau8Y'




class owner(commands.Cog, name = "Owner"):
    def __init__(self, bot):
        self.bot = bot 

    @commands.slash_command(name='logs',description = 'Logs do bot')
    @commands.is_owner()
    async def logs(self, inter):
        re = requests.get("https://api.discloud.app/v2/app/850123093077917716/logs", headers={"api-token": token}).json()
        ret = re['apps']
        rei = ret['terminal']
        res = rei['small'][:1018]
        li = rei['url']

        oEmbed = disnake.Embed(title = 'Log:', color = 0xffb354, description = f'[Link do log]({li})')
        oEmbed.set_auteor(name = 'Pão Bot', icon_url = 'https://cdn.disnakeapp.com/avatars/850123093077917716/2fe303ab1bf685becf029d72834b0f16.png')
        oEmbed.add_field(name ='\u200b', value = f'```{res}```', inline=False)
        oEmbed.set_thumbnail(url = 'https://cdn-icons-png.flaticon.com/512/2125/2125009.png')

        await inter.response.send_message(embed = oEmbed, ephemeral = True)


    @commands.slash_command(name='status',description = 'Status do bot')
    @commands.is_owner()
    async def status(self, inter):
        app = await client.app_info('850123093077917716')
        cont = app.status
        cpu = app.cpu
        mem = app.memory
        restart = app.last_restart
        embed = disnake.Embed(title= 'Status:', color= 0xffb354, description= f'{cont}\n{cpu}\n{mem}\n{restart}')
        await inter.response.send_message(embed = embed)
            


    @commands.slash_command(name='usuario',description = 'Status do plano')
    @commands.is_owner()
    async def user(self, inter):
        user = await client.user_info()
        plano = user.plan
        dias = plano.expire_date
        planoend = plano.expires_in
        embed = disnake.Embed(title= 'Info do plano:', color= 0xffb354, description= f'Plano: {plano}\nTermina {planoend}')
        await inter.response.send_message(embed = embed, ephemeral = True)


    @commands.slash_command(name='restart',description = 'Reinicia o bot(*Apenas o dono do bot pode utilizar este comando*)')
    @commands.is_owner()
    async def restart(self, inter):
        await client.restart('850123093077917716')


    @commands.slash_command(name='backup',description = 'Faz o backup do bot e envia em zip')
    @commands.is_owner()
    async def backup(self, inter):
        await inter.response.defer(with_message = True, ephemeral = True)

        dire = pathlib.Path('./')
        with zipfile.ZipFile('backup.zip', mode = 'w') as archive:
            for file_path in dire.rglob('*'):
                archive.write(file_path, arcname=file_path.relative_to(dire))
        await inter.edit_original_message(file = disnake.File(rb'backup.zip'))
        os.remove('backup.zip')
        
    @commands.Cog.listener()
    async def on_time():

        #Autenticação do bot

        aute = twitter.OauthHandler('f2pBkuQmLbPnkxTiQKDRQ3tDo','DWTU0wDbVhBPO0AlwsvLE4kXb7Qmko0Sadzxlr6WOhgmOj6m0C') 
        aute.set_access_token('1437949410990858244-Od2zyTfIwnrUoUBrqoalIxkmJGJ28n', 'LruNOhJq8000CqVRt1RMRJAh4zaXtHXYKJOL4CYd9WQwO')
        api = twitter.API(aute)

        try: 
            api.verify_credentials()
            print ("Autenticado!")

        except:
            print("Não autenticado!")

        #Criação do objeto da API

        api = twitter.API(aute, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

        #Retweet

        hashtag = '#ForzaHorizon5', '#XboxShare'

        def twitter_bot(hashtag):
            while True:
                tz_SP = pytz.timezone('America/Sao_Paulo')
                datetime_SP = datetime.now(tz_SP)
                tempo = datetime_SP.strftime("%H:%M")
                hora = '19:00'
                print(tempo)
                if tempo == hora:
                    for tweet in twitter.Cursor(api.search, q=hashtag, rpp=20,).items(2):
                        try:

                            tweet_id = dict(tweet._json)['id']
                            tweet_text = dict(tweet._json)['text']
                            api.retweet(tweet_id)
                        except twitter.TweepError as error:
                            print(error.reason)
            twitter_bot(hashtag)
            asyncio.sleep(50)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner carregado!')



def setup(bot):
    bot.add_cog(owner(bot))

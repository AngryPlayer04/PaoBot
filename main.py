import disnake
from disnake import channel
from disnake.ext import commands, tasks
import json
import sys
import os 
from datetime import datetime 
import pytz
from itertools import cycle
import asyncio
import requests
sys.path.append(os.path.abspath("Mod"))
from discloudapi import *

# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  


# Intents
intents = disnake.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)

#status= cycle(['p.help', 'Pão', 'Bread', f'Estou em {int(len(bot.guilds))} servidores'])
current_time = datetime.now()
tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

@bot.event
async def on_ready():
  bot.load_extension('cogs.')

for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():


  print ('===============================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')
  #print (len(bot.guilds))
  print ('===============================')

  ligado.start()
  
  bot.loop.create_task(status_task())
  ligado.stop()

@tasks.loop(seconds=11)
async def ligado():
  user = [319963626108878848]
  for id in user:
    member = await bot.fetch_user(id)
    try:
      await member.send(f'{member.mention} Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')
    except:
      pass


async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'Digite {prefix}help | Estou em {len(bot.guilds)} servidores'),status=disnake.Status.online)
        await asyncio.sleep(1800)


@tasks.loop(hours = 8)
async def verifydays(self,ctx):
  result = UserStatus(api_token = "5UdvclE49xDuQXVhZ3rLJLRtPWkEB7vU7TrPNRPAukiUFdw9VKoAfB8THRcV9IM")
  r = result.planDataEnd
  if r <= 1:
    cas = bot.get_user(319963626108878848)
    await cas.send('**O PLANO TA ACABANDO, FAZ BACKUP!!**')

@verifydays.before_loop
async def before_my_task():
    await bot.wait_until_ready()




bot.run(token)

import discord
from discord import channel
from discord.ext import commands, tasks
import json
import os 
from datetime import datetime 
import pytz
from itertools import cycle
import asyncio
import requests

# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  


# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)

#status= cycle(['p.help', 'Pão', 'Bread', f'Estou em {int(len(bot.guilds))} servidores'])
current_time = datetime.now()
tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

@bot.event
async def on_ready():
  bot.load_extension('cogs.')

for filename in os.listdir('Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():


  print ('============================================')
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
      member.send(f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')
    except:
      pass


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                name=f'Digite {prefix}help caso precise de ajuda | Estou em {len(bot.guilds)} servidores'),status=discord.Status.online)
        await asyncio.sleep(1800)






bot.run(token)

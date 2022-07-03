import disnake
from disnake.ext import commands
import json
import os 
from datetime import datetime 
import pytz
import asyncio
import requests

# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  apitoken = data['api-token']


# Intents
intents = disnake.Intents.default()
intents.message_content = True

# The bot
bot = commands.Bot(prefix, intents = intents, case_insensitive = True)

tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

@bot.event
async def on_ready():
  bot.load_extension('cogs.')

for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')

async def on_ready():


  print ('===============================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')

  
  bot.loop.create_task(status_task())
  #ligado.stop()
  del bot.on_ready





async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'Digite {prefix}help | Estou em {len(bot.guilds)} servidores'),status=disnake.Status.do_not_disturb)
        await asyncio.sleep(1800)



bot.run(token)

import discord
from discord.ext import commands, tasks
import json
import os 
from datetime import datetime 
import pytz
from itertools import cycle
import asyncio

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

@bot.event
async def on_ready():
  bot.load_extension('cogs.')

for filename in os.listdir('Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():
  status= cycle(['p.help', 'Pão', 'Bread', f'Estou em {len(bot.guilds)} servidores'])

  tz_BR = pytz.timezone('America/Sao_Paulo') 
  datetime_BR = datetime.now(tz_BR)
  print ('============================================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')
  #print (len(bot.guilds))
  print ('===============================')
  
  bot.loop.create_task(status_task())
    

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                name=f'Digite {prefix}help caso precise de ajuda | Estou em {len(bot.guilds)-2} servidores'),status=discord.Status.online)
        await asyncio.sleep(1800)




bot.run(token)

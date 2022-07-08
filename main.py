from asyncio import tasks
import disnake
from disnake.ext import commands, tasks
import json
import os 
from datetime import datetime 
import pytz
import asyncio
import aiohttp

# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  

  apitoken = "s3UGc5HvsXtePkAEd1km278lttmqfS4oBX4VW74Qw2Tmpud0Ptyc74PdDU7T7"


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

@bot.event
async def on_ready():



  print ('===============================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')

  

  bot.loop.create_task(status_task())
  bot.loop.create_task(tempo_task())
  

  member = bot.get_channel(992499815529316473)
  
  await member.send(f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')



async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'Digite {prefix}help | Estou em {len(bot.guilds)} servidores'),status=disnake.Status.do_not_disturb)
        await asyncio.sleep(1800)


async def tempo_task(self):

  tz_SP = pytz.timezone('America/Sao_Paulo') 
  datetime_SP = datetime.now(tz_SP) 
  tempo = datetime_SP.strftime("%H:%M")
  hora = '19:49'
  if tempo == hora:
    print('o tempo bateu')
  if tempo != hora:
    print('nao é hora')
    
 
 

bot.run(token)

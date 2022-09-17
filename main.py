import disnake
from disnake.ext import commands
import json
import discloud
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
  

  client = discloud.Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6InM2STVhbXoydiJ9.KDsWoIwx9sAZUlj9AONK8ArHENl0TQTb68Pf5_wau8Y')


# Intents
intents = disnake.Intents.default()
intents.message_content = True

# The bot
bot = commands.Bot(prefix, intents = intents, case_insensitive = True, sync_commands_debug= True)

tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)


@bot.event
async def on_ready():

  print ('===============================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')

  

  bot.loop.create_task(status_task())
  bot.loop.create_task(tempo_task())
  del bot.on_ready

  member = bot.get_channel(992499815529316473)
  
  await member.send(f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')



async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'/ | Estou em {len(bot.guilds)} servidores'),status=disnake.Status.online)
        await asyncio.sleep(1800)


async def tempo_task():
  while True:
    tz_SP = pytz.timezone('America/Sao_Paulo')
    datetime_SP = datetime.now(tz_SP)
    tempo = datetime_SP.strftime("%H:%M")
    hora = '00:00'
    if tempo == hora:
      await client.restart_app('850123093077917716')
    if tempo != hora:
      pass
    await asyncio.sleep(25)



bot.load_extensions('./Cogs')

bot.run(token)

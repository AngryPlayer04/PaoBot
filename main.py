import disnake
from disnake.ext import commands
import json
from datetime import datetime 
import pytz
import asyncio
import requests


# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  

  apitoken = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOTk2MzYyNjEwODg3ODg0OCIsImtleSI6InM2STVhbXoydiJ9.KDsWoIwx9sAZUlj9AONK8ArHENl0TQTb68Pf5_wau8Y')


# Intents
intents = disnake.Intents.default()
intents.message_content = True

# The InteractionBot
InteractionInteractionBot = commands.InteractionBot(intents = intents, sync_commands_debug= True)

tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)


@InteractionInteractionBot.event
async def on_ready():

  print ('===============================')
  print (f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')

  

  InteractionBot.loop.create_task(status_task())
  InteractionBot.loop.create_task(tempo_task())
  del InteractionBot.on_ready

  member = InteractionBot.get_channel(992499815529316473)
  
  await member.send(f'Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')



async def status_task():
    while True:
        await InteractionBot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'/ | Estou em {len(InteractionBot.guilds)} servidores'),status=disnake.Status.online)
        await asyncio.sleep(1800)


async def tempo_task():

  while True:
    tz_SP = pytz.timezone('America/Sao_Paulo')
    datetime_SP = datetime.now(tz_SP)
    tempo = datetime_SP.strftime("%H:%M")
    hora = '00:00'
    if tempo == hora:
      await asyncio.sleep(60)
      requests.put("https://api.discloud.app/v2/app/850123093077917716/restart", headers={"api-token":apitoken})
    if tempo != hora:
      pass
    await asyncio.sleep(25)



InteractionBot.load_extensions('./Cogs')

InteractionBot.run(token)

import discord
from discord.ext import commands
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
  

  apitoken = "s3UGc5HvsXtePkAEd1km278lttmqfS4oBX4VW74Qw2Tmpud0Ptyc74PdDU7T7"


# Intents
intents = discord.Intents.default()
intents.message_content = True

# The bot
bot = commands.Bot(prefix, intents = intents, case_insensitive = True)

tz_BR = pytz.timezone('America/Sao_Paulo') 
datetime_BR = datetime.now(tz_BR)

@bot.event
async def on_ready():
  for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'Cogs.{filename[:-3]}')

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
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                name=f'Digite {prefix}help | Estou em {len(bot.guilds)} servidores'),status=discord.Status.online)
        await asyncio.sleep(1800)


async def tempo_task():
  while True:
    tz_SP = pytz.timezone('America/Sao_Paulo')
    datetime_SP = datetime.now(tz_SP)
    tempo = datetime_SP.strftime("%H:%M")
    hora = '00:00'
    if tempo == hora:
      requests.post("https://discloud.app/api/v2/app/850123093077917716/restart", headers={"api-token": apitoken})
    if tempo != hora:
      pass
    await asyncio.sleep(25)



bot.run(token)

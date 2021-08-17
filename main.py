import discord
from discord.ext import commands, tasks
import json
import os 
from datetime import datetime 
import pytz
from itertools import cycle

# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)
status = cycle(['Prefix: p.', 'Pão', 'Bread'])

current_time = datetime.now()

@bot.event
async def on_ready():
  bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():
  tz_BR = pytz.timezone('America/Sao_Paulo') 
  datetime_BR = datetime.now(tz_BR)
  print ('===============================')
  print('Acordei pra tomar café às {}'.format(datetime_BR.strftime("%H:%M")))
  print ('===============================')
  change_status.start()  

@bot.command
async def ping(ctx):
  msg = "Pong <a:paopula:858815343072903178> `{0} ms`!".format(int(bot.latency * 1000))
  await ctx.reply(msg) 

@tasks.loop(seconds = 15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))



bot.run(token)

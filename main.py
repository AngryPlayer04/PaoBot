import discord
from discord.ext import commands, tasks
import json
import os 
import platform
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
  tz_BR = pytz.timezone('America/Sao_Paulo') 
  datetime_BR = datetime.now(tz_BR)
  print('Acordei pra tomar café às {}'.format(datetime_BR.strftime("%H:%M")))
  change_status.start()


@tasks.loop(seconds = 20)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))
      

@bot.command(name='clear', help=' this command will clear msgs')
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount)

#Ping
@bot.command()
async def ping(ctx):
    msg = "Pong <a:paopula:858815343072903178> `{0} ms`!".format(int(bot.latency * 1000))
    await ctx.send(msg)
  

@bot.event
async def on_message(message):
  if message.content == "Pão":
    await message.reply(':bread:', mention_author=True)
  if message.content == "pão":
    await message.reply(':bread:', mention_author=True)
  if message.content == "bread":
    await message.reply(':bread:', mention_author=True)
  if message.content == "Bread":
    await message.reply(':bread:', mention_author=True)
  if message.content == "Oãp":
    await message.reply(':bread:', mention_author=True)
  await bot.process_commands(message)
    

bot.run(token)

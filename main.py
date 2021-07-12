import discord
from discord.ext import commands, tasks
import json
import os 
import platform
from datetime import datetime 
import pytz
import random
import PIL
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

@bot.event 
async def on_ready():
  ctx.send('Oi', message.author = 319963626108878848)


@tasks.loop(seconds = 15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))
      

@bot.command(name='clear', help=' this command will clear msgs')
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount)

#Ping
@bot.command()
async def ping(ctx):
    msg = "Pong <a:paopula:858815343072903178> `{0} ms`!".format(int(bot.latency * 1000))
    await ctx.reply(msg)
  
@bot.command(name= 'receita', help='this command send a random recipe')
async def receita(ctx):
  lin = "https://www.tudogostoso.com.br/receita/72313-pao-caseiro-facil.html",\
 "https://www.tudogostoso.com.br/receita/79996-pao-de-queijo-3-ingredientes.html", \
 "https://www.tudogostoso.com.br/receita/83-pao-de-batata.html", \
 "https://www.tudogostoso.com.br/receita/105067-pao-recheado.html"
  await ctx.reply(random.choice(lin))

@bot.event
async def on_message(message):
  bread = 'https://tenor.com/view/falling-bread-bread-gif-19081960'
  if message.content == "Pão":
    await message.reply(bread, mention_author=True)
  elif message.content == "pão":
    await message.reply(bread, mention_author=True)
  elif message.content == "bread":
    await message.reply(bread, mention_author=True)
  elif message.content == "Bread":
    await message.reply(bread, mention_author=True)
  elif message.content == "Oãp":
    await message.reply(bread, mention_author=True)
  await bot.process_commands(message)
    

bot.run(token)

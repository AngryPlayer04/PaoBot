import disnake
from disnake.ext import commands, tasks
import json
import os 
from datetime import datetime 
import pytz
import asyncio


# Get configuration.json
with open("configuration.json", "r") as config: 
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]
  


# Intents
intents = disnake.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, case_insensitive = True)

#status= cycle(['p.help', 'Pão', 'Bread', f'Estou em {int(len(bot.guilds))} servidores'])

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


  ligado.start()
  
  bot.loop.create_task(status_task())
  ligado.stop()

@tasks.loop(seconds=5)
async def ligado():
  user = [319963626108878848]
  for id in user:
    member = await bot.fetch_user(id)
    try:
      await member.send(f'{member.mention} Acordei pra tomar café às {(datetime_BR.strftime("%H:%M"))}')
    except:
      pass


async def status_task():
    while True:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching,
                name=f'Digite {prefix}help | Estou em {len(bot.guilds)} servidores'),status=disnake.Status.online)
        await asyncio.sleep(1800)








bot.run(token)

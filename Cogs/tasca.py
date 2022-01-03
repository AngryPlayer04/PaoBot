import json
import discord
from discord.ext import tasks, commands
from itertools import cycle

from main import change_status

with open("configuration.json", "r") as config: 
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]


intents = discord.Intents.default()
bot = commands.Bot(prefix, intents = intents)

@bot.event
async def on_ready():
    async for guild in bot.fetch_guilds(limit=None):
        guilds = await bot.fetch_guilds(limit=None).flatten()
        change_status.start()
guilds = len(bot.guilds)
@tasks.loop(seconds=14)
async def change_status():
    
    status= cycle(['p.help', 'Pão', 'Bread', f'Estou em {guilds} servidores'])
    await bot.change_presence(activity=discord.Game(next(status)))



    

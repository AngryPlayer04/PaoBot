import discord
from discord.ext import commands, tasks
import json
import os
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

@bot.event
async def on_ready():
	change_status.start()
	print('O {bot.user} está on!!')

@tasks.loop(seconds = 20)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))
	

emojis=None
@bot.command()
async def ping(ctx):
	global emojis
	if not emojis:
		emojis = {e.name:str(e) for e in ctx.bot.emojis}
		msg = "Pong! :paopula: `{0} ms`!".format(int(bot.latency * 1000)).replace(':paopula:',emojis['paopula'])
		await ctx.send(msg)
		

@bot.command(name='clear', help=': this command will clear msgs')
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit=amount)

@bot.event
async def on_message(message):
	if message.content == "Pão":
		await message.channel.send(':bread:')
	if message.content == "pão":
		await message.channel.send(':bread:')
	if message.content == "bread":
		await message.channel.send(':bread:')
	await bot.process_commands(message)
    

bot.run(token)
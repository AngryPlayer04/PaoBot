import discord
import json
from discord.ext import commands

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)


emojis=None
@bot.command()
async def ping(ctx):
	global emojis
	if not emojis:
		emojis = {e.name:str(e) for e in ctx.bot.emojis}
		msg = "Pong! :paopula: `{0} ms`!".format(int(bot.latency * 1000)).replace(':paopula:',emojis['paopula'])
		await ctx.send(msg)

bot.run(token)
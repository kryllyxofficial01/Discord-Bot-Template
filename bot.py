import discord
from discord.ext import commands

# Connects your code to the bot. Treat it like a password.
TOKEN = ""

client = commands.Bot(command_prefix="!") # You can change the prefix if you want.

# When the code successfully connects to the bot, this message will get printed.
@client.event
async def on_ready():
  print("Logged on as {0.user}.".format(client))

# The bot will reply with "pong" when a user types "!ping".
@client.command()
async def ping(ctx):
  await ctx.send("pong")

# Runs the bot.
client.run(TOKEN)

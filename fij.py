import discord
import os

from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(
    command_prefix= ("fij "),
    intents=discord.Intents(messages=True, guilds=True, bans=True, reactions=True),
    case_insensitive=True
)

# Removes default help command
bot.remove_command('help')

@bot.event
async def on_ready():
    print('We have logged in.'.format(bot))

@bot.event
async def on_message(message):
     await bot.process_commands(message)

     # Status
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fortnite | fij help"))

# Loads all cogs.
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

#Pass
bot.run(BOT_TOKEN)
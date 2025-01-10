import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import asyncio


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="fij ",
    intents=intents,
    case_insensitive=True
)

# Removes default help command
bot.remove_command('help')



@bot.event
async def on_ready():
    await load_cogs()

    # Print "Fij has logged in" when Fij is ready
    print('Fij has logged in.'.format(bot))

    # Status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fortnite | fij help"))


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f'cogs.{filename[:-3]}'
            try:
                print(f"Loading {cog_name}")
                await bot.load_extension(cog_name)
                print(f"Loaded {cog_name} successfully.")
            except Exception as e:
                print(f"Couldn't load {cog_name}: {e}")


@bot.event
async def on_disconnect():
    print("Bruh, it disconnect")


@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error: {event}: {args} {kwargs}")



if __name__ == "__main__":
    bot.run('TOKEN')

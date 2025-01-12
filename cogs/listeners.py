import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot, Cog, bot
from discord.ext.commands.core import command

import random


class Listeners(Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):

        # Make sure it doesn't respond to itself.
        # This is probably not a good permenant fix. Please change this later.
        if message.author.bot: return


        #Most of the stuff here you can just delete as 
        #it's mostly just random unneeded shit, but it's
        #too iconic for fij so i'm gonna leave it here

        #Yeah, I just have to use if statements here. 
        #Theres no way to do this with commands sadly 
        #(at least i think)
        if("p") == message.content.lower():
            await message.channel.send("p")

        if("loge") in message.content.lower():
            await message.channel.send("<:loge:1327795593359130644>") #loge emote lol (it's a loge)

        if("gug") in message.content.lower():
            await message.channel.send("<:gug:1327798433347801098>") #gug emote lol (it's a gug)

        if("fij") == message.content.lower():
            responses = ("hi", "hello", "bob?", "erm...", "lock me in", "hi litte jodiac", "tatjanagmeiner.com", "liiiive on beam", "that's me")
            await message.channel.send(random.choice(responses))




# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Listeners(bot))

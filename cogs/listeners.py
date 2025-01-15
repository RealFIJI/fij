import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot, Cog, bot
from discord.ext.commands.core import command

import random
from util import generate

class Listeners(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.generator = generate.Generate()


    @commands.Cog.listener()
    async def on_message(self, message):

        # Make sure it doesn't respond to itself.
        # This is probably not a good permenant fix. Please change this later.
        if message.author.bot: return


        # You may NOT delete this. If you do, you will be banned from GitHub, by me personally.

        # Yeah, I just have to use if statements here.
        # There's no way to do this with commands sadly
        # (at least I think)
        if("p") == message.content.lower():
            await message.channel.send("p")

        if("loge") in message.content.lower():
            await message.channel.send("<:loge:1327795593359130644>") #loge emote lol (it's a loge)

        if("gug") in message.content.lower():
            await message.channel.send("<:gug:1327798433347801098>") #gug emote lol (it's a gug)

        if("fij") == message.content.lower():
            responses = ("hi", "hello", "bob?", "erm...", "lock me in", "hi litte jodiac", "tatjanagmeiner.com", "liiiive on beam", "that's me")
            await message.channel.send(random.choice(responses))


        # Random chance of Fij joining in on the conversation
        if random.randint(1, 100) == 25: # Twenty-five
            personality = "Reply to the message as if you were casually involved in the conversation. E.g., agreeing as if you were listening the whole time, like you have a full understanding of the conversation. Keep it short, simple, and casual."
            response = await self.generator.generate(personality, message)

            await message.channel.send(response)




# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Listeners(bot))

import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands

import random
import asyncpraw


reddit = asyncpraw.Reddit(client_id = "CLIENT_ID",
                     client_secret = "CLIENT_SECRET",
                     username = "USERNAME",
                     password = 'PASSWORD',
                     user_agent = "USER_AGENT")


class Reddit(Cog):

    def __init__(self, bot):
        self.bot = bot

    #Gets a subreddit from reddit
    @commands.command()
    async def subreddit(self, ctx, the_subreddit):
        # Don't ask...
        if the_subreddit.lower() in ["shit", "poop", "poopy"]:
            return await ctx.channel.send("lol no shit related subreddits")


        # A user can access any subreddit, including nsfw ones, so the channel must be marked nsfw.
        if ctx.channel.is_nsfw():
            subreddit = await reddit.subreddit(str(the_subreddit))
            all_subs = []

            # Goes through the top 100 hot posts
            hot = subreddit.hot(limit = 100)

            async for submission in hot:
                all_subs.append(submission)

            # Pick a random submission
            random_sub = random.choice(all_subs)

            # Take submission and store in variable
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title = name)
            em.set_image(url = url)

            # Send embed
            await ctx.channel.send(embed= em)
        else:
            await ctx.channel.send("You cannot use the subreddit command in non-NSFW channels.")

    @subreddit.error
    async def subreddit_error(self, ctx, error):
        await ctx.channel.send(error)



    @app_commands.command(name="subreddit", description="Grabs a random post from a specified subreddit. Can only be used in NSFW channels.")
    @app_commands.describe(the_subreddit="The subreddit to grab the bings from")
    async def slash_subreddit(self, interaction: discord.Interaction, the_subreddit: str):
        # Don't ask...
        if the_subreddit.lower() in ["shit", "poop", "poopy"]:
            return await interaction.response.send_message("lol no shit related subreddits")


        channel = interaction.channel

        # A user can access any subreddit, including nsfw ones, so the channel must be marked nsfw.
        if channel.is_nsfw():
            subreddit = await reddit.subreddit(str(the_subreddit))
            all_subs = []

            # Goes through the top 100 hot posts
            hot = subreddit.hot(limit=100)

            async for submission in hot:
                all_subs.append(submission)

            # Pick a random submission
            random_sub = random.choice(all_subs)

            # Take submission and store in variable
            name = random_sub.title
            url = random_sub.url
            em = discord.Embed(title=name)
            em.set_image(url=url)


            # Send embed
            await interaction.response.send_message(embed=em)
        else:
            await interaction.response.send_message("You cannot use the subreddit command in non-NSFW channels.")



# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Reddit(bot))

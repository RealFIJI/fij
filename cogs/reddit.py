import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command

import random
# import asyncpraw
#
#
# reddit = asyncpraw.Reddit(client_id = "CLIENT_ID",
#                      client_secret = "CLIENT_SECRET",
#                      username = "USERNAME",
#                      password = "PASSWORD",
#                      user_agent = "USER_AGENT")


class Reddit(Cog):

    def __init__(self, bot):
        self.bot = bot
    #
    # #Gets a subreddit from reddit
    # @commands.command()
    # async def subreddit(self, ctx, theSubreddit):
    #     # A user can access any subreddit, including nsfw ones, so the channel must be marked nsfw.
    #     if ctx.channel.is_nsfw():
    #         subreddit = await reddit.subreddit(str(theSubreddit))
    #         all_subs = []
    #
    #         # Goes through the top 200 hot posts
    #         hot = subreddit.hot(limit = 200)
    #
    #         async for submission in hot:
    #             all_subs.append(submission)
    #
    #         # Pick a random submission
    #         random_sub = random.choice(all_subs)
    #
    #         # Take sumbission and store in variable
    #         name = random_sub.title
    #         url = random_sub.url
    #
    #         em = discord.Embed(title = name)
    #
    #         em.set_image(url = url)
    #
    #         # Don't ask...
    #         if(theSubreddit != "shit" and theSubreddit != "poop" and theSubreddit != "poopy"):
    #             # Send embed
    #             await ctx.send(embed= em)
    #         else:
    #             await ctx.send("lol no shit related subreddits")
    #     else:
    #         await ctx.send("You cannot use the subreddit command in non-NSFW channels.")
    #     @subreddit.error
    #     async def subreddit_error(self, ctx, error):
    #         await ctx.channel.send(error)


# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Reddit(bot))

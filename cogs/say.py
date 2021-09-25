import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command

class Say(Cog):

    def __init__(self, bot):
        self.bot = bot

    #Say command (makes Fij say something.)
    @commands.command()
    async def say(self, ctx, *, args):
        await ctx.channel.send(args)
    @say.error
    async def say_error(self, ctx, error):
        await ctx.channel.send(error)



# Setup the cog for the bot
def setup(bot: Bot) -> None:
    bot.add_cog(Say(bot))
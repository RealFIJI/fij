import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands


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



    @app_commands.command(name="say", description="Make Fij say whatever you could possibly imagine, Little Odiebyte.")
    @app_commands.describe(args="What you want Fij to say")
    async def slash_say(self, interaction: discord.Interaction, args: str):
        await interaction.response.send_message(args)



# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Say(bot))

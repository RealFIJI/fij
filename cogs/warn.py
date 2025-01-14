import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands


class Warn(Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Warn command (currently anyone can warn, does nothing)
    @commands.command()
    async def warn(self, ctx, member:discord.User=None, *, reason=None):
        await ctx.channel.send(f"{ctx.author.mention} has warned {member.mention} for: **{reason or 'No reason provided.'}**")

    @warn.error
    async def warn_error(self, ctx, error):
        await ctx.channel.send(error)

    @app_commands.command(name="warn", description="Warns someone for a given reason. Doesn't do much, just sends a message saying you warned the person.")
    @app_commands.describe(member="The user to warn", reason="Warn reason")
    async def slash_warn(self, interaction: discord.Interaction, member: discord.User, reason: str = None):
        await interaction.response.send_message(f"{interaction.user.mention} has warned {member.mention} for: **{reason or 'No reason provided.'}**")




# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Warn(bot))

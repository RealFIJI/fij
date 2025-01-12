import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands


class Mutes(Cog):

    def __init__(self, bot):
        self.bot = bot

    #Mute command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f"{ctx.author} has muted {member} for: {reason or 'No reason provided'}.")

    # Will directly tell you the error if you use the command wrong. Maybe make it more easy to understand errors in the future?
    @mute.error
    async def mute_error(self, ctx, error):
        await ctx.channel.send(error)

    #Unmute command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        # I don't think there should really be an unmute reason. But maybe...
        await ctx.send(f"{ctx.author} has unmuted {member}.")

    @unmute.error
    async def unmute_error(self, ctx, error):
        await ctx.channel.send(error)



    @app_commands.command(name="mute", description="Mutes a Glodie.")
    @app_commands.describe(member="The Glodie to mute", reason="The reasonbob")
    async def slash_mute(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if not interaction.user.guild_permissions.manage_messages:
            return await interaction.response.send_message("You don't have the perms to mute people, Little Glodie.")

        role = discord.utils.get(interaction.guild.roles, name="Muted")
        await member.add_roles(role)
        await interaction.response.send_message(f"{interaction.user} has muted {member} for {reason or 'No reason provided'}.")

    @app_commands.command(name="unmute", description="Unmutes a Glodie.")
    @app_commands.describe(member="The Glodie to unmute", reason="The reasonbob")
    async def slash_unmute(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if not interaction.user.guild_permissions.manage_messages:
            return await interaction.response.send_message("You don't have the perms to unmute people, Little Glodie.")

        role = discord.utils.get(interaction.guild.roles, name="Muted")
        await member.remove_roles(role)
        await interaction.response.send_message(f"{interaction.user} has unmuted {member} for {reason or 'No reason provided'}.")



# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Mutes(bot))

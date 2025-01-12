import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands


class Bans(Cog):

    def __init__(self, bot):
        self.bot = bot

    # The ban command. User must have ban_members permission to use it.
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.User=None, reason=None):
        banner = ctx.author
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Sorry, but you can't ban yourself " + banner)
            return

        message = f"You have been banned from {ctx.guild.name} for {reason or 'no reason whatsoever. Rude...'}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} has been banned by " + banner.mention + " for " + reason)

    # Will directly tell you the error if you use the command wrong. Maybe make it more easy to understand errors in the future?
    @ban.error
    async def ban_error(self, ctx, error):
        await ctx.channel.send(error)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member:discord.User=None, reason=None):
        unbanner = ctx.author
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Sorry, but you can't unban yourself " + unbanner)
            return
        
        await ctx.guild.unban(member, reason=reason)
        await ctx.channel.send(f"{member} has been unbanned by {unbanner.mention} for {reason or 'no reason whatsoever. Beam...'}")

        # Depending on the user's settings this may or may not cause an error. should probably fix in future verions lol
        message = f"You have been unbanned from {ctx.guild.name} for {reason}"
        await member.send(message)

    # Will directly tell you the error if you use the command wrong. Maybe make it more easy to understand errors in the future?
    @unban.error
    async def unban_error(self, ctx, error):
        await ctx.channel.send(error)



    @app_commands.command(name="ban", description="Bans an Odie from the server.")
    @app_commands.describe(member="The Odie to ban", reason="The reason")
    async def slash_ban(self, interaction: discord.Interaction, member: discord.User, reason: str = None):
        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message("You don't have the perms to ban people, Little Odie.")

        await member.send(f"You've probably been banned from {interaction.guild.name} for {reason or 'no reason whatsoever. Rude...'}")


        banner = interaction.user
        try:
            # Everything's good, lock 'em in.
            await interaction.guild.ban(member, reason=reason)
            await interaction.response.send_message(f"You have been banned from {interaction.guild.name} for {reason or 'no reason whatsoever. Beam...'}")
        except Exception as e:
            await interaction.response.send_message(e)

    @app_commands.command(name="unban", description="Unbans an Odie from the server.")
    @app_commands.describe(member="The Odie to unban", reason="The reason")
    async def slash_unban(self, interaction: discord.Interaction, member: discord.User, reason: str = None):
        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message("You don't have the perms to unban people, Little Odie.")


        await member.send(f"You've probably been unbanned from {interaction.guild.name} for {reason or 'no reason whatsoever. Beam...'}")

        unbanner = interaction.user
        try:
            # Everything's good, lock 'em in.
            await interaction.guild.unban(member, reason=reason)
            await interaction.response.send_message(f"{member} has been unbanned by {unbanner.mention} for {reason or 'no reason whatsoever. Beam...'}")
        except Exception as e:
            await interaction.response.send_message(e)




# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Bans(bot))

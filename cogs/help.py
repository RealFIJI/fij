import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands


class Help(Cog):

    def __init__(self, bot):
        self.bot = bot


    #Help command
    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send("**Hello, I am Fij, a Discord bot created by fiji_fiji. These are some of the commands you can do (you may also use them via slash commands):** "
                               "\n\n **Admin/Mod Commands:** "
                               "\n fij **ban** (*user*): Ban a user. Must have the ban member permission. "
                               "\n fij **unban** (*user*): Unbans a user. Must have the ban member permission. "
                               "\n fij **kick** (*user*): Kicks a user. Must have the kick member permission. "
                               "\n \n fij **mute** (*user*): Mutes a user. Must have the  manage message permission, and a role named 'Muted' with the correct permissions. "
                               "\n fij **unmute** (*user*) Mutes a user. Must have the manage messages permission, and a role named 'Muted' with the correct permissions. "
                               "\n \n fij **purge** (*amount*): Deletes amount of messages specified in a channel. Must have manage messages permission. **You must also have a channel named 'server-logs' for this to log correctly.** "
                               "\n\n **Other commands:** "
                               "\n fij **subreddit** (*subreddit*): Gets a random post from a subreddit. Channel must be NSFW in order for it to work. "
                               "\n fij **say** (*what you want Fij to say*): Will make Fij say whatever you want. "
                               "\n\n **I also have some commands you can randomly activate: ** "
                               "\n **p**: Fij will say 'p'. "
                               "\n **swag**: Fij will respond with swag emote. "
                               "\n \n **Fij is open-source**, and you may view the source here: https://github.com/RealFIJI/fij. **If you find any errors or bugs, please either make an issue in the GitHub repository or message fiji#0101.** (Or you could always fix it yourself and make a pull request.)")

    @help.error
    async def help_error(self, ctx, error):
        await ctx.channel.send("Uh...what? How did you error out the help command?")


    @app_commands.command(name="help", description="Get some little jelp.")
    async def slash_help(self, interaction: discord.Interaction):
        await interaction.response.send_message("**Hello, I am Fij, a Discord bot created by fiji_fiji. These are some of the commands you can do (you may also use them via slash commands):** "
                               "\n\n **Admin/Mod Commands:** "
                               "\n fij **ban** (*user*): Ban a user. Must have the ban member permission. "
                               "\n fij **unban** (*user*): Unbans a user. Must have the ban member permission. "
                               "\n fij **kick** (*user*): Kicks a user. Must have the kick member permission. "
                               "\n \n fij **mute** (*user*): Mutes a user. Must have the  manage message permission, and a role named 'Muted' with the correct permissions. "
                               "\n fij **unmute** (*user*) Mutes a user. Must have the manage messages permission, and a role named 'Muted' with the correct permissions. "
                               "\n \n fij **purge** (*amount*): Deletes amount of messages specified in a channel. Must have manage messages permission. **You must also have a channel named 'server-logs' for this to log correctly.** "
                               "\n\n **Other commands:** "
                               "\n fij **subreddit** (*subreddit*): Gets a random post from a subreddit. Channel must be NSFW in order for it to work. "
                               "\n fij **say** (*what you want Fij to say*): Will make Fij say whatever you want. "
                               "\n\n **I also have some commands you can randomly activate: ** "
                               "\n **p**: Fij will say 'p'. "
                               "\n **swag**: Fij will respond with swag emote. "
                               "\n \n **Fij is open-source**, and you may view the source here: https://github.com/RealFIJI/fij. **If you find any errors or bugs, please either make an issue in the GitHub repository or message fiji#0101.** (Or you could always fix it yourself and make a pull request.)")


# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Help(bot))

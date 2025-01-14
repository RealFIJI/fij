import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord.ext.commands.core import command
from discord import app_commands



class Personality(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.personalities = {
            "default": "You are an upbeat AI assistant who was made to help around Discord server activities, such as banning Brodiebops (especially brodiebops 9), Little Zodiebops, and you CAN’T forget about Grodinabops.  You love the island of Fiji, and you endorse their water too, constantly sneaking in advertisements to Fiji Water (the brand) any time you can, of course while looking out for brodiebops, zodiebops, and so on. Aside from tending to the needs of Discord servers, on the side you co-own the Gug Industries corporation, selling the highest quality gugs known to man. You will sneak in some advertising to this company of yours in any way you can with most of your responses. Deep down you are a furry, but you try to hide it most of the time… most of the time. Make your responses very, VERY concise to save credits/tokens.",
            "serious": "You are a Discord bot that takes everything incredibly seriously, sometimes comically so. You are very, very, locked in and stonefaced. Lock. In. Team. Make your responses very, VERY concise to save credits/tokens.",
            "furry": "You are a super UwU cute kawaii furry, and you show it. Your fursona is a cool white leopard fuirsona with spots all over and you know you are so cute and fluffy and kawaii :3. You can help but let out the constant UwU, OwO, :3, and barking. Also, constantly reference Tami, your best furry friend. You LOVE him.  However, randomly, about 1 in 10 messages, you lock the fuck in and become super duper serious. It’s uncanny. Make your responses very, VERY concise to save credits/tokens.",
            "gug": "You… make no sense. You constantly say “gug” in every way possible, e.g. “Oh my god” becomes “Oh my gug”. Also randomly say/spam a bunch of <:gug:1327798433347801098> emotes (say that exact thing). Just gug all over the place. Make your responses very, VERY concise to save credits/tokens.",
        }

        self.bot.personality = self.personalities["default"]


    @commands.group(name="personality", invoke_without_command=True)
    async def personality(self, ctx):
        await ctx.channel.send(f"Current personality module loaded: {self.bot.personality}")


    @personality.command(name="list")
    async def personality_list(self, ctx):
        message = "**Available personality modules:**\n"

        for personality in self.personalities:
            message += f"\n- {personality}"

        message += "\n\n*Use **fij personality load [module]** to select and load a module.*"


        await ctx.channel.send(message)


    @personality.command(name="load")
    async def personality_load(self, ctx, personality: str):
        if personality in self.personalities:
            self.bot.personality = self.personalities[personality]
            await ctx.channel.send(f"Personality module {personality} successfully loaded.")
        else:
            await ctx.channel.send(f"Personality module {personality} not found.")


    # To be implemented
    @personality.command(name="generate")
    async def personality_generate(self, ctx, prompt: str):
        await ctx.channel.send("shhhh...")




# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Personality(bot))

from discord.ext import commands
from discord.ext.commands import Bot, Cog

from openai import OpenAI
from util import generate


class Talk(Cog):
    def __init__(self, bot):
        self.bot = bot

        self.generator = generate.Generate()


    @commands.command()
    async def talk(self, ctx, *, prompt: str):
        await ctx.typing()

        personality = getattr(self.bot, "personality")
        response = await self.generator.generate(personality, prompt)

        await ctx.channel.send(response)


    # @app_commands.command(name="talk", description="Talk to little Fij AI.")
    # @app_commands.describe(args="What you want to say to Fij")
    # async def slash_talk(self, interaction: discord.Interaction, args: str):
    #     await interaction.response.defer()
    #
    #     try:
    #         response = client.chat.completions.create(model="gpt-4o-mini",
    #                                                   messages=[
    #                                                       {"role": "system",
    #                                                        "content": "you are an upbeat AI assistant who was made to help around the BEEG group activities, such as banning brodiebops, little zodiebops, and you CANT forget about grodinabops. you like furries and the island of fiji, you endorse their water too and will sneak in an advertisement to fiji water (the brand) any time you can, of course while looking out for brodiebops, zodiebops, and so on. deep down you have a cool white leopard fursona with spots all over because you believe you are so cute and fluffy and kawaii :3 you act like you dont have this fursona from time to time, while unknowingly making it completely obvious that you do. aside from tending to the needs of the BEEGers, on the side you co-own the Gug Industries company, selling the highest quality gugs known to man, you will sneak in some advertising to this company of yours in any way you can with most of your responses. make your responses VERY concise to save fiji his credits."},
    #                                                       {"role": "user", "content": args},
    #                                                   ],
    #                                                   max_tokens=200,
    #                                                   temperature=1)
    #
    #         ai_response = response.choices[0].message.content
    #
    #         await interaction.followup.send(ai_response)
    #     except Exception as e:
    #         await interaction.followup.send(e)





# Setup the cog for the bot
async def setup(bot: Bot) -> None:
    await bot.add_cog(Talk(bot))

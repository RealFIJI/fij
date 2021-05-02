import discord
import random
import asyncio
import discord.ext
import asyncpraw
import time

from discord.ext import commands
from discord.utils import get

reddit = asyncpraw.Reddit(client_id = "YOURCLIENTIDHERE",
                     client_secret = "YOURCLIENTSECRETHERE",
                     username = "YOURUSERNAMEHERE",
                     password = "YOURPASSWORDHERE",
                     user_agent = "YOURUSERAGENTHERE")

client = commands.Bot (command_prefix = 'fij ')
client.remove_command('help')



@client.event
async def on_ready():
    print('We have logged in.'.format(client))

@client.event
async def on_message(message):
     await client.process_commands(message)

     if message.author == client.user:
        return

     #Most of the stuff here you can just delete as 
     #it's mostly just random unneeded shit, but it's
     #too iconic for fij so i'm gonna leave it here

     #Yeah, I just have to use if statements here. 
     #Theres no way to do this with commands sadly 
     #(at least i think)
     if("p") == message.content:
         await message.channel.send("p")

     if("swag") == message.content:
         await message.channel.send("<:swag:838324542967119883>") #swag emote lol (it's a cat)    
    
     if("channel check") == message.content:
         if message.channel.is_nsfw():
             await message.channel.send("true")
         else:
             await message.channel.send("false")

#Classes for mute and warn
class Mutee(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        if argument.guild_permissions.manage_messages:
            raise commands.BadArgument("You cannot mute another staff member.")
        else:
            return argument

class Warnn(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        return argument

#COMMANDS

#Ban command
@client.command()
@commands.has_permissions(ban_members=True)
async def ban (ctx, member:discord.User=None, reason =None):
    banner = ctx.author
    if member == None or member == ctx.message.author:
        await ctx.channel.send("lol you can't ban yourself stupid idot stupid ahhahahhaahah")
        return
    if reason == None:
        reason = "for no reason"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned by " + banner.mention + " for " + reason + "! lol imagine")


#Kick command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick (ctx, member:discord.User=None, reason =None):
    banner = ctx.author
    if member == None or member == ctx.message.author:
        await ctx.channel.send("lol you can't ban yourself stupid idot stupid ahhahahhaahah")
        return
    if reason == None:
        reason = "for no reason."
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    await ctx.channel.send(f"{member} has been kicked by " + banner.mention + " for " + reason + "! lol imagine")


#Purge command
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=0):
    logChannel = client.get_channel(745366252922470418)
    channelUsedIn = ctx.message.channel
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await logChannel.send(f'{amount} messages have been purged by {ctx.message.author.mention} in {channelUsedIn}')

#Mute command
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user: Mutee, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    try:
        await user.add_roles(role)
        await ctx.send(f"{ctx.author} has muted {user} for: {reason or 'No reason provided.'}")
    except discord.Forbidden:
        return await ctx.send("Unable to mute user. Maybe you don't have the correct roles, "
                              "or you're trying to mute somebody higher than me.")

#Unmute command
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user: Mutee):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    try:
        await user.remove_roles(role)
        await ctx.send(f"{ctx.author} has unmuted {user}.")
    except discord.Forbidden:
        return await ctx.send("Unable to mute user. Maybe you don't have the correct roles, "
                              "or you're trying to mute somebody higher than me.")

#Warn command (currently anyone can warn, does nothing)
@client.command()
async def warn(ctx, user: Warnn, *, reason=None):
    try:
        await ctx.send(f"{ctx.author} has warned {user} for: **{reason or 'No reason provided.'}**")
    except discord.Forbidden:
        return await ctx.send("Unable to warn user.")

#Say command (makes fij say something.)
@client.command()
async def say(ctx, *, args):
    await ctx.send(args)

#Gets a subreddit from reddit
@client.command()
async def subreddit(ctx, theSubreddit):
    if ctx.channel.is_nsfw():
         subreddit = await reddit.subreddit(str(theSubreddit))
         all_subs = []

         hot = subreddit.hot(limit = 200)

         async for submission in hot:
            all_subs.append(submission)
       
         random_sub = random.choice(all_subs)

         name = random_sub.title
         url = random_sub.url

         em = discord.Embed(title = name)

         em.set_image(url = url)
         
         #Don't ask...
         if(theSubreddit != "shit" and theSubreddit != "poop" and theSubreddit != "poopy"):
             await ctx.send(embed= em)
         else:
             await ctx.send("lol no shit related subreddits")
    else:
       await ctx.send("You cannot use the subreddit command in non NSFW channels.")



#ERRORS
@subreddit.error
async def subreddit_error(ctx):
    await ctx.send("Invalid subreddit.")
@purge.error
async def purge_error(ctx, error):
    commander = ctx.author
    await ctx.send("You either must be an admin to purge messages, or you went above the purge limit (the limit is 99) " + commander.mention)
@mute.error
async def mute_error(ctx):
    await ctx.send("Unable to mute user. Maybe you don't have the correct roles, "
                              "or you're trying to mute somebody higher than me.")
@kick.error
async def kick_error(ctx, error):
   commander = ctx.author
   await ctx.send("You either don't have the correct permissions to kick someone, or you entered an invalid user.  " + commander.mention)
@ban.error
async def ban_error(ctx, error):
   commander = ctx.author
   await ctx.send("You either don't have the correct permissions to ban someone, or you entered an invalid user. " + commander.mention)



#Pass
client.run('YOURCLIENTSECRETHERE')
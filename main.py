import discord
from discord.ext import commands
import asyncio
from discord.utils import get
from discord.ext.commands import Bot
from discord import User
import time

TOKEN = 'ODc3MzEwNTgxMDE3ODIxMjI1.YRwxJg.YguoUXUYdmBbj3TWWzDjH9Zyvlg'

client = commands.Bot(command_prefix = "#")




@client.event
async def on_ready():
    print("Logges in as "+ client.user.name+"\n")

@client.command()
async def info(ctx, *args):

    if args[0] == "lonely" :
        await ctx.send("Use #lonely if you need company")
    elif args[0] == "do_bezos":
        await ctx.send("Use #do_bezos if you want the bot to repeat you")
    else:
        await ctx.send("-HELP-MENU-\n#lonely if you feel lonely \n#do_bezos to get bezost\nUse #info <command> for more information")

@client.event
async def on_message_delete(message):
    channel = client.get_channel(803028642283782176)
    Inhalt = message.content
    Autor = message.author
    x = Inhalt + "\n--" + str(Autor)
    await channel.send(x)



@client.command()
async def lonely(ctx):

    await ctx.send(f"@here unterhaltet <@{ctx.author.id}> ein bisschen ")

@client.command()
async def do_bezos(ctx, *args):
    phrase = ""
    for i in args:
        phrase += i
        phrase += " "
    await ctx.send(phrase)






@client.command(name = "truck")
async def truck(ctx, user: discord.Member):
    channel = ctx.channel
    await ctx.send(f"{user.mention} achtung ein Truck!")
    def check(m):
        return m.content == '#ninja_move' and m.channel == channel and m.author == user
    try:
        msg = await client.wait_for('message', check=check, timeout = 10.0)
    except asyncio.TimeoutError:
        await channel.send(f"{user.mention} wird vom Truck überrolt!")
    else:
        await channel.send(f"{user.mention} macht eine coole Ninja-Rolle nach rechts und weicht aus!")





client.run(TOKEN)
#Venzel du hs

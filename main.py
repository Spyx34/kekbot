import custom
import random as r
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
    try:
        if args[0] == "lonely" :
            await ctx.send("Use #lonely if you need company")
        elif args[0] == "do_bezos":
            await ctx.send("Use #do_bezos if you want the bot to repeat you")
        elif args[0] == "truck":
            await ctx.send("Use #truck <user> to warn your friend of an incoming truck")
        elif args[0] == "ssp":
            await ctx.send("Use #ssp <schere/stein/papier> to play Rock Paper Scissors")
    except:
        await ctx.send('''.
                          -------HELP-MENU-------
                          #lonely if you feel lonely
                          #do_bezos to get bezost
                          #truck summon a truck
                          #ssp play rock paper scissors
                          -------------------------------
                          Use #info <command> for more information''')

@client.event
async def on_message_delete(message):
    channel = client.get_channel(803036842646700072)
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


@client.command()
async def ssp(ctx,*args):
    input = args[0]
    ssp_zahl = r.randint(1,3)
    if args[0] == "hund":
        await ctx.send("Ich setzte arschbohrer bei deinem Hund ein! \nGet shitted du Bot!")
    elif ssp_zahl == 1:
        await ctx.send("Schere!")
    elif ssp_zahl == 2:
        await ctx.send("Stein!")
    elif ssp_zahl == 3:
        await ctx.send("Papier!")

    if ssp_zahl == 1 and input == 'schere' or ssp_zahl == 2 and input == 'stein' or ssp_zahl == 3 and input == "papier":
        await ctx.send("Unentschieden!")
    elif ssp_zahl == 1 and input == 'stein' or ssp_zahl == 2 and input == "papier" or ssp_zahl == 3 and input == 'schere':
        await ctx.send("Verdammt! Du gewinnst.")
    elif ssp == 1 and input == "papier" or ssp_zahl == 2 and input == "schere" or ssp_zahl == 3 and input == "stein":
        await ctx.send("Get shitted du bot!")
    elif args[0]:
        print("that Motherfucker used hund")



@client.command()
async def truck(ctx, user: discord.Member):
    channel = ctx.channel
    await ctx.send(f"{user.mention} achtung ein Truck!\nWeiche mit ninja_move aus!")
    def check(m):
        return m.content == 'ninja_move' and m.channel == channel and m.author == user
    try:
        msg = await client.wait_for('message', check=check, timeout = 15.0)
    except asyncio.TimeoutError:
        await channel.send(f"{user.mention} wird vom Truck überrolt!")
    else:
        zuf = r.randint(1,4)
        if zuf == 1:
            await channel.send(f"{user.mention} macht eine coole Ninja-Rolle nach rechts und weicht aus!")
        elif zuf == 2:
            await channel.send(f"{user.mention} macht eine coole Ninja-Rolle nach links und weicht aus!")
        elif zuf == 3:
            await channel.send(f"{user.mention} legt sich flach auf den Boden und lässt den Truck über sich brausen!")
        else:
            await channel.send(f"{user.mention} springt über den Truck und überlebt!")



#@client.command()
#async def kill(ctx, user: discord.Member):
#    await ctx.send(f'{user.mention} stirbt')
#
#    global todesliste
#    todesliste = {}
#    try:
#        tempo = todesliste[f'{user}']
#        todesliste[f'{user}'] = tempo + 1
#    except:
#        temporaer = {f'{user}' : 1}
#        todesliste = todesliste | temporaer
#
#@client.command()
#async def rip(ctx, user: discord.Member):
#    #print(todesliste[f'{user}'])
#    await ctx.send(f'{user} starb ' + str(todesliste[f'{user}']) + 'mal')







client.run(TOKEN)

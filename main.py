import custom
import random as r
import discord
from discord.ext import commands
import asyncio
import giphy_client
from giphy_client.rest import ApiException
from discord.utils import get
import time

intents = discord.Intents.default()
intents.members = True

TOKEN = 'ODc3MzEwNTgxMDE3ODIxMjI1.YRwxJg.YguoUXUYdmBbj3TWWzDjH9Zyvlg'

client = commands.Bot(command_prefix = "#", intents = intents)




@client.event
async def on_ready():
    print("Logges in as "+ client.user.name+"\n")

@client.event
async def on_member_join(member):
    server_name = client.get_guild(802985801100165200)
    await member.send(f'Willkommen auf {server_name}!')
    print(1)


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
        elif args[0] == "clear" or args[0] == "do_woman":
            await ctx.send("Use #clear <amount> to clear a certain amount of messages")
        elif args[0] == "gif":
            await ctx.send("Use #gif <gif_name> to search and send a gif \nAliases: searchgif")
        elif args[0] == "gif":
            await ctx.send("Use #rickroll <user> to rickroll someone \nAliases: rick , rickastley")
    except:
        await ctx.send('''.
                          -------HELP-MENU-------
                          #lonely if you feel lonely
                          #do_bezos to get bezost
                          #truck summon a truck
                          #ssp play rock paper scissors
                          #gif for a gif
                          #clear to clear old messages
                          #rickroll to rickroll some1
                          -------------------------------
                          Use #info <command> for more information''')

@client.event
async def on_message_delete(message):
    channel = client.get_channel(803036842646700072)
    Inhalt = message.content
    Autor = message.author
    x = Inhalt + "\n--" + str(Autor)
    await channel.send(x)

@client.command(aliases=['do_woman'])
async def clear(ctx, Anzahl = 15):
    await ctx.channel.purge(limit=int(Anzahl) + 1)


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

@client.command(aliases=[ 'searchgif'])
async def gif(ctx,*,Suche="dog"):
    api_key = 'GSGMjDZvTnm9Ks5ZBBmKnk2hXTOOVHPq'
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.gifs_search_get(api_key, Suche, limit = 5) #limit gibt limit für return der anzahl an gifs an
        gif_liste = list(api_responce.data)
        gif = r.choice(gif_liste)
        await ctx.channel.send(gif.embed_url)
    except ApiException as e:
        print('fehlversuch gif aufzurufen mit api--> check api key')

@client.command(aliases=[ 'goodnight'])
async def gutenacht(ctx,*,Suche="good night"):
    api_key = 'GSGMjDZvTnm9Ks5ZBBmKnk2hXTOOVHPq'
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.gifs_search_get(api_key, Suche, limit = 5) #limit gibt limit für return der anzahl an gifs an
        gif_liste = list(api_responce.data)
        gif = r.choice(gif_liste)
        await ctx.channel.send(gif.embed_url)
    except ApiException as e:
        print('fehlversuch gif aufzurufen mit api--> check api key')

@client.command(aliases=[ 'rickastley', 'rick'])
async def rickroll(ctx,*,user : discord.Member,Suche="rickroll"):
    api_key = 'GSGMjDZvTnm9Ks5ZBBmKnk2hXTOOVHPq'
    api_instance = giphy_client.DefaultApi()

    try:
        api_responce = api_instance.gifs_search_get(api_key, Suche, limit = 1) #limit gibt limit für return der anzahl an gifs an
        gif_liste = list(api_responce.data)
        gif = r.choice(gif_liste)
        await ctx.channel.send(gif.embed_url)
    except ApiException as e:
        print('fehlversuch gif aufzurufen mit api--> check api key')
    await ctx.send(f'{user.mention} ,du wurdest gerade von {ctx.author} gerickrolled!')

@client.command()
async def kill(ctx, user: discord.Member):
    await ctx.send(f'{user.mention} stirbt')


client.run(TOKEN)

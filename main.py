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

TOKEN = 'Your Token'

client = commands.Bot(command_prefix = "#", intents = intents)




@client.event
async def on_ready():
    print("Logges in as "+ client.user.name+"\n")

@client.event
async def on_member_join(member):
    server_name = client.get_guild(802985801100165200)
    await member.send(f'Willkommen auf {server_name}!')
    print(1)
    rolle = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(rolle)

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
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member,*,reason=None):
    await member.send(f'You were kicked from the Schnitzel Server {reason}')
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member} {reason}')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,*,reason=None):
    await member.send(f'You were banned from the Schnitzel Server {reason}')
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member} {reason}')

@client.command(aliases=['pardon'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    print(banned_users)
    member_name, member_tag = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        reason = ban_entry.reason

        if (user.name,user.discriminator) == (member_name,member_tag):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}\nHe was banned for: {reason}')

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx,member: discord.Member):
    seine_rollen = member.roles
    Mitglied = []
    f = open('txt_files/Muted.txt', 'a')
    f.write(f'{member.display_name}')

    for i in seine_rollen:
        rolle = str(i)  
        if rolle != '@everyone':

            Mitglied.append(rolle)
            f.write(f'/{rolle}')
        else:
            pass
    f.write('/\n')




    for i in Mitglied:
        rolle = discord.utils.get(member.guild.roles, name=f'{i}')
        await member.remove_roles(rolle)

    rolle = discord.utils.get(member.guild.roles, name='Muted')
    await member.add_roles(rolle)
    f.close()
    await ctx.send(f'Muted {member.display_name}')

@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member: discord.Member):
    rolle = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(rolle)

    Zeilen = 0
    name = str(member.display_name)
    with open('txt_files/Muted.txt', 'r+') as read_obj:
        for line in read_obj:
            Zeilen += 1

            if name in line:

                f = open('txt_files/Muted.txt', 'r')
                x = f.readlines()
                zeile = Zeilen - 1
                f.close()
                output_1 = x[zeile]
                output_2 = output_1.split('/')

                output_2.pop(0)
                output_2.pop(-1)
                with open("txt_files/Muted.txt", "r") as f:
                    lines = f.readlines()
                with open("txt_files/Muted.txt", "w") as f:
                    for line in lines:
                        print(line)
                        if line != output_1:
                            f.write(line)
                        else:
                            print('gesuchte line gefunden')
                            pass

    try:

        for role in output_2:
            rolle = str(role)
            richtige_rolle = discord.utils.get(member.guild.roles, name=f'{rolle}')
            await member.add_roles(richtige_rolle)
            await ctx.send(f'Rolle {rolle} zurück gegeben')
    except:
        await ctx.send('This user isnt muted')


    read_obj.close()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Da fehlt noch irgendwas')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Diesen command gibt es noch nicht')
        time.sleep(2)
        await ctx.send('Du Knecht', delete_after = 1)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Nicht so schnell du Knecht')
    elif isinstance(error, commands.NSFWChannelRequired):
        await ctx.send('Lass das lieber in einem nsfw channel machen :wink:')
    elif isinstance(error, commands.UserNotFound):
        await ctx.send('User konnte nicht gefunden werden')
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send('Dazu hast du keine Berechtigung :(')
    else:
        await ctx.send('Irgendwas ist da schief gelaufen')


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
    api_key = 'YOUR_GIPHY_API_KEY'
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
    api_key = 'YOUR_GIPHY_API_KEY'
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
    api_key = 'YOUR_GIPHY_API_KEY'
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
   
@client.command(aliases=['profilbild','pb','avatar'])
async def pfp(ctx,member: discord.Member):
    await ctx.send(member.avatar_url)


#Counter:

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.channel.id == counter_channel_id:
        counterliste = open('counterliste.txt', 'r')
        nummer = counterliste.read()
        Nachricht = message.content
        counterliste.close()
        Autorliste = open('Autorliste.txt','r')
        ex_autor = Autorliste.read()
        Autor = message.author
        Autorliste.close()

        try:
            integer_1 = int(nummer)
            message_int = int(Nachricht)
            print(Autor)
            print(ex_autor)
            if  str(ex_autor) == str(Autor):
                await message.delete()

            else:

                if integer_1 + 1 == message_int:
                    richtig = open('counterliste.txt', 'w')
                    richtig.truncate(0)
                    richtig.write(f'{message_int}')
                    counterliste.close()
                    Autorliste = open('Autorliste.txt','w')
                    Autorliste.truncate(0)
                    Autorliste.write(f'{Autor}')
                    Autorliste.close()
                else:
                    await message.delete

        except:
            await message.delete()

#@client.event
#async def on_message_delete(message):
#    if message.channel.id == 804278089592602635 and message.author.id != user.id:
#        channel = client.get_channel(804278089592602635)
#        inhalt = message.content
#        recount = open('counterliste.txt','r+')
#        zahl = recount.read()
#        zahl = int(zahl)
#        recount.truncate(0)
#        zahl_1 = zahl - 1
#        recount.write(f'{zahl_1}')
#        recount.close()
#        await channel.send(zahl_1)
#    else:
#       pass

    
#Tic Tac Toe:
player1 = ''
player2 = ''
turn = ''
gameOver = True

board = []

umzugewinnen = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

@client.command(aliases=['ttt'])
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [':white_large_square:',':white_large_square:',':white_large_square:',
                 ':white_large_square:',':white_large_square:',':white_large_square:',
                 ':white_large_square:',':white_large_square:',':white_large_square:']
        turn = ''
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2

        line = ''

        #board senden
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += ' ' +board[x]
                await ctx.send(line)
                line = ''
            else:
                line += ' ' + board[x]

        #Beginner

        num = r.randint(1,2)
        if num == 1:
            turn = player1
            await ctx.send(f'<@{str(player1.id)}>, du bist dran')

        elif num == 2:
            turn = player2
            await ctx.send(f'<@{str(player2.id)}>, du bist dran')

        else:
            await ctx.send('Es spielt gerade jemand, versuch es danach nochmal')

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    print(pos)
    if pos > 10 :
        print('nein')
        await ctx.send('Du musst eine Zahl von  1-9  und ein freies feld wählen')
        pass
    elif pos < 0 :
        print('nein')
        await ctx.send('Du musst eine Zahl von  1-9  und ein freies feld wählen')
        pass
    elif board[pos - 1] != ':white_large_square:':
        print('nein')
        await ctx.send('Du musst eine Zahl von  1-9  und ein freies feld wählen')
        pass

    if not gameOver:
        mark = ''
        if turn == ctx.author:
            print('kommt durch author')
            if turn == player1:
                mark = ':regional_indicator_x:'
            elif turn == player2:
                mark = ':o2:'
            if pos < 10 and pos > 0 and board[pos - 1] == ':white_large_square:':
                board[pos - 1] = mark
                count += 1
                print('ja')
                line = ''
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += ' ' + board[x]
                        await ctx.send(line)
                        line = ''
                    else:
                        line += ' ' + board[x]
                check_gewinner(umzugewinnen,mark)
                if gameOver:
                    await ctx.send(f'{mark} gewinnt!')
                elif count >= 9:
                    await ctx.send('Unentschieden! Niemand gewinnt')

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1


        else:
            await ctx.send('Du bist nicht dran')
    else:
        await ctx.send('Du hast grad kein Spiel am laufen')

def check_gewinner(umzugewinnen, mark):
    global gameOver
    for condition in umzugewinnen:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error,commands.BadArgument):
        await ctx.send('Markier einen gültigen Spieler')

@client.command()
async def now_playing_ttt(ctx):
    if not gameOver:
        await ctx.send(f'Es spielen gerade: {player1} und {player2}')
    else:
        await ctx.send('Es spielt gerade niemand')

@client.command()
async def reset_ttt(ctx):
    global gameOver
    if not gameOver:
        global board
        global count

        gameOver = True
        count = 0
        board = [':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:']
        await ctx.send('Spielstand zurück gesetzt')
    else:
        await ctx.send('Es spielt gerade niemand')
    
    
#Errors:


@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Da fehlt noch irgendwas')
    elif isinstance(error,commands.MissingPermissions):
        await ctx.channel.purge(limit=1)
        await ctx.send('Dazu hast du keine Berechtigung', delete_after=15)



client.run(TOKEN)

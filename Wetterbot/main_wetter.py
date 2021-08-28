import json
import discord
import requests
from weather import *

TOKEN = 'your token'
weather_key = 'your token'
client = discord.Client()
command_prefix = 'w.'

@client.event
async def on_ready():
    print("Logges in as "+ client.user.name+"\n")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='w.[standort]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        city = message.content.replace(command_prefix,'')
        if len(city) >= 1:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric&lang=de'

            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await message.channel.send(embed=wetter_antwort(data, city))
            except KeyError:
                await message.channel.send(embed=on_error_msg(city))




client.run(TOKEN)

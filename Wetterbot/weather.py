import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperatur',
    'feels_like' : 'Gefühlte',
    'temp_min' : ' Minimale Temperatur',
    'temp_max' : 'Maximale Temperatur'
}



def parse_data(data):
    data = data['main']

    del data['humidity']
    del data['pressure']

    return data


def  wetter_antwort(data,city):
    city = city.title()
    message = discord.Embed(title=f'{city} Wetter', description=f'Hier die Wetter Daten für {city}.',color = color)
    for key in key_features:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline = False
        )

    return message

def on_error_msg(city):
    city = city.title()
    return discord.Embed(
        title='Error',
        description=f'Es ist ein Fehler beim Suchen der Wetterinformationenn für {city} aufgetreten.',
        color=color
    )

import requests
import telebot
from exchange_rate import lari_final, usd_final

## create a token for telegram
token_weather = '34a25b9ab2c41a71f4660e894d1be85b'
Bot = telebot.TeleBot("671182374:AAE1lGCsWPUAwLR33kItO4urJY1JXZeHTe8")

@Bot.message_handler(commands=["start"])
def start(m, result=False):
    Bot.send_message(m.chat.id, 'Здарова')

def get_weather(location):
    API_KEY = '34a25b9ab2c41a71f4660e894d1be85b'
    API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    main = data['weather'][0]['main']
    description = data['weather'][0]['description']
    city = data['name']
    temp = data['main']['temp']
    temp_feels = data['main']['feels_like']
    return f'Город {city}, Температура {temp}, Ощущается как {temp_feels}, Осадки {description}'



## add new button to bot 'weather'
@Bot.message_handler(commands=['weather'])
def weather(m):
    # Get the weather data
    weather_data = get_weather('Batumi, Georgia')

    # Send the weather data to the user
    Bot.send_message(m.chat.id, weather_data)



@Bot.message_handler(commands=['exchange'])
def exchange(m):
    exchange_general = lari_final + usd_final
    Bot.send_message(m.chat.id, exchange_general)



Bot.polling(none_stop=True, interval=0)
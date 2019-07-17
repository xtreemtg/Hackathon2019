import requests
import json

def get_weather(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?'
                            f'q={city}&units=metric&APPID=fb0e6229d78973814f4cf193f2900387')
    return json.loads(response.text)



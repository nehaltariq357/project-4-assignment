import requests
from pprint import pprint

API_KEY = "79403fc4f94038be252498fae55ec143"

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

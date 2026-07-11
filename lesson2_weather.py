import os

import requests

API_KEY = os.getenv("WEATHER_API_KEY")
city = "Thanjavur,IN"

url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    feels_like = data["main"]["feels_like"]



    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
    print(f"wind speed: {wind_speed}")
    print(f"feels like: {feels_like}")

else:
    print(f"Error: {response.status_code}")
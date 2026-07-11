import requests 
import time 
import schedule 
from datetime import datetime 
import os

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
     response = requests.get(url)
     if response.status_code == 200:
        return response.json()
     else:
        print(f"Error: {response.status_code}")
        return None

def weather_job():
     print(f"\n⏰ Auto check at {datetime.now().strftime('%H:%M:%S')}")
     data = get_weather("Mannargudi")
     if data:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        print(f"🌡️ Temp: {temp}°C | {condition}")
     
schedule.every().day.at("08:00").do(weather_job)


print("🚀 Weather scheduler started — checks every 10 seconds")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(1)
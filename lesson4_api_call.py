import requests 
from datetime import datetime 

API_KEY = "a3942e1d39d496eceff6564e38b40e2c"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
         return response.json()
    else:
         print(f"Error fetching weather: {response.status_code}")
         return None 
results = []
def display_weather_details(data,city):
     dict_details = {}
     temp = data["main"]["temp"]
     feels_like = data["main"]["feels_like"]
     humidity = data["main"]["humidity"]
     condition = data["weather"][0]["description"]
     wind_speed = data["wind"]["speed"]
     dict_details["city"] = city 
     dict_details["temperature"] = temp 
     dict_details["Humidity"] = humidity
     dict_details["condition"]= condition 
     dict_details["wind Speed"] = wind_speed 
      
     results.append(dict_details)


     #print(f"\n📍 Weather Report for {city.upper()}")
     #print(f"🌡️  Temperature: {temp}°C (Feels like {feels_like}°C)")
     #print(f"💧 Humidity: {humidity}%")
     #print(f"🌤️  Condition: {condition}")
     #print(f"💨 Wind Speed: {wind_speed} m/s")

     

     alerts = []

    
     if temp > 35:
        alerts.append(f"🔥 HIGH TEMPERATURE ALERT: {temp}°C")
     if humidity > 80:
        alerts.append(f"💧 HIGH HUMIDITY ALERT: {humidity}%")
     if "rain" in condition.lower():
        alerts.append(f"🌧️  RAIN ALERT: {condition}")
     if wind_speed > 10:
        alerts.append(f"💨 HIGH WIND ALERT: {wind_speed} m/s")
    
     if alerts:
        print("\n⚠️  ALERTS:")
        for alert in alerts:
            print(alert)
     else:
        print("\n✅ No alerts — weather looks fine!")
     timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

     with open("weather_log.txt","a",encoding="utf-8") as f:
         f.write(f"\n--- {timestamp} ---\n")
         f.write(f"City: {city}\n")
         f.write(f"Temp: {temp}°C, Humidity: {humidity}%, Condition: {condition}\n")

         if alerts:
             for alert in alerts:
                 f.write(f"ALERT:{alert}\n")
         else:
             f.write("No alerts\n")
     print(f"\n📁 Log saved at {timestamp}")

     

    


print("All 5 city names for weather ")
for i in range(5):
    city = input(f"Enter city{i+1} name: ")
    data = get_weather(city)
    if data:
        display_weather_details(data,city)
    

print("\n🌍 City Comparison:")
print(f"{'City':<15} {'Temp':<10} {'Humidity':<12} {'Condition'}")
print("-" * 55)
for r in results:
    print(f"{r['city']:<15} {r['temperature']:<10} {r['Humidity']:<12} {r['condition']}")


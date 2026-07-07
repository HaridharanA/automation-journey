import requests

API_KEY = "a3942e1d39d496eceff6564e38b40e2c"
city = "Thanjavur,IN"

url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]


    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print(f"Error: {response.status_code}")
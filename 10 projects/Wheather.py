import requests

def get_weather(city):
    api_key = "cbb62a7eac949df508cb18d8f27a1db4"  
# Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Set parameters
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"📍 Weather in {city}: {weather}")
        print(f"🌡️ Temperature: {temp}°C")
    else:
        print("❌ City not found. Please check the spelling.")

# Main Program
print("🌦️ Weather Predictor")
city_name = input("Enter city name: ")
get_weather(city_name)

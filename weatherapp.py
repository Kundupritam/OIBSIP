#importing requests module
import requests

#fetching information using city_name and api_key
def get_weather(city_name,api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]

        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Condition: {weather['description']}")
    else:
        print("City not found. Please try again.")

#taking input of cit_name from user
def main():
    print("=== Simple Weather App ===")
    api_key = "2d5570568d1df0f33be23bc4ef400f93"    # API key disposed – generate a new one if needed
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()





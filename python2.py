import requests
import json

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key def get_weather(self, city_name):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        complete_url = base_url + "?appid=" + self.api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            print("Temperature (in kelvin unit) = " +
                  str(current_temperature) +
                  "\nAtmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\nHumidity (in percentage) = " +
                  str(current_humidity) +
                  "\nDescription = " +
                  str(weather_description))
        else:
            print("City Not Found")

def main():
    api_key = "YOUR_API_KEY"
    weather_fetcher = WeatherFetcher(api_key)

    city_name = input("Enter city name: ")
    weather_fetcher.get_weather(city_name)

if __name__ == "__main__":
    main()

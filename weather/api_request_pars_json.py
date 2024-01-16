import requests
import os
from dataclasses import dataclass
from data_weather_set import WeatherData
from message_data_set import Message


@dataclass
class Requests:
    url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")

    @classmethod
    def end_point(cls, city):
        """Returns formatted url"""
        return f"{cls.url}/data/2.5/weather?q={city}&appid={cls.api_key}"

    @classmethod
    def get_openwather(cls, city, language):
        """Makes an api request to openweather, displays a weather message to the console"""
        endpoint = cls.end_point(city)
        params = {
            "q": city,
            "appid": cls.api_key,
            "lang": language,
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            weather_data = response.json()

            parsed_weather = {
                "city_name": weather_data["name"],
                "weather_id": weather_data["weather"][0]["id"],
                "atmosphere": weather_data["weather"][0]["main"],
                "temp_min": weather_data["main"]["temp_min"],
                "temp_max": weather_data["main"]["temp_max"],
                "country_name": weather_data["sys"]["country"],
                "temperature": weather_data["main"]["temp"],
                "temp_feels_like": weather_data["main"]["feels_like"],
                "condition_of_sky": weather_data["weather"][0]["description"],
                "wind_speed": weather_data["wind"]["speed"],
                "humidity": weather_data["main"]["humidity"],
            }

            weather_id = parsed_weather["weather_id"]
            icon = WeatherData.get_weather_group(weather_id)

            country = parsed_weather["country_name"]
            city_name = parsed_weather["city_name"]
            temp_kelvin = parsed_weather["temperature"]
            temp_min = parsed_weather["temp_min"]
            temp_max = parsed_weather["temp_max"]
            temp_kelvin_feels = parsed_weather["temp_feels_like"]
            descript = parsed_weather["condition_of_sky"]
            wind_speed = parsed_weather["wind_speed"]
            humidity = parsed_weather["humidity"]

            temp_in_cels = WeatherData.get_celsius(float(temp_kelvin))
            temp_in_cels_min = WeatherData.get_celsius(float(temp_min))
            temp_in_cels_max = WeatherData.get_celsius(float(temp_max))
            temp_in_cels_feels = WeatherData.get_celsius(float(temp_kelvin_feels))

            text = Message.text_message(
                country,
                city_name,
                temp_in_cels,
                temp_in_cels_min,
                temp_in_cels_max,
                temp_in_cels_feels,
                descript,
                icon,
                wind_speed,
                humidity,
            )
            print(text)

        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                print("Error 400: Bad Request")
            elif e.response.status_code == 404:
                print("Error 404: Data is not found on the server")
            elif e.response.status_code == 503:
                print("Error 503: Service unavailable")
            else:
                print("Error during the API request:", e)

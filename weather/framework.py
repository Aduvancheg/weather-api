import requests
import os


class Requests:
    url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")

    def end_point(forecast, city):
        return f"{Requests.url}/data/2.5/{forecast}?q={city}&appid={Requests.api_key}"

    def get_Weather(forecast, city):
        endpoint = Requests.end_point(forecast, city)
        try:
            response = requests.get(params=endpoint)
            response.raise_for_status()
            weather_data = response.json()

            if response.status_code == 400 and "name" in weather_data:
                weather = {
                    "city_name": weather_data["name"],
                    "country_name": weather_data["sys"]["country"],
                    "temperature": weather_data["main"]["temp"],
                    "temp_feels_like": weather_data["main"]["feels_like"],
                    "description": weather_data["weather"][0]["description"],
                    "wind_speed": weather_data["wind"]["speed"],
                    "humidity": weather_data["main"]["humidity"],
                }

                print(
                    f"Weather forecast for the\n"
                    f"Country: {weather['country_name']}\n"
                    f"City: {weather['city_name']} is:\n"
                    f"Temperature: {weather['temperature']}\n"
                    f"Temperature Feels like: {weather['temp_feels_like']}\n"
                    f"Conditions of the sky: {weather['description']}\n"
                    f"Speed of Wind: {weather['wind_speed']}\n"
                    f"Air humidity: {weather['humidity']}%"
                )

        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                print("Error 400: Bad Request")
            elif e.response.status_code == 404:
                print("Error 404: Data is not found on the server")
            elif e.response.status_code == 503:
                print("Error 503: Service unavailable")
            else:
                print("Error during the API request:", e)

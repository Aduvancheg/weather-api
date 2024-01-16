from dataclasses import dataclass


@dataclass
class Thunderstorm:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Drizzle:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Rain:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Snow:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Atmosphere:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Clear:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class Clouds:
    id: int = 0
    main: str = ""
    description: str = ""
    icon: str = ""


@dataclass
class WeatherData:
    kelvin_constant: float = 273.15

    thunderstorm_group2 = [
        Thunderstorm(
            id=200,
            main="Thunderstorm",
            description="thunderstorm with light rain",
            icon="🌩️",
        ),
        Thunderstorm(
            id=201,
            main="Thunderstorm",
            description="thunderstorm with rain",
            icon="⛈️",
        ),
        Thunderstorm(
            id=202,
            main="Thunderstorm",
            description="thunderstorm with heavy rain",
            icon="⛈️",
        ),
        Thunderstorm(
            id=210,
            main="Thunderstorm",
            description="light thunderstorm",
            icon="⚡",
        ),
        Thunderstorm(
            id=211,
            main="Thunderstorm",
            description="thunderstorm",
            icon="🌩️",
        ),
        Thunderstorm(
            id=212,
            main="Thunderstorm",
            description="heavy thunderstorm",
            icon="🌩️",
        ),
        Thunderstorm(
            id=221,
            main="Thunderstorm",
            description="ragged thunderstorm",
            icon="🌩️",
        ),
        Thunderstorm(
            id=230,
            main="Thunderstorm",
            description="thunderstorm with light drizzle",
            icon="⛈️",
        ),
        Thunderstorm(
            id=231,
            main="Thunderstorm",
            description="thunderstorm with drizzle",
            icon="⛈️",
        ),
        Thunderstorm(
            id=232,
            main="Thunderstorm",
            description="thunderstorm with heavy drizzle",
            icon="⛈️",
        ),
    ]

    drizzle_group3 = [
        Drizzle(
            id=300,
            main="Drizzle",
            description="light intensity drizzle",
            icon="🌦️",
        ),
        Drizzle(
            id=301,
            main="Drizzle",
            description="drizzle",
            icon="🌧️",
        ),
        Drizzle(
            id=302,
            main="Drizzle",
            description="heavy intensity drizzle",
            icon="🌧️",
        ),
        Drizzle(
            id=310,
            main="Drizzle",
            description="light intensity drizzle rain",
            icon="🌦️",
        ),
        Drizzle(
            id=311,
            main="Drizzle",
            description="drizzle rain",
            icon="🌧️",
        ),
        Drizzle(
            id=312,
            main="Drizzle",
            description="heavy intensity drizzle rain",
            icon="🌧️",
        ),
        Drizzle(
            id=313,
            main="Drizzle",
            description="shower rain and drizzle",
            icon="🌧️",
        ),
        Drizzle(
            id=314,
            main="Drizzle",
            description="heavy shower rain and drizzle",
            icon="🌧️",
        ),
        Drizzle(
            id=321,
            main="Drizzle",
            description="shower drizzle",
            icon="🌧️",
        ),
    ]

    rain_group5 = [
        Rain(
            id=500,
            main="Rain",
            description="light rain",
            icon="🌦️",
        ),
        Rain(
            id=501,
            main="Rain",
            description="moderate rain",
            icon="🌧️",
        ),
        Rain(
            id=502,
            main="Rain",
            description="heavy intensity rain",
            icon="🌧️",
        ),
        Rain(
            id=503,
            main="Rain",
            description="very heavy rain",
            icon="🌧️",
        ),
        Rain(
            id=504,
            main="Rain",
            description="extreme rain",
            icon="🌧️",
        ),
        Rain(
            id=511,
            main="Rain",
            description="freezing rain",
            icon="🌧️",
        ),
        Rain(
            id=520,
            main="Rain",
            description="light intensity shower rain",
            icon="🌦️",
        ),
        Rain(
            id=521,
            main="Rain",
            description="shower rain",
            icon="🌧️",
        ),
        Rain(
            id=522,
            main="Rain",
            description="heavy intensity shower rain",
            icon="🌧️",
        ),
        Rain(
            id=522,
            main="Rain",
            description="ragged shower rain",
            icon="🌧️",
        ),
    ]

    snow_group6 = [
        Snow(
            id=600,
            main="Snow",
            description="light snow",
            icon="❄️",
        ),
        Snow(
            id=601,
            main="Snow",
            description="snow",
            icon="❄️",
        ),
        Snow(
            id=602,
            main="Snow",
            description="heavy snow",
            icon="⛄️",
        ),
        Snow(
            id=611,
            main="Snow",
            description="sleet",
            icon="❄️",
        ),
        Snow(
            id=612,
            main="Snow",
            description="light shower sleet",
            icon="❄️",
        ),
        Snow(
            id=613,
            main="Snow",
            description="shower sleet",
            icon="❄️",
        ),
        Snow(
            id=615,
            main="Snow",
            description="light rain and snow",
            icon="❄️",
        ),
        Snow(
            id=616,
            main="Snow",
            description="rain and snow",
            icon="❄️",
        ),
        Snow(
            id=620,
            main="Snow",
            description="light shower snow",
            icon="❄️",
        ),
        Snow(
            id=621,
            main="Snow",
            description="shower snow",
            icon="⛄️",
        ),
        Snow(
            id=622,
            main="Snow",
            description="heavy shower snow",
            icon="⛄️",
        ),
    ]

    atmosphere_group7 = [
        Atmosphere(
            id=701,
            main="Mist",
            description="mist",
            icon="🌫️",
        ),
        Atmosphere(
            id=711,
            main="Smoke",
            description="smoke",
            icon="🌫️",
        ),
        Atmosphere(
            id=721,
            main="Haze",
            description="haze",
            icon="🌫️",
        ),
        Atmosphere(
            id=731,
            main="Dust",
            description="sand/dust whirls",
            icon="🌫️",
        ),
        Atmosphere(
            id=741,
            main="Fog",
            description="fog",
            icon="🌫",
        ),
        Atmosphere(
            id=751,
            main="Sand",
            description="sand",
            icon="🌫️",
        ),
        Atmosphere(
            id=761,
            main="Dust",
            description="dust",
            icon="🌫️",
        ),
        Atmosphere(
            id=762,
            main="Ash",
            description="volcanic ash",
            icon="🌫️",
        ),
        Atmosphere(
            id=771,
            main="Squall",
            description="squalls",
            icon="🌫️",
        ),
        Atmosphere(
            id=781,
            main="Tornado",
            description="tornado",
            icon="🌪",
        ),
    ]

    clear_group8 = [
        Clear(
            id=800,
            main="Clear",
            description="clear sky",
            icon="🌞",
        ),
    ]

    clouds_group8 = [
        Clouds(
            id=801,
            main="Clouds",
            description="few clouds: 11-25%",
            icon="🌤️",
        ),
        Clouds(
            id=802,
            main="Clouds",
            description="scattered clouds: 25-50%",
            icon="🌥️",
        ),
        Clouds(
            id=803,
            main="Clouds",
            description="broken clouds: 51-84%",
            icon="🌥️",
        ),
        Clouds(
            id=804,
            main="Clouds",
            description="overcast clouds: 85-100%",
            icon="☁️",
        ),
    ]

    @classmethod
    def get_weather_group(cls, target_id):
        for group in [
            cls.thunderstorm_group2,
            cls.drizzle_group3,
            cls.rain_group5,
            cls.snow_group6,
            cls.atmosphere_group7,
            cls.clear_group8,
            cls.clouds_group8,
        ]:
            for obj in group:
                if obj.id == target_id:
                    return obj.icon
        return "Something went wrong"

    @classmethod
    def get_celsius(cls, tem_kelvin) -> float:
        temperature = tem_kelvin - cls.kelvin_constant
        return temperature

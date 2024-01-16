# JSON parsing factory and Weather message composition


# Environment setup, git workflow
### Set up your environment like described in this guide: `https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99`


## Install packages and venv
``` shell
cd /path/to/project/root
```

## Install dependencies from pyproject.toml
``` shell
pdm install
```

## Set up: environment variable configuration
# Create file .env in the yourproject root
``` shell
touch .env
```

## Register on the `http://api.openweathermap.org` web site, then generate your own unic an API key in your profile: `https://home.openweathermap.org/api_keys`

## Add env's configurations to file .env
``` shell
API_URL="http://api.openweathermap.org"
API_KEY="example"
```

## Export environment variables from .env file
``` shell
export $(cat .env | xargs)
```


# Usage
### API documentation of openweather: `https://openweathermap.org/api`

### To run this code, next step should be fulfilled:
## Where arguments: №1 name of city, for example: `Warsaw`, if city hase 2 or 3 words you need to combine them using quotes for example: `Los Angeles`. Argument №2 is abbreviation of name of language, for example `en`, or 'ru', but you will get only description of weathere on this target language, another code will be on original Eng language.
```shell
pdm run ./weather/get_weather_cli_parser.py Warsaw pl
```

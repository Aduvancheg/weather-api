from datetime import datetime
from dataclasses import dataclass


@dataclass
class Message:
    PADDING: int = 20
    REVERSE = "\033[;7m"
    RESET = "\033[0m"
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[33m"
    WHITE = "\033[37m"

    @classmethod
    def display_text_with_padding(cls, text):
        padded_text = " " * cls.PADDING + text + " " * cls.PADDING
        print(padded_text)

    @classmethod
    def date(self):
        date_time = datetime.now()
        now = date_time.strftime("%d/%m/%Y %H:%M")
        return now

    @classmethod
    def text_message(
        cls,
        country,
        city,
        temperature,
        temp_min,
        temp_max,
        temp_feels,
        description,
        icon,
        wind_speed,
        humidity,
    ):
        today = cls.date()

        return (
            f"{cls.PADDING * ' '}{cls.YELLOW} Weather forecast on: {today} {cls.RESET}{cls.PADDING * ' '}\n"
            f"{cls.WHITE}Country:{cls.RESET} {cls.RED}{country}{cls.RESET}\n"
            f"{cls.WHITE}City:{cls.RESET} {cls.RED}{city}{cls.RESET}\n"
            f"Temperature: {cls.RED  if round(temperature) > 0 else cls.CYAN}{round(temperature)}{cls.RESET}\n"
            f"Temperature min: {cls.RED  if round(temp_min) > 0 else cls.CYAN}{round(temp_min)}{cls.RESET}\n"
            f"Temperature max: {cls.RED  if round(temp_max) > 0 else cls.CYAN}{round(temp_max)}{cls.RESET}\n"
            f"Temperature Feels like: {cls.RED if round(temp_feels) > 0 else cls.CYAN}{round(temp_feels)}\n"
            f"{cls.BLUE}Conditions of the sky:{cls.RESET} {cls.GREEN}{description}{cls.RESET}, {icon}\n"
            f"{cls.BLUE}Speed of Wind:{cls.RESET} {cls.GREEN}{round(wind_speed)}{cls.RESET}\n"
            f"{cls.BLUE}Air humidity:{cls.RESET} {cls.GREEN}{humidity}%{cls.RESET}"
        )

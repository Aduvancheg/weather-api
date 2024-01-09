import argparse
from framework import Requests


def read_user_cli_input():
    """Read user cli input"""

    parser = argparse.ArgumentParser(
        description="Get the current or forecasted weather for a specific city"
    )

    parser.add_argument(
        "forecast",
        type=str,
        help="Current weather or future, this option can be one of them: weather or forecast",
    )
    parser.add_argument("city", type=str, help="Name of the city")
    args = parser.parse_args()
    forecast = args.forecast
    city = args.city
    Requests.get_Weather(forecast, city)


if __name__ == "__main__":
    read_user_cli_input()

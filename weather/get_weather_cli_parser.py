import argparse
from api_request_pars_json import Requests


def read_user_cli_input():
    """Read user cli input"""

    parser = argparse.ArgumentParser(
        description="Get the current or forecasted weather for a specific city"
    )
    parser.add_argument("city", type=str, help="Name of the city")
    parser.add_argument("language", type=str, help="Type of language")
    args = parser.parse_args()
    city = args.city
    language = args.language

    Requests.get_openwather(city, language)


if __name__ == "__main__":
    read_user_cli_input()

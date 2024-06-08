from typing import Any

import requests  # type: ignore


def get_weather(city: str) -> Any:
    """
    Retrieve the weather forecast for a city.

    :param city: The city's name.
    :return: A dictionary containing the weather information.
    """
    response = requests.get(f"https://weatherchannel.com/{city}")
    return response.json()

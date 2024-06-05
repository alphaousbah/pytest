from typing import Any


def format_data_for_display(people: list[dict[str, Any]]) -> list[str]:
    """
    Format the given list of people data for display.

    :param people: A list of dictionaries containing people's data.
    :return: A list of formatted strings for display.
    """
    formatted_data = [
        f"{person['given_name']} {person['family_name']}: {person['title']}"
        for person in people
    ]
    return formatted_data


def format_data_for_excel(people: list[dict[str, Any]]) -> str:
    """
    Format the given list of people data for display in Excel format.

    :param people: A list of dictionaries containing people's data.
    :return: A formatted string suitable for Excel.
    """
    header = "given,family,title"
    rows = [
        f"{person['given_name']},{person['family_name']},{person['title']}"
        for person in people
    ]
    return f"{header}\n" + "\n".join(rows)

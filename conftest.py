from typing import Any

import pytest


@pytest.fixture  # type: ignore[misc]
def people_data() -> list[dict[str, Any]]:
    return [
        {
            "name": "Bob",
            "age": 35,
            "gender": "male",
            "hobbies": ["music", "sports"],
            "favorite_color": "blue",
        },
        {
            "name": "Alice",
            "age": 30,
            "gender": "female",
            "hobbies": ["reading", "hiking"],
            "favorite_color": "green",
        },
        {
            "name": "Charlie",
            "age": 42,
            "gender": "male",
            "hobbies": ["music", "traveling"],
            "favorite_color": "red",
        },
    ]

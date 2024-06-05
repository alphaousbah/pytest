from typing import Any

import pytest


@pytest.fixture  # type: ignore[misc]
def people_data() -> list[dict[str, Any]]:
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

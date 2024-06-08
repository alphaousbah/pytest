from typing import Any

import pytest

from format_data import format_data_for_display


@pytest.mark.data_test  # type: ignore[misc]
def test_format_data_for_display(people_data: list[dict[str, Any]]) -> None:
    assert format_data_for_display(people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

from typing import Any

from format_data import format_data_for_display, format_data_for_excel


def test_format_data_for_display(people_data: list[dict[str, Any]]) -> None:
    assert format_data_for_display(people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel(people_data: list[dict[str, Any]]) -> None:
    assert (
        format_data_for_excel(people_data)
        == """given,family,title
    Alfonsa,Ruiz,Senior Software Engineer
    Sayid,Khan,Project Manager
    """
    )

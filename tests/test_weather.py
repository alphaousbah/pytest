from pytest_mock import MockerFixture

from engine.function_weather import get_weather


def test_gest_weather(mocker: MockerFixture) -> None:
    mock_data = {
        "temperature": "+7 °C",
        "wind": "13 km/h",
        "description": "Partly cloudy",
        "forecast": [
            {"day": "1", "temperature": "+10 °C", "wind": "13 km/h"},
            {"day": "2", "temperature": "+6 °C", "wind": "26 km/h"},
            {"day": "3", "temperature": "+15 °C", "wind": "21 km/h"},
        ],
    }
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data

    mocker.patch("requests.get", return_value=mock_response)

    result = get_weather("London")

    assert result == mock_data

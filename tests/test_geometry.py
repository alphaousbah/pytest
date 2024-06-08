import pytest
from pytest_mock import MockerFixture

from engine.function_geometry import get_circle_area


def test_get_circle_area(mocker: MockerFixture) -> None:
    mocker.patch("engine.function_geometry.PI", 6)
    expected = 24
    obtained = get_circle_area(2)
    assert obtained == pytest.approx(expected)

import pytest


@pytest.fixture  # type: ignore[misc]
def example_fixture() -> int:
    return 1


class TestClass:
    def test_with_fixture(self, example_fixture: int) -> None:
        assert example_fixture == 1

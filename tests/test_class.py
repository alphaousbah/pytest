import pytest


class TestClass:
    def test_one(self) -> None:
        x: str = "hello"
        assert "h" in x

    @pytest.mark.xfail  # type: ignore[misc]
    def test_two(self) -> None:
        x: str = "hello"
        assert hasattr(x, "row")

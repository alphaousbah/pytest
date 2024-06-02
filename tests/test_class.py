class TestClass:
    def test_one(self) -> None:
        x: str = "hello"
        assert "h" in x

    def test_two(self) -> None:
        x: str = "hello"
        assert hasattr(x, "row")

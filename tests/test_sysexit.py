import pytest


def f() -> None:
    raise SystemExit(1)


def test_mytest() -> None:
    with pytest.raises(SystemExit):
        f()

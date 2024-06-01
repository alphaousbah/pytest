def do_this(x: int) -> int:
    """
    This function does this.

    :param x: x is an integer.
    :return: The value of x plus one.
    """
    return x + 1


def test_do_this() -> None:
    assert do_this(1) == 2

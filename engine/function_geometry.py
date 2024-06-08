PI = 3


def get_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle from its radius

    :param radius: The radius of the circle.
    :return: The area of the circle.
    :raise TypeError: If the radius is not a number.
    :raise ValueError: If the radius is negative.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("The radius must be a number")
    if radius < 0:
        raise ValueError("The radius must be positive")
    return PI * radius**2

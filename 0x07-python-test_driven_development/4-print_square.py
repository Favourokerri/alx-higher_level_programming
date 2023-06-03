#!/usr/bin/python3
"""function that prints a square with the character # """


def print_square(size):
    """ prints a square with #
    Args:
        size - length of the quare and must be n integer
    Raises:
        ValueError if size is less than 0
        TypeError if size is float and less than 0
    Return:
        square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)

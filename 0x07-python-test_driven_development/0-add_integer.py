#!/usr/bin/python3
"""
    add two numbers together
"""


def add_integer(a, b=98):
    """Try to addd two numbers together
    Args:
        a = first number and must be integer or float
        b = second number with default value 98 and must be float or integer
    raises:
        raise a type error of any of the numbers is not a float or an integer
    Returns:
        returns the addition of both numbers
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        return(int(a) + int(b))
    except TypeError as e:
        raise TypeError(e)

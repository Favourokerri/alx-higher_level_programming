#!/usr/bin/python3
"""An empty class"""


class BaseGeometry:
    """This is an empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """vlidate integer
        Args:
            name - name of the integer
            value - value of integer
        raises:
            type error if not integer
            value erro if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

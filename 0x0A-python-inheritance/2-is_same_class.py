#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """checks if an object is instance of a class
    Args:
        obj - object to be checked
        a_class - the Base class
    Returns: true if object isinstance otherwise false
    """
    return (type(obj) == a_class)

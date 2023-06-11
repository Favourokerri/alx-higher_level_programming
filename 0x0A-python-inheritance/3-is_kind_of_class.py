#!/usr/bin/python3
"""if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """ check if an object is an instance
    Args:
        obj - the objecy
        a_class - the class
    Returns - True if instance else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
""" a function that returns says a persons name """


def say_my_name(first_name, last_name=""):
    """ function that says a persons name
    Args:
        first_name = the first name of the user
        last_name = last_name of the user
    raises:
        if name not a string, raise TypeError
    Return:
        My name is <first name> <last name>
    """

    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        print("My name is {}, {}".format(first_name, last_name))
    except TypeError as e:
        raise TypeError(e)

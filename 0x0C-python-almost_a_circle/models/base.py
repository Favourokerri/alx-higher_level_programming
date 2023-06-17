#!/usr/bin/python3
"""base class with a private attribute """


class Base:
    """Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id if it is not none """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

#!/usr/bin/python3
""" inherits from another class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """print list in sorted form """
        print(sorted(self))

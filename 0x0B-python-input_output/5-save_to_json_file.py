#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a file usuing json
    Args:
        my_obj - the object
        filename - name of the file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

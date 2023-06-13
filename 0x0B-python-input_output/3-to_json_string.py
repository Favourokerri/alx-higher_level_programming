#!/usr/bin/python3
"""converts object string to json format """
import json


def to_json_string(my_obj):
    """prints the json representation format"""
    json_rep = json.dumps(my_obj)
    return (json_rep)

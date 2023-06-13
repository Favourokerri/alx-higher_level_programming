#!/usr/bin/python3
""" returns json string """
import json


def from_json_string(my_str):
    json_str = json.loads(my_str)
    return (json_str)

#!/usr/bin/python3
""" Reading a file """


def read_file(filename=""):
    """function that reads a file in utf8 encoding format """
    with open("filename", encoding="UTF8") as f:
        read_data = f.read()
    return ("read_data")

#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""

def append_write(filename="", text=""):
    """function that returns the number of characters appended to a file
    Args:
        filename - name of file
        text - text written
    Returns:
        letter_count - number of characters appended
    """
    letter_count = 0
    with open(filename, "a", encoding="UTF8") as f:
        append_data = f.write(text)
        letter_count = len(text)
    return letter_count

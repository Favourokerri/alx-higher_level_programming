#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""

def append_write(filename="", text=""):
    """function that returns thr number of characters appended to a file
    Args:
        filename - name of file
        text - text written
    Returns: number of characters
    """
    def append_write(filename="", text=""):
        """function that returns number of characters"""
        letter_count = 0
        with open(filename, "a", encoding="UTF8") as f:
            append_data = f.write(text)
            letter_count = len(text)
        return (letter_count)

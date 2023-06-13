#!/usr/bin/python3
"""a function that returns the number of characters written to a file """


def write_file(filename="", text=""):
    """returns the number of character written
    Args:
        filename - file to be written to
        text - content of file
    Returns: number of character
    """
    count_letter = 0
    with open(filename, "w", encoding="UTF8") as f:
        write_data = f.write(text)
        for i in text:
            count_letter += 1
    return (count_letter)

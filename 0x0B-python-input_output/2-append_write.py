#!/usr/bin/python3

"""A module that appends content to afile"""


def append_write(filename="", text=""):
    """
    appends text to a file
    and returns number of charsa dded

    Args:
        filename: (file)file to append data to
        text: (str) daato append to file

    return:
        number of chars printed
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_of_chars_printed = file.write(text)
        return (num_of_chars_printed)

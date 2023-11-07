#!/usr/bin/python3

"""A module that writes to afile and returns number or characters printed"""


def write_file(filename="", text=""):
    """Afunction that creates and or writes to a file
    and returns the number or char printed

    Args:
        filename: (file) file to write to or create
        text:(str) string to write to file

    return:
        the number of chars printed
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars_printed = file.write(text)
        return (num_chars_printed)

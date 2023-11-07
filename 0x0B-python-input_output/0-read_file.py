#!/usr/bin/python3


"""a module which reads a file and prints to stdout"""


def read_file(filename=""):
    """
    reads into a file and prints its contents
    to stdout

    Args:
        filename:(file)file to read from
    """

    with open(filename, "r+", encoding="utf-8") as file:

        """
        while the file is not empty continue reading"""
        lines = file.readlines()

        for line in lines:
            print(line, end="")

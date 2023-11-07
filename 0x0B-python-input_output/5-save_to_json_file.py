#!/usr/bin/python3

"""A module that writes to json"""
import json


def save_to_json_file(my_obj, filename):
    """
    opens the file and encodes the object
    then writes it to a json file

    Args:
        my_obj: (str) to write to  a file
        filename: (json) the file to write to
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)

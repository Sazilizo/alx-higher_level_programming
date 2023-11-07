#!/usr/bin/python3

""" A module that decodes json string to python """
import json


def from_json_string(my_str):
    """
    decodes the json data to python string

    Args:
        my_str: (json_data) data to decode (deserialize)
    return:
        a python string
    """
    to_python_str = json.loads(my_str)
    return (to_python_str)

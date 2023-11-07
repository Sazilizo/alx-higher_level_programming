#!/usr/bin/python3

import json
""" A module that encodes a python string to json"""


def to_json_string(my_obj):
    """
    Encodes the string passed to json data

    Args:
        my_obj: (any) object to encode

    return:
        encoded json string
    """

    return (json.dumps(my_obj))

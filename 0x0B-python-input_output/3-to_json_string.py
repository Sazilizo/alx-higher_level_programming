#!/usr/bin/python3

""" A module that encodes a python string to json"""
import json


def to_json_string(my_obj):
    """
    Encodes the string passed to json data

    Args:
        my_obj: (any) object to encode

    return:
        encoded json string
    """
    to_json = json.dumps(my_obj)
    return (to_json)

#!/usr/bin/python3

"""A module that that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    creates an object from a json file to python

    Args:
        filename:file

    """
    with open(filename, "r") as json_file:
        obj = json.load(json_file)
        return(obj)

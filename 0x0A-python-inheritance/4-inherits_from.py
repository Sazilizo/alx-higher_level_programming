#!/usr/bin/python3

"""Checks instance of a class"""


def inherits_from(obj, a_class):
    """
    checks instance is of a subclass

    Args:
        obj: (any type) to check
        a_class: to check against

    return:
        True is issubclass(type(obj), a_class)
        else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        False

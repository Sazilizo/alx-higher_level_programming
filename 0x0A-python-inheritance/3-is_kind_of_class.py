#!/usr/bin/python3

"""A class checking module"""


def is_kind_of_class(obj, a_class):
    """
        checks if instance of obj is a_class

    Args:
        obj: (any type) type to chec
        a_class: obj to check against

    return:
        True if instance of obj == a_class
        else False

    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

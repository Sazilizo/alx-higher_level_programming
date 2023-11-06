#!/usr/bin/python3

"""A function that checks for a class"""


def is_same_class(obj, a_class):
    """
    checks if the type is the same as a_class

    Args:
        obj: (any type)the type to check
        a_class: the type to check against

    return:
        if obj == a_class type return True
        else return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

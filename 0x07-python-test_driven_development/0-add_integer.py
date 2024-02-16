#!/usr/bin/python3


def add_integer(a, b=98)
    """
        add_integer isa function that add two integers and returns their sum
        if either of the arguments are not of type int or float then raise a TypeError

        Args:
            a: (int) integer to add
            b:(int) integer to add

        Raises:
            TypeError: If a or b aren't integer and/or float numbers

        return: sum of a and b

    """
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)

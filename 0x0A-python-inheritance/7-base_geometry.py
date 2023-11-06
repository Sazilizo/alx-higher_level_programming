#!/usr/bin/python3

"""A BaseGeometry module"""


class BaseGeometry:
    """
    A base Geometry class"""

    def area(self):
        """
        sets the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        raises ValueError and TypeError if conditionsare not met
        Args:
            self: object
            name: a string
            value: shuld be an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

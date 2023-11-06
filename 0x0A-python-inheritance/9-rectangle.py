#!/usr/bin/python3


"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle subclass of BaseGeometry"""
    def __init__(self, width, height):
        """
        Initializing new Rectangle method

        Args:
            width: (int) Rectangle width
            height: (int) Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        """ Return str """
        return("[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height))

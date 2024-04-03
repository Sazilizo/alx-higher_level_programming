#!/usr/bin/python3


"""
a module consisting of a Rectangle class
that has a getter and setter for both width and height
"""


class Rectangle:
    """A Rectangle class with attributes  width and height"""
    def __init__(self, width=0, height=0):
        """
       Initialize a Rectangle instance with a given width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The new width value.
        if width > 0 raise ValueErorr
        if width is not of int type, raise TypeError
        """
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

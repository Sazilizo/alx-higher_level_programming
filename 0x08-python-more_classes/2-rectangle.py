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
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        :param value: The new width value.
        if width > 0 raise ValueErorr
        if width is not of int type, raise TypeError
        """
        if not(isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: the height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, height):
        if not(isinstance(height, int)):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = height

    def area(self):
        return self._height * self._width

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2*(self._width + self._height)

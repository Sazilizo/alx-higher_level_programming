#!/usr/bin/python3

from models.base import Base
"""A modulethat inherits from the Base class"""


class Rectangle(Base):
    """
    A Rectangle class that inherits from Base
    sets private instance attribute
    calls init function from the Parent class
    which checks if id is of type int or not

    each private attribute has a getter and a setter

    Args:
        Base: (class) Parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def __height(self):
        return self.__height

    @__height.setter
    def __height(self, height):
        self.__height = height

    @property
    def __width(self):
        return self.__width

    @__width.setter
    def __width(self, width):
        self.__width = width

    @property
    def __x(self):
        return self.__x

    @__x.setter
    def __x(self, x):
        self.__x = x

    @property
    def __y(self):
        return self.__y

    @__y.setter
    def __y(self, y):
        self.__y = y

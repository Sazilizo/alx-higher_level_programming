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
        """Inittializing all the attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        Getter function for height
        returns the private height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This methos sets the private height attribute to value
        """
        self.__height = value

    @property
    def width(self):
        """Return the value of private attrbute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of private attribute width to value
        Args:
            value: (int)
        """
        self.__width = value

    @property
    def x(self):
        """
        Gets the value at private attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets th value of private attribute x to value
        Args: 
            value: (int) 
        """
        self.__x = value

    @property
    def y(self):
        """
        Gets the value at private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the private attribute value to value
        Args:
            value: (int)
        """
        self.__y = value
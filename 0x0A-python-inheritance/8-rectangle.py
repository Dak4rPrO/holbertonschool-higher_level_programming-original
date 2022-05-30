#!/usr/bin/python3
"""class basegeometry"""


class BaseGeometry:
    """ My BaseGeometry class """

    def area(self):
        """ def area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ def integer """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


"""class rectangle"""


class Rectangle(BaseGeometry):
    """ My Rectangle class """

    def __init__(self, width, height):
        """ init def """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

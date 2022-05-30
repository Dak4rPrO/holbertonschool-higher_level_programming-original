#!/usr/bin/python3
class BaseGeometry:
    """ My BaseGeometry class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ My Rectangle class """

    def __init__(self, width, height):
        super().integer_validator(width, height)
        self.__width = width
        self.__height = height
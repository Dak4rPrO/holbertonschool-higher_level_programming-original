#!/usr/bin/python3
""" class basegeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ My Rectangle class """

    def __init__(self, width, height):
        """ def init """

        super().integer_validator(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        """ def area """

        return(self.__width * self.__height)

    def __str__(self):
        """ def str """

        return (f"[Rectangle] {self.__width}/{self.__height}")

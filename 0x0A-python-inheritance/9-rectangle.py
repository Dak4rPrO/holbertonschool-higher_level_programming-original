#!/usr/bin/python3
""" class basegeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ My Rectangle class """

    def __init__(self, width, height):
        """ def init """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        
        """ def area """
    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        """ def str """

        return (f"[Rectangle] {self.__width}/{self.__height}")

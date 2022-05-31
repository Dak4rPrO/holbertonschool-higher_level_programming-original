#!/usr/bin/python3
""" class rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ My Square class """

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        return(self.__size * self.__size)

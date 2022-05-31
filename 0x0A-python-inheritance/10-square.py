#!/usr/bin/python3
""" class rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ My Square class """
    
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return(self.__size * self.__size)

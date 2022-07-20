#!/usr/bin/python3
"""estupido estandar"""


class Square:
    """estupido estandar"""

    def __init__(self, size=0):
        """ def init """

        self.size = size

    @property
    def size(self):
        """def size"""
        return self.__size

    @size.setter
    def size(self, value):
        """def size, value"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > = 0")
        self.__size = value

    def area(self):
        """ def area """
        return(self.__size * self.__size)

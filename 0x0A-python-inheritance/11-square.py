#!/usr/bin/python3
""" import """


Rectangle = __import__("9-rectangle").Rectangle
""" class square """


class Square(Rectangle):
    """ My Square class """

    def __init__(self, size):
        """ def init """

        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """def area """

        return(self.__size * self.__size)

    def __str__(self):
        """ def str """

        return (f"[Square] {self.__size}/{self.__size}")

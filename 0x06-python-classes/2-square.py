#!/usr/bin/python3
"""estupido estandar"""


class Square:
    """estupido estandar"""

    def __init__(self, size=0):
        """ def init """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

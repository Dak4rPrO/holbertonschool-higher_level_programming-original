#!/usr/bin/python3
""" class basegeometry """


class BaseGeometry:
    """ My BaseGeometry class """

    def area(self):
        """ def area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """def integer """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


""" class rectangle """


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


""" class square """


class Square(Rectangle):
    """ My Square class """

    def __init__(self, size):
        """ def init """

        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ def area """

        return(self.__size * self.__size)

#!/usr/bin/python3
""" Call the super class with id, x, y, width and height - this super call will
use the logic of the __init__ of the Rectangle class. The width and height must
be assigned to the value of size """


from models.rectangle import Rectangle


class Square:
    """ class Square that inherits from Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ def init """
        super().__init__(id, size, size, x, y)
        
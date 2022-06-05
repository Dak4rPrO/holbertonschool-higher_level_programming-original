#!/usr/bin/python3
""" Call the super class with id, x, y, width and height - this super call will
use the logic of the __init__ of the Rectangle class. The width and height must
be assigned to the value of size """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ def init """
        super().__init__(size, size, x, y, id)
        
        def __str__(self):
            """ def str """
            return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
        
        @property
        def size(self):
            return self.height
        
        @size.setter
        def size(self, value):
            """ def size"""
            self.width = value
            self.height = value       
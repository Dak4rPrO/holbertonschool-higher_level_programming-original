#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creating class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing class Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Rewriting __str__ """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        """ Setting size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ def update """
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
    def to_dictionary(self):
        """ def dictionary """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
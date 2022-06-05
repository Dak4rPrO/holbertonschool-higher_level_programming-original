#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ class rectangle """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ def init """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def height(self):
        """ property height """
        return self.__height

    @height.setter
    def height(self, value):
        """ def height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ property width """
        return self.__width

    @width.setter
    def width(self, value):
        """ def width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def x(self):
        """ property x """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ def x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ property y """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ def y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """ def area """
        return self.__width * self.__height
    
    def display(self):
        """ def display """
        """ string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                string += "\n"
        print(string[:-1])"""
        
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
    
    def __str__(self):
        """ def str """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}")
    
    def update(self, *args, **kwargs):
        """ def update """         
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:                
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:                  
                    self.__x = arg
                elif i == 4:                    
                    self.__y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

#!/usr/bin/python3
""" class Student that defines a student by """


class Student:
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ def init """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ def attrs """

        if attrs == None:
            return(vars(self))
        else:
            return self.__dic__

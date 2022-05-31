#!/usr/bin/python3
""" function that writes a string to a text file and returns
    the number of characters written"""


def write_file(filename="", text=""):
    """ prototype write_file """

    with open(filename, encoding="UTF-8", mode="w") as f:
        return(f.write(text))

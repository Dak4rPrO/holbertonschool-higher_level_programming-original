#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added """


def append_write(filename="", text=""):
    """ prototype append_write """

    with open(filename, encoding="UTF-8", mode="a") as file:
        return(file.write(text))

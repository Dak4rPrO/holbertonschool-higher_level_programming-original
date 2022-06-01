#!/usr/bin/python3
""" function that divides 2 integers and prints the result """


def safe_print_division(a, b):
    """ def division"""

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

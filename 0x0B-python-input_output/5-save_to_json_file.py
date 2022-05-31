#!/usr/bin/python3
""" function that writes an Object to a text file,
    using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ prototype save_json """

    with open(filename, encoding="UTF-8", mode="w") as f:
        json.dump(my_obj, f)

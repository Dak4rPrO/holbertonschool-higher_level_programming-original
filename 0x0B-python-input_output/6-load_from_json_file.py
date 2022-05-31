#!/usr/bin/python3
""" function that creates an Object from a “JSON file” """


import json


def load_from_json_file(filename):
    """ prototype load_json """

    with open(filename, mode="r", encoding="UTF-8") as f:
        return (json.load(f))

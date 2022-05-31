#!/usr/bin/python3
""" script that adds all arguments to a Python list,
    and then save them to a file """

import json, sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    file = load_from_json_file("add_item.json")
except:
    file = []

file_name = "add_item.json"
for argc in range(1, len(sys.argv)):
    file.append(sys.argv[argc])
save_to_json_file(file, file_name)

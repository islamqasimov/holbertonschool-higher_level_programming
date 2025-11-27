#!/usr/bin/python3
"""
JSON representation module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that saves JSON string to a file
    """

    with open(filename, "w", encoding='UTF-8') as file:
        file.write(json.dumps(my_obj))

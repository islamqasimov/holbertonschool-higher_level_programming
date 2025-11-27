#!/usr/bin/python3
"""
JSON representation module
"""


import json


def load_from_json_file(filename):
    """
    Function that loads from JSON file
    """

    with open(filename, "r", encoding='UTF-8') as file:
        return json.loads(file.read())

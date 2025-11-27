#!/usr/bin/python3
"""
JSON representation module
"""


import json


def from_json_string(my_str):
    """
    Function to return JSON string
    """

    return json.loads(my_str)

#!/usr/bin/python3
"""
Basic serialization module
"""


import json

def serialize_and_save_to_file(data, filename):
    """
    Serialization function
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(data))
    

def load_and_deserialize(filename):
    """
    Deserialization function
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        return json.loads(file.read())

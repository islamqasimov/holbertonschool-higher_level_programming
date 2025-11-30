#!/usr/bin/python3
"""
Module to work with CSV and JSON files
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    Converting CSV files to JSON
    """
    try:
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            with open('data.json', 'w') as json_file:
                data = json.dumps([dct for dct in reader])
                json_file.write(data)
        return True
    except FileNotFoundError:
        return False
         

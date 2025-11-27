#!/usr/bin/python3
"""
Testing script that adds arguments to json file
"""

import sys

if __name__ == "__main__":
    save_to_json_f = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_f = __import__('6-load_from_json_file').load_from_json_file
    filename = 'add_item.json'
    args = sys.argv[1:]
    try:
        content = load_from_json_f(filename)
        save_to_json_f(content + args, filename)
    except FileNotFoundError:
        save_to_json_f(args, filename)

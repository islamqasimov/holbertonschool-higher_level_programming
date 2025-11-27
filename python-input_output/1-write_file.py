#!/usr/bin/python3
"""
Module to write file
"""


def write_file(filename='', text=''):
    """
    Function that writes or creates file
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(text)
    return len(text)

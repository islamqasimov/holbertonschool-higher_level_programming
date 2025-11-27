#!/usr/bin/python3
"""
Module to append file
"""


def append_write(filename='', text=''):
    """
    Function that appends or creates file
    """

    with open(filename, 'a', encoding='UTF-8') as file:
        file.write(text)
    return len(text)

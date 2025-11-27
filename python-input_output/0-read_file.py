#!/usr/bin/python3
"""
Module to read and print out a file
"""


def read_file(filename=""):
    """
    Function to read and print out a file
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end='')

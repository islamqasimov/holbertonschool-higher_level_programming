#!/usr/bin/python3
"""
Module for defining Student
"""


class Student:
    """
    Class that represents student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dct = self.__dict__
        if attrs is not None:
            output = {}
            for at in attrs:
                if at in dct.keys():
                    output[at] = dct[at]
            return output
        return dct

    def reload_from_json(self, json):
        for key, value in json.items():
            self.key = value
        
        

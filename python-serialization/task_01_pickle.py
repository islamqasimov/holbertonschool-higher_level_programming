#!/usr/bin/python3
"""
Class s&des|erialization
"""


import pickle


class CustomObject:
    """
    Custom Class
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {self.name}")
        print("Age: {self.age}")
        print("Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None

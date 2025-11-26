#!/usr/bin/python3
"""
List module inheritance
"""


class MyList(list):
    """
    List child class, with extra print sorted method
    """
    def print_sorted(self):
        print(sorted(self))

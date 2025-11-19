#!/usr/bin/python3
def no_c(string):
    new_string = ''
    for i in string:
        if i not in 'cC':
            new_string += i
    return new_string

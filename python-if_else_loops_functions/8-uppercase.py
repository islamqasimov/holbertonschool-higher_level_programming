#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ''

    for char in str:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char

    return uppercase_str

#!/usr/bin/python3
def islower(c):
    if ord(c) == ord(c.lower()) and not c.isdigit():
        return True
    else:
        return False

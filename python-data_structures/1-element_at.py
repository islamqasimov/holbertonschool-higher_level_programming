#!/usr/bin/python3
def element_at(lst, index):
    return lst[index] if len(lst) > abs(index) else None

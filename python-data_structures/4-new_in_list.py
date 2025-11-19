#!/usr/bin/python3
def new_in_list(lst, i, ne):
    if i < 0 or i >= len(lst):
        return lst.copy()
    new_list = lst.copy()
    new_list[i] = ne
    return new_list

#!/usr/bin/python3
def element_at(lst, index):
    if index < 0:
        # negative index is valid only if within -len(lst) to -1
        if index >= -len(lst):
            return lst[index]
        else:
            return None
    else:
        # non-negative index must be < len(lst)
        if index < len(lst):
            return lst[index]
        else:
            return None

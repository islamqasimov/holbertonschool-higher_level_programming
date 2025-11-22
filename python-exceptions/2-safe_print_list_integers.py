#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            el = my_list[i]
            if type(el) == type(5):
                print(el, end='')
                counter += 1
        print()
    except (ValueError, TypeError, IndexError):
        print()
        return counter
    return counter

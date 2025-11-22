#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            el = my_list[i]
            if isinstance(el, int):
                print("{:d}".format(el), end='')
                counter += 1
        print()
    except (ValueError, TypeError):
        print()
        return counter
    return counter

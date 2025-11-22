#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result_list = [] #list(map(lambda x, y: x / y, my_list_1, my_list_2))
        itarables_list = list(zip(my_list_1, my_list_2))
        for i in range(list_length):
            try:
                div = itarables_list[i][0] / itarables_list[i][1]
                result_list.append(div)
            except ZeroDivisionError:
                result_list.append(0)
                print('division by 0')
            except TypeError:
                result_list.append(0)
                print('wrong type')
    except IndexError:
        result_list.append(0)
        print('out of range')
    finally:
        return result_list
    
    

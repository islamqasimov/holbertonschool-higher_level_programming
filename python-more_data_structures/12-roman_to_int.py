#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != type(''):
        return 0
    roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
    }
    temp = 0
    result = 0
    count = 1
    for i in range(len(roman_string)):
        num = roman_nums[roman_string[i]]
        if len(roman_string) == 1 or i == len(roman_string) - 1: 
            result += num - temp
            temp = 0
            count = 1
        elif num >= roman_nums[roman_string[i + count]]:
            result += num - temp
            temp = 0
            count = 1
        else:
            count += 1
            temp += num
    return result


#!/usr/bin/python3
print(', '.join("0{0}".format(num) if num < 10 else "{0}".format(num) for num in range(100)))

#!/usr/bin/python3
def print_matrix_integer(matrix):
    for row in matrix:
        for col in row:
            if row[-1] == col:
                print("{:d}".format(col))
            else:
                print("{:d}".format(col), end=' ')


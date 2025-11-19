#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str_matrix = ''
    for row in matrix:
        for col in row:
            if row[-1] == col:
                str_matrix += '{:d}\n'.format(col)
            else:
                str_matrix += '{:d} '.format(col)
    print(str_matrix)

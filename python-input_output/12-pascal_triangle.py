#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Function that creates Pascal Triangle using nums of now (n)
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        current_row = [1]
        prev_row = triangle[i-1]
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j+1])
        current_row.append(1)
        triangle.append(current_row)

    return triangle

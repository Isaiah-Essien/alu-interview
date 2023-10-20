#!/usr/bin/python3
"""This script defines a function to generate Pascal's Triangle up to a given row 'n'."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to row 'n' and return it as a list of lists."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

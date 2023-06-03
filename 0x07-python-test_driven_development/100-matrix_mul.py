#!/usr/bin/python3
"""a function that multiplies 2 matrices """


def matrix_mul(m_a, m_b):
    """ function that multiplies two matric
    Args:
        m_a - first martrix
        m_b - second matrix
    Raises:
        if m_a or m_b is not a list: raise a TypeError
        if m_a or m_b is not a list of lists: raise a TypeError
        if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError
        if one element of those list of lists is not int: raise a TypeError
        if m_a or m_b is not a rectangle raise a TypeError
        If m_a and m_b can’t be multiplied: raise a ValueError
    Return:
        multiplies matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(sublist, list) for sublist in m_a or []):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(sublist, list) for sublist in m_b or []):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    row_size_a = len(m_a[0])
    if any(len(row) != row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if any(len(row) != row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        matrix1.append(my_row)

    matrix2 = []
    for row in m_a:
        my_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        matrix2.append(my_row)

    return matrix2

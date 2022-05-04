#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for x in range(len(matrix)):
        square = map(lambda x: x * x, matrix[x])
        copy_matrix.append(list(square))
    return copy_matrix

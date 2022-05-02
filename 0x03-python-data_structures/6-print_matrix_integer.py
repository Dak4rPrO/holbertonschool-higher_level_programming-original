#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """for fila in range(len(matrix)):
        for columna in range(len(matrix[fila])):
            print(matrix[fila][columna], end=" ")
            if columna < matrix[fila]"""
    for x in matrix:
        print(*x)

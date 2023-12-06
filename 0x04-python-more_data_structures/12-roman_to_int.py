#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lamda y: y**2, x)), matrix)))

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))


# return list(map(lambda row: list(map(lambda n: n**2, row)), matrix))

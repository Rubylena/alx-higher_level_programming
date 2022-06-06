#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for i in range(len(matrix)):

        # for j inside i matrix
        for j in range(len(matrix[i])):

            # print both i and j together
            print("{:d}".format(matrix[i][j]), end="")

            # if j is not the last element then keep space and
            # no new line at end
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")

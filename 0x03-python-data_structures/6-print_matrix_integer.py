#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for length in matrix:
        for width in length:
            print("{:d}".format(width), end="")
        print()

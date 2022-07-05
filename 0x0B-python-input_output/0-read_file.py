#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=''):
    """Print the contents of a UTF8 textfile to stdout."""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")

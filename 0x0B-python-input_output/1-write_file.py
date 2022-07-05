#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename='', text=''):
    """Writes a string to UTF8 text file"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

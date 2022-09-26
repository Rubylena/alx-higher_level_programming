#!/usr/bin/python3
"""initialize"""
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


def post():
    """post values to a url and get error code"""
    url = argv[1]

    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: '.format(e.code))


if __name__ == '__main__':
    post()

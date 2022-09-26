#!/usr/bin/python3
"""initialize"""
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from sys import argv


def post():
    """post values to a url"""
    url = argv[1]
    value = {'email': argv[2]}

    data = urlencode(value).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    post()

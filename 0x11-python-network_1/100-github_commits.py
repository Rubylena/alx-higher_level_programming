#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


def get_commits():
    """display Github id"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    print(url)
    req = requests.get(url)
    json = req.json()

    for i in range(0, 10):
        sha = json[i].get('sha')
        author = json[i].get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))


if __name__ == '__main__':
    get_commits()

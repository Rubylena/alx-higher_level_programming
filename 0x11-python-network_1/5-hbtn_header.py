#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


req = requests.get(argv[1])
print(req.headers.get('X-Request-Id'))

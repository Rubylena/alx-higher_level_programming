#!/usr/bin/python3
"""initialize"""
import requests
from sys import argv


req = requests.get(argv[1])
code = req.status_code
if(code == 200):
    print(req.text)
else:
    print('Error code: ', req.status_code)

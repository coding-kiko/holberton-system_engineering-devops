#!/usr/bin/python3
"""0. Gather data from an API"""

from sys import argv
import requests

id = argv[1]

r = requests.get('https://jsonplaceholder.typicode.com/todos')
print(r.json())

#!/usr/bin/python3
"""0. Gather data from an API"""

from sys import argv
import requests

id = argv[1]
r = requests.get('https://jsonplaceholder.typicode.com/todos')
done = 0
tasks = []
print(type(r.json()[1].get("completed")))
"""
for task in r.json():
    if task.get('userId') == id:
        tasks.append(task.get('title'))
        if task.get('completed') == "true"
        """

#!/usr/bin/python3
"""0. Gather data from an API"""

from sys import argv
import requests
import json

id = int(argv[1])
r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
users = requests.get('https://jsonplaceholder.typicode.com/users').json()
tasks = []
data = {}
filename = argv[1] + ".json"

data[argv[1]] = []

for user in users:
    if user.get("id") == id:
        username = user.get("username")
        break

for task in r:
    if task.get("userId") == id:
        temp = {"task": task.get("title"), "completed": task.get("completed"), "username": username}
        data[argv[1]].append(temp)

with open(filename, 'w') as f:
    json.dump(data, f)
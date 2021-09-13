#!/usr/bin/python3
"""0. Gather data from an API"""

from sys import argv
import requests
import csv

id = int(argv[1])
r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
users = requests.get('https://jsonplaceholder.typicode.com/users').json()
tasks = []
filename = argv[1] + ".csv"

for user in users:
    if user.get("id") == id:
        username = user.get("username")
        break

with open(filename, mode='w') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for task in r:
        if task.get("userId") == id:
            w.writerow([argv[1], username, task.get("completed"), task.get("title")])

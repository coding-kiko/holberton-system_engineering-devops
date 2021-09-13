#!/usr/bin/python3
"""0. Gather data from an API"""

from sys import argv
import requests

id = int(argv[1])
r = requests.get('https://jsonplaceholder.typicode.com/todos')
done = 0
tasks = []
total = 0
j = r.json()
name = "joaquin"

for task in j:
    if task.get("userId") == id:
        if task.get("completed"):
            tasks.append(task.get("title"))
            done += 1
        total += 1

print("Employee {} is done with tasks({}/{}):".format(name, done, total))
for task in tasks:
    print("\t {}".format(task))

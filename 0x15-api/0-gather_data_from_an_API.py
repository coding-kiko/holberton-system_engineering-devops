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

for task in j:
    if task.get("userId") == 1:
        tasks.append(task.get("title"))
        if task.get("completed"):
            done += 1
        total += 1

print("{}  -   {}/{}".format(tasks, done, total))

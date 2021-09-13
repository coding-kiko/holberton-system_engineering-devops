#!/usr/bin/python3
"""0. Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    usernames = {}

    for u in users:
        usernames[str(u.get("id"))] = u.get("username")

    for task in r:
        if str(task.get("userId")) not in data:
            data[str(task.get("userId"))] = []
        data[str(task.get("userId"))].append({
                                            "task": task.get("title"),
                                            "completed": task.get("completed"),
                                            "username": usernames.get(
                                                str(task.get("userId")))
                                            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)

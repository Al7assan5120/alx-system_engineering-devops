#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{sys.argv[1]}").json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [task.get('title') for task in todos if task.get('completed')]
    print(f"Employee {user.get('name')} is done with tasks("
          f"{len(completed)}/{len(todos)}):")
    for task in completed:
        print(f"\t{task}")

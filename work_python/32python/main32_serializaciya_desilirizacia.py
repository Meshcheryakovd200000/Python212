# модуль requests
import csv
import json

# pip install requests

import requests

# копируем https://jsonplaceholder.typicode.com/todos

response = requests.get("https://jsonplaceholder.typicode.com/todos")

print(type(response.text))

print(response.text)

todos = json.loads(response.text)


todos_by_user = {}
for todo in todos:  # todos - список словарей
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1
print(todos_by_user)
# .........


# csv

with open('data.csv') as f:
    file_reader = csv.reader(f, delimiter =",")
    print(file_reader)


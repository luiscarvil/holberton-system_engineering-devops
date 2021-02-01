#!/usr/bin/python3
"""
send data from a cvs file and create
"""
import requests
import json
import csv
from sys import argv

if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    employee_id = argv[1]

    req_todos = requests.get(url_todos, params={'userId': employee_id}).json()
    name_users = (requests.get(
        url_users, params={'id': employee_id}).json())[0].get('name')
    filename = employee_id + ".csv"
    with open(filename, mode='w') as file_csv:
        writer = csv.writer(file_csv, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for obj in req_todos:
            if obj.get('userId') == int(employee_id):
                writer.writerow([employee_id,
                                name_users, str(obj.get('completed')),
                                 obj.get('title')])

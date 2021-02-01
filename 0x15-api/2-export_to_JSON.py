#!/usr/bin/python3
"""
send data from a cvs file and create
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    employee_id = argv[1]

    req_todos = requests.get(url_todos, params={'userId': employee_id}).json()
    name_users = (requests.get(
        url_users, params={'id': employee_id}).json())[0].get('username')
    new_list = []
    user_list_todo = {}
    with open("{}.json".format(employee_id), mode="w") as jsonfile:
        for obj in req_todos:
            json_dict = {}
            json_dict['task'] = obj.get('title')
            json_dict['completed'] = obj.get('completed')
            json_dict['username'] = name_users
            new_list.append(json_dict)
        user_list_todo[employee_id] = new_list
        data_json = json.dumps(user_list_todo)
        jsonfile.write(data_json)
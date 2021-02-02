#!/usr/bin/python3
"""
send data from a json file and create the file for all users
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    employee_id = 1
    all_list_users = requests.get(url_users).json()
    user_list_todo = {}

    for employee_id in range(1, len(all_list_users) + 1):
        req_todos = requests.get(url_todos,
                                 params={'userId': employee_id}).json()
        name_users = (requests.get(
            url_users, params={'id': employee_id}).json())
        new_list = []
        employee = name_users[0].get('username')
        for obj in req_todos:
            json_dict = {}
            json_dict['username'] = employee
            json_dict['task'] = obj.get('title')
            json_dict['completed'] = obj.get('completed')
            new_list.append(json_dict)
        user_list_todo[employee_id] = new_list
    with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(user_list_todo, jsonfile)

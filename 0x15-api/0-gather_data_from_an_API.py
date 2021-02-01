#!/usr/bin/python3
"""
print data from an api (json file)
"""
import requests
from sys import argv

if __name__ == '__main__':
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    employee_id = argv[1]

    todos_get = requests.get(url_todos, params={'userId': employee_id}).json()
    users_get = (requests.get(
        url_users, params={'id': employee_id}).json())[0].get('name')

    list_true_obj = [obj.get('title') for i, obj in enumerate(todos_get)
                     if todos_get[i].get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        users_get, len(list_true_obj), len(todos_get)))
    for i in list_true_obj:
        print("\t " + i)

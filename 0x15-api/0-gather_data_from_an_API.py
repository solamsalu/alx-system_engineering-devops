#!/usr/bin/python3
"""0. Write  a script using  REST API, for a given employee ID, 
returns information about his/her TODO list progress."""

import requests
from sys import argv


def get_user(id):
    """get the user
    Args:
        id (integer: user id]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users', params={'id': id}).json()
    name = users[0]['name']
    url = 'https://jsonplaceholder.typicode.com/'
    todos = requests.get(url + 'todos', params={'userId': id}).json()
    return([name, todos])


def show(data):
    name = data[0]
    todos = data[1]
    n = 0
    str_to_print = ''
    for task in todos:
        if task['completed'] is True:
            n += 1
            str_to_print += '\t ' + task['title'] + '\n'
    print('Employee {} is done with tasks({}/{}):'.format(name, n, len(todos)))
    print(str_to_print, end='')


if __name__ == '__main__':
    data = get_user(argv[1])
    show(data)

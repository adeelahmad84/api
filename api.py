#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           api.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    API script.
"""

import requests
import json
import unittest

def main():
    def _url(path):
            return 'https://todo.example.com' + path

    response = requests.get('https://todolist.example.com/tasks/')
    if response.status_code != 200:
    # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(response.status_code))

    print(response.status_code)
    data = response.json()

if __name__ == '__main__':
        import doctest
        doctest.testmod()
        main()
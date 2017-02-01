#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           api.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    API script.
"""

from __future__ import print_function
import doctest
#import json
#import unittest
import requests
import fresh

def main():
    """
    This module will liaise the Fresh Service Desk API.
    """


    response = fresh.get_tickets
    if response.status_code != 200:
    # This means something went wrong.
        raise requests.HTTPError('GET /tasks/ {}'.format(response.status_code))

    print(response.status_code)
    #data = response.json()

if __name__ == '__main__':
    doctest.testmod()
    main()

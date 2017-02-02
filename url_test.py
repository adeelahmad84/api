#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           scraping.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Web Scraping script.
"""

import doctest
from time import sleep
import requests

def main():
    """
    Retrieve all teh URLs needed.
    """
    with open('urls.txt') as urls:
        try:
            for url in urls:
                get_urls = []
                get_urls.append(url)

                for rest_url in get_urls:
                    response = requests.get(rest_url)
                    sleep(10)
                    if response.status_code != 200:
                        print "[ERROR] when calling " + rest_url + \
                                                            " got back HTTP response code: " + \
                                                            str(response.status_code)
                    else:
                        print "[SUCCESS] when calling " + rest_url + "."

        except requests.exceptions.ConnectionError:
            response.status_code = "Connection refused"

if __name__ == '__main__':
    doctest.testmod()
    main()

#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           scraping.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Web Scraping script.
"""

import urllib2
from bs4 import BeautifulSoup
import unittest

def main():
    events = "http://kb.eventtracker.com/evtpass/results.asp"
    page = urllib2.urlopen(events)
    soup = BeautifulSoup(page, "html.parser")

    all_links=soup.find_all("a")
    print all_links
    for links in all_links:
        print links.get("href")

if __name__ == '__main__':
        import doctest
        doctest.testmod()
        main()
#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           fresh.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Script to define low-level URL destination.
"""

import os
import requests

def _url(path):
    return os.environ.get('FRESH_URL') + path
    """
    Just adding the URL and its relative path
    """

def get_tickets():
    """
    Retrieve Tickets.
    """
    return requests.get(_url('/helpdesk/tickets/'))


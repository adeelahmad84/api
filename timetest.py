#!/usr/bin/env python
# -- coding: utf-8 --

__version__ = "0.1"

DOCUMENTATION = """
---
File:           timetest.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    API script.
"""

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

EXAMPLES = '''
- name: Ensure foo is installed.
modulename:
    name: foo
    state: present
'''

RETURN = '''
pass
'''

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from module_utils.basic import AnsibleModule
import unittest
import json

def main():
    """
    This module will liaise the Fresh Service Desk API.
    """
    module = AnsibleModule(
            argument_spec = dict(
                state     = dict(default='present', choices=['present', 'absent']),
                name      = dict(required=True),
                enabled   = dict(required=True, type='bool'),
                something = dict(aliases=['whatever'])
                )
            )




if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )

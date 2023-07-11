#!/usr/bin/python3
# 6-from_json_string.py
# John Mwadime
"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

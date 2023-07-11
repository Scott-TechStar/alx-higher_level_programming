#!/usr/bin/python3
# 3-write_file.py
# John Mwadime
"""
contain the JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)

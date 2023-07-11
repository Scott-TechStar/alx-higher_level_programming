#!/usr/bin/python3
# 7-save_to_json_file.py
# John Mwadime
"""Add all arguments to a Python list and save them to a file."""
import json
import sys

def save_to_json_file(obj, '5-save_to_json_file'):
    with open('5-save_to_json_file', 'w') as file:
        json.dump(obj, file)

def load_from_json_file('6-load_from_json_file'):
    with open('6-load_from_json_file') as file:
        return json.load(file)

# Load existing list from file if it exists, otherwise create an empty list
try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

# Add all arguments to the list
existing_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(existing_list, 'add_item.json')

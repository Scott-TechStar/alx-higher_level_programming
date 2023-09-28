#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers, left, right):
    """Return a peak in a list of unsorted integers."""
    if left == right:
        return list_of_integers[left]

    mid = (left + right) // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak(list_of_integers, left, mid)
    else:
        return find_peak(list_of_integers, mid + 1, right)

def find_peak_wrapper(list_of_integers):
    if not list_of_integers:
        return None
    return find_peak(list_of_integers, 0, len(list_of_integers) - 1)


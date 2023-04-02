#!/usr/bin/python3
"""
Find Peak task 6
"""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    peak = binary_search(list_of_integers, 0, size - 1)
    return list_of_integers[peak]

def binary_search(a, lo, hi):
    """Recursive binary search of the peak"""
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)

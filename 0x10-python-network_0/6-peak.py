#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers is None or list_of_integers == []:
        return None

    def recursive_search(lo, hi):
        if lo == hi:
            return list_of_integers[lo]
        mid = (hi + lo) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return recursive_search(mid + 1, hi)
        else:
            return recursive_search(lo, mid)

    return recursive_search(0, len(list_of_integers) - 1)


#!/usr/bin/python3

"""
This function finds the peak in a list of unsorted integers as required.
"""


def find_peak(list_of_integers):
    """
    Returns the peak of the list_of_integers or None.
    """
    
    length = len(list_of_integers)
    mid_element = length
    mid = length // 2

    if length == 0:
        return None

    while True:
        mid_element = mid_element // 2
        
        if (mid < length - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_element // 2 == 0:
                mid_element = 2
            mid = mid + (mid_element // 2)
        
        elif mid_element > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_element // 2 == 0:
                mid_element = 2
            mid = mid - mid_element // 2
        
        else:
            return list_of_integers[mid]

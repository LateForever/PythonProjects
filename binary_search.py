# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:35:42 2021

@author: student
"""

def binary_search(array, searchnumber):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid_index = (left + right) // 2
        mid_number = array[mid_index]
        if mid_number == searchnumber:
            print(f"{mid_number} found at {mid_index} position")
            return True
        else:
            if mid_number < searchnumber:
                left = mid_index
            else:
                right = mid_index
    else:
        print("Nie ma takiego elementu")


tab = [1,2,3,4,9,11,19,32,42,56,78,122,189]

binary_search(tab, 78)


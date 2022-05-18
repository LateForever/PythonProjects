# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:20:09 2021

@author: student
"""
def binary_search(arr, left, right, target):
    mid_index = (left + right) // 2
    mid_number = arr[mid_index]
    
    if left <= right:
        if  mid_number == target:
            return mid_index
        if mid_number < target:
            return binary_search(arr, mid_index, (right-left),target)
        elif mid_number > target:
            return binary_search(arr, left, mid_index, target)
    else:
          return -1
    
tab = [1,2,3,4,9,11,19,32,42,56,78,122,189]
find_number = 56

a = binary_search(tab, 0, len(tab)-1, 57)
print(a)



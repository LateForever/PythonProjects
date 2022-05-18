# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:54:04 2021

@author: David
"""
def binary_search(ar, target):
    left = 0
    right = len(ar)-1
    index = 0
    while left <= right:
        mid_index = (left+right)//2
        mid_number = ar[mid_index]
        if target == mid_number:
            print(f"{mid_number} found at {mid_index} position")
            return True
        elif target > mid_number:
            left = mid_index
        elif target < mid_number:
            right = mid_index
            

tab = [1,2,3,4,9,11,19,32,42,56,78,122,189]
binary_search(tab, 9)
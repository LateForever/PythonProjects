# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:25:27 2021

@author: student
"""

t = [2,9,7,1,8,14,17]

def bubble_sort(t):
    n = len(t)
    for i in range(n):
        for j in range(0, n-i-1):
            print(t)
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
                print(t)
        
bubble_sort(t)

for i in range(len(t)):
    print(t[i])
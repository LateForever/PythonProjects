# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:17:15 2021

@author: student
"""
from functools import cpm_to_key

tab = [("kwadrat", 2), ("kolko", 3), ("trojkat", 4), ("kwadrat", 1)]

weight = {"kwadrat": 1,
           "trojkat": 2,
           "kolko": 3}

def compare(item1, item2):
    if weight[item1[0]] < weight[item2[0]]:
        return -1
    elif weight[item1[0]] > weight[item2[0]]:
         return 1
    else:
        if item1[1] > item2[1]:
            return 1
        elif item1[1] < item2[1]:
            return -1
        else:
            return 0
        
tab.sort(key=cpm_to_key(compare))
        
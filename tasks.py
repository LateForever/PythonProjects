# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:59:02 2021

@author: student
"""

def index_of_caps(word):
    t = []
    t_index = []
    for i in word:
        t.append(i)
    x = 0
    for i in t:
        if str.isupper(i):
            t_index.append(x)
            x += 1
        else:
            x += 1
    return (t_index)
            
a = index_of_caps("eDaBiT")
b = index_of_caps("eQuINoX")
c = index_of_caps("determine")
d = index_of_caps("STRIKE")
e = index_of_caps("sUn")
print(a,b,c,d,e)

def is_curzon(num):
    a = 2 ** num + 1
    b = 2 * num + 1
    if a % b == 0:
        return (f"{a} is a multiple of {b}")
    else:
        return (f"{a} is not a multiple of {b}")

f = is_curzon(5) 
g = is_curzon(10) 
h = is_curzon(14)

print(f) 
print(g)
print(h)


    











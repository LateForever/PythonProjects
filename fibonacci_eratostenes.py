# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:29:29 2021

@author: student
"""

import math

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    print(n-1+n-2)
    return fib(n-1) + fib(n-2)

x = fib(9)
print(x)

def fib2(n):
    t = [1,1]
    for i in range(n-2):
        t.append(t[i] + t[i+1])
        print(t)

fib2(9)

def fib3(n, l1, l2):
    if n-1 > 0:    
        print(l1 + l2)
    else:
        return
    return fib3(n-1, l2 ,l1+l2)

p = fib3(8,0,1)
print(p)
    
def eratostenes(a,n):
    t = []
    tt = True
    tf = False
    tab = []
    for i in range(a,n+1):
        t.append(i)
    print(t)
    tab = [tt] * (n+1)
    tab[0] = tab[1] = False
    
    for i in range(a,int(math.sqrt(t[-1]))+1):
        for j in range(i,len(t)+1,i):
            if j != i: 
                tab[j] = tf

    print(tab)
    
    c = []
    counter = 2
    for i in tab[2:]:
        if i == True:
            c.append(counter)
        print(counter,i)
        counter+= 1

    c = c[:-1]
    print(c)
   
eratostenes(2,200)
    
    
    
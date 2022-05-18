# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:27:56 2021

@author: student
"""

def sito(n):
    temp = [1 for x in range(n+1)]
    print(temp)
    print(len(temp))
    for i in range(2,n+1):
        for j in range(i+1,n+1):
            if j%i == 0:
                temp[j] = 0
                
    print(len(temp))
    print(temp)
    primes = []
    for i in range(2,len(temp)):
        if temp[i] == 1:
            primes.append(i)
            
    print(primes)
    return primes
        
sito(200)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:50:06 2021

@author: student
"""


def mergeSort(t):
    if len(t) > 1:
        mid = len(t)//2
        
        L = t[:mid]
        P = t[mid:]
        print(f"Lewa tablica {L}")
        print(f"Prawa tablica {P}")
        mergeSort(L)
        mergeSort(P)
        
        print("\n\n\n\n\n")
        
        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i] > P[j]:
                t[k] = P[j]
                j += 1
            else:
                t[k] = L[i]
                i += 1
            print(t)
            k += 1
        
        while i < len(L):
            t[k] = L[i]
            i += 1
            k += 1
            
        while j < len(P):
            t[k] = P[j]
            j += 1
            k += 1
            
        print(t)
        
t = [12, 11, 13, 5, 6, 7, 5, 1, 31, 8, 1, 2, 0, 41]
mergeSort(t)

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:39:36 2021

@author: student
"""

from functools import cmp_to_key

class Person:
    def __init__(self,family_members, animals):
        self.family_members = family_members
        self.animals = animals
    
person1 = Person(1,3)
person2 = Person(1,2)
person3 = Person(3,1)
person4 = Person(3,0)
person5 = Person(4,5)

tabperson = [person1, person2, person3, person4, person5]

def compare(num1: Person, num2: Person):
    if num1.family_members < num2.family_members:
        return -1
    elif num1.family_members > num2.family_members:
        return 1
    else:
        if num1.animals > num2.animals:
            return -1
        elif num1.animals < num2.animals:
            return 1
        else:
            return 0
        
tabperson.sort(key=cmp_to_key(compare))
for i in tabperson:
    print(i.family_members, i.animals)

            
    
    
        


    
    
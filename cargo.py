# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:24:41 2021

@author: student
"""

cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort(reverse= True)
boxCapacity = 90
box = []
i = 0


while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
    print(len(cargo))
    print(box)
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i += 1

print("The collected items sum is: ", sum(box))
print("The element are: ", box)



# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:09:47 2021

@author: student
"""
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def compare(el1, el2):
   if el1[0] > el2[0]:
       return 1
   elif el1[0] < el2[0]:
       return -1
   else:
       if el1[1] > el2[1]:
           return 1
       elif el1[1] < el2[1]:
           return -1
       else:
           return 0

n = int(input())
arr = []
nr = 1
while n!=0:
    t,d = input().split()
    arr.append([int(t),int(d),nr])
    nr += 1
    n-=1

arr.sort(key=cmp_to_key(compare))
resultarr = []

daynumber = 1
while arr:  
    if arr[0][0] + daynumber -1 <= arr[0][1]:
        resultarr.append([arr[0][2], daynumber])
        daynumber += arr[0][0]
        arr.pop(0)
    else:
        arr.pop(0)
        
print(len(resultarr))
for i in resultarr:
    print(i[0],i[1])

    
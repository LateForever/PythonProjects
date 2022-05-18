b# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:27:50 2021

@author: student
"""


values = [10,43,12,18,19,24,27,29,30,31,34,40,67,80,90]

max = len(values) - 2

i = 0
while i < max:
    print(i, values[i],values[i + 1], values[i + 2])
    
    if(values[i] < values[i + 1] and values[i + 1] < values[i + 2]):
        print('\tFound: ',values[i],values[i + 1], values[i + 2] )
    i += 1

def euler_number(number):
       e =  (1 + (1/number))** number
       print(e)

euler_number(8888)

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
max = len(numbers)

i = 0
while i < max:
    last_index = len(numbers) - 1
    print(i, numbers[i])
    if (i == last_index):
        break
    if (numbers[i + 1] == numbers[i]**2):
        print('\tFound: ',numbers[i], numbers[i + 1])
    i += 1  
    
print('End')

'''

'''
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
max_numbers = len(numbers)
print(max_numbers)
i = 0
while i < max_numbers:
    last_index = max_numbers - 3
    print(i, numbers[i], numbers[i+1], numbers[i + 2])
    if (i == last_index):
        break
    if (numbers[i]**2 == numbers[i + 1] and numbers[i + 1]**2 == numbers[i + 2]):
        print(f'\tFound: {numbers[i]} {numbers[i+1]} {numbers[i+2]}')
    i += 1
print('End')

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
max_texts = len(texts)
print(max_texts)
i = 0
while i < max_texts:
    last_index = max_texts - 2
    print(i, texts[i], texts[i + 1])
    if (i == last_index):
        break
    if (len(texts[i]) == len(texts[i+1])):
        print(f'\tFound: {texts[i]} {texts[i + 1]}')
    i += 1
print('End')


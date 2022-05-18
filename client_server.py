# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:31:42 2021

@author: student
"""

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20189))
tm = s.recv(1024)
s.close()
print('Czas serwera: ', tm)
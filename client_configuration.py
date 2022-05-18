# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:13:31 2021

@author: student
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.httpbin.org', 80))
s.sendall('GET /html HTTP/1.1\r\nHost: httpbin.org\r\n\r\n'.encode('utf-8'))
data = b''

while b'\r\n\r\n' not in data:
    data += s.recv(100)
    
contentlength = int(data.decode('utf-8').split('Content-Length: ')[1].split('\r\n')[0])

header_lenght = len(data.decode('utf-8').split('\r\n\r\n')[0])

while len(data) < contentlength + header_lenght:
    data += s.recv(100)

print('Content length =', (contentlength))
     

data = data.decode('utf-8')
resp = data.split('\r\n\r\n')
    
b = resp[0].split('\r\n')
c = resp[1].split()

with open('index.html', 'w') as f:
    f.write(resp[1])

start = resp[1].find("<p>") + len("<p>")
end = resp[1].find("</p>")
substring = resp[1][start:end]
print(substring)

s.close()
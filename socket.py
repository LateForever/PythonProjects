import socket as s

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM) #utworzenie gniazda
s.bind(('localhost', 20189)) #dowiazanie portu 8888
s.listen(5)

while 1:
    client, adrr = s.accept() #odebraine polaczenia
    print("Polaczenie z ", adrr) 
    client.send('Hello World')
    client.close()
    
    
#-- coding: utf-8--
#echo_client.py


import socket
import datetime



host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))
tekst = raw_input("upisite tekst za slanje serveru")
client_socket.sendall(tekst)

data = client_socket.recv(1024)
print data
client_socket.close()
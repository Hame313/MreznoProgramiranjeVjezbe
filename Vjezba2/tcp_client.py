#tcp_client.py

import socket

client_socket = socket.socket()
host = socket.gethostname()

port = 9999
#Linija koda client_socket.connect((host,port)) se konektuje na odredjeni host i port.
client_socket.connect ((host, port))
print client_socket.recv(1024)

client_socket.close()

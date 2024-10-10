import sys
from socket import *

fileName = sys.argv[1]
name = 'hostname'
port = 50001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((name, port))

with open(fileName, 'r') as file:
    for line in file:
        clientSocket.send(line.encode())
        result = clientSocket.recv(1024).decode()

clientSocket.close()
    



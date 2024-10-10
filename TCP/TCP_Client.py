import sys
from socket import *

fileName = sys.argv[1]
name = "localhost"
port = 50001

with open(fileName, 'r') as file:
    for line in file:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((name, port))
        clientSocket.send(line.encode())
        result = clientSocket.recv(1024).decode()

clientSocket.close()
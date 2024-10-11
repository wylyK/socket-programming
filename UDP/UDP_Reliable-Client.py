import sys
from socket import *

if len(sys.argv) < 2:
    print("Expecting input file!")
    exit()


fileName = sys.argv[1]
name = "localhost"
port = 50001

with open(fileName, 'r') as file:
    for line in file:
        line = line.strip()
        print("Input request: " + line)
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.sendto(line.encode(), (name, port))
        extendedResult, _ = clientSocket.recvfrom(1024)
        statusCode, result = extendedResult.decode().split(" ")

        match statusCode:
            case "200":
                print("The result is: " + result)
            case "620":
                print("Error " + statusCode + ": Invalid operator!")
            case "630":
                print("Error " + statusCode + ": Invalid operands!")

        clientSocket.close()
import sys
from socket import *

if len(sys.argv) < 2:
    print("Expecting input file!")

else:
    fileName = sys.argv[1]
    name = "localhost"
    port = 50001

    with open(fileName, 'r') as file:
        for line in file:
            
            line = line.strip()
            print("Input request: " + line)
            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.connect((name, port))
            clientSocket.send(line.encode())
            extendedResult = clientSocket.recv(1024).decode()
            statusCode, result = extendedResult.split(" ")

            match statusCode:
                case "200":
                    print("The result is: " + result)
                case "620":
                    print("Error " + statusCode + ": Invalid operator!")
                case "630":
                    print("Error " + statusCode + ": Invalid operands!")

            clientSocket.close()
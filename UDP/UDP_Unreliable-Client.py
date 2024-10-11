import sys
from socket import *

if len(sys.argv) < 2:
    print("Expecting input file!")
    exit()

fileName = sys.argv[1]
name = "localhost"
port = 50001
statusCode = "200"

with open(fileName, 'r') as file:
    for line in file:
        line = line.strip()
        d = 0.1
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        while True:
            clientSocket.sendto(line.encode(), (name, port))
            clientSocket.settimeout(d)

            try: 
                extendedResult, _ = clientSocket.recvfrom(1024)
                statusCode, result = extendedResult.decode().split(" ")
                clientSocket.settimeout(None)
                break

            except timeout:
                d = 2 * d
                if d > 2:
                    print("Request timed out: the server is DEAD")
                    statusCode = "300"
                    break
                else:
                    print("Request timed out: resending")

        match statusCode:
            case "200":
                print("The result is: " + result)
            case "300":
                print("Error " + statusCode + ": Server is DEAD!")
            case "620":
                print("Error " + statusCode + ": Invalid operator!")
            case "630":
                print("Error " + statusCode + ": Invalid operands!")

        clientSocket.close()
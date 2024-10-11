import sys
import random
from socket import *

if len(sys.argv) == 1:
    print("Expecting numeric probability and seed!")
    exit()

elif len(sys.argv) == 2:
    print("Expecting seed!")
    exit()

p = float(sys.argv[1])
random.seed(sys.argv[2])

def calculate(expression):
    expression = expression.split()
    operator = expression[0]

    statusCode = "200"
    result = "-1"

    try:
        x = int(expression[1])
        y = int(expression[2])
    except:
        x = 1
        y = 1
        statusCode = "630"

    match operator:
        case "+":
            result = str(x + y)
        case "-":
            result = str(x - y)
        case "*":
            result = str(x * y)
        case "/":
            if y == 0:
                statusCode = "630"
            else: 
                result = str(x / y)            
        case _:
            result = "-1"
            statusCode = "620"

    if statusCode == "630":
        result = "-1"

    return statusCode, result

def start():
    port = 50001
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", port))
    
    try:
        while True:
            expression, address = serverSocket.recvfrom(1024)
            expression = expression.decode()
            message = ""
            if random.random() <= p:
                message = "dropped"
            else:
                statusCode, result = calculate(expression)
                message = statusCode + " " + result
                serverSocket.sendto(message.encode(), address)

            print(expression + " -> " + message)
    except KeyboardInterrupt:
        print("\nServer Terminated")
        serverSocket.close()

start()
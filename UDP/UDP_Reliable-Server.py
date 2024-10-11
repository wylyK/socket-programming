from socket import *

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
    serverSocket.timeout(0.5)

    try:
        while True:
            try:
                expression, address = serverSocket.recvfrom(1024)
                expression = expression.decode()
                statusCode, result = calculate(expression)
                extendedResult = statusCode + " " + result
                serverSocket.sendto(extendedResult.encode(), address)
                print(expression + " -> " + extendedResult)
            except serverSocket.timeout:
                pass
    except KeyboardInterrupt:
        serverSocket.close()
        

start()
from socket import *
def isntWhiteSpace(letter):
    return letter != ""

def calculate(expression):
    expression = expression.split(" ")
    expression = list(filter(isntWhiteSpace, expression))
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
            statusCode, result = calculate(expression.decode())
            extendedResult = statusCode + " " + result
            serverSocket.sendto(extendedResult.encode(), address)
            print(expression + " -> " + extendedResult)
        
    except KeyboardInterrupt:
        serverSocket.close()

start()
from socket import *

def calculate(expression):
    prefix = expression.split()
    operator = prefix[0]
    x = int(prefix[1])
    y = int(prefix[2])
    result = ""

    match operator:
        case "+":
            result = str(x + y)
        case "-":
            result = str(x - y)
        case "*":
            result = str(x * y)
        case "/":
            result = str(x / y)

    return result

def start():
    port = 50001
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    try:
        while True:
            connectionSocket, _ = serverSocket.accept()
            expression = connectionSocket.recv(1024).decode()
            result = calculate(expression)
            connectionSocket.send(result.encode())
        
    except KeyboardInterrupt:
        serverSocket.close()

start()
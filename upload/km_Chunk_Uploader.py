import os
import json
from socket import *
from datetime import datetime

directory = os.path.dirname(__file__) + "/"
os.chdir(directory)
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    print(str(addr[0]) + " connected")
    message = json.loads(connectionSocket.recv(1024).decode())
    try:
        with open(message["requested_content"], "rb") as file:
            while True:
                bytes_read = file.read(1024)
                if not bytes_read:
                    break
                connectionSocket.sendall(bytes_read)
    except IOError:
        print("Requested chunk could not be found (Did you really delete a chunk?)")

    with open("km_ulog.txt", "a") as log:
        log.write(
            message["requested_content"] + " " + str(datetime.fromtimestamp(datetime.now().timestamp())) + " " + str(
                addr[0]) + "\n")
    connectionSocket.close()

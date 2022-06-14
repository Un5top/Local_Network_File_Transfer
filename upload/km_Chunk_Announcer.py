import os
import math
import time
import json
from socket import *

directory = os.path.dirname(__file__) + "/"
os.chdir(directory)
validFile = False
while not validFile:
    try:
        filename = input("Enter name of file to be hosted (with extension): ")
        x = filename.rfind('.')
        content_name = filename[0:x]
        c = os.path.getsize(filename)
        CHUNK_SIZE = math.ceil(math.ceil(c)/5)
        validFile = True
    except FileNotFoundError:
        print("File does not exist")


index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkName = content_name+'_'+str(index)
        with open(directory + chunkName, 'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))

serverPort = 0
# You may change your broadcast ip in the next line
# 25.255.255.255
broadcastIp = '25.255.255.255'

serverAddress = (broadcastIp, 5001)

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to transmit")

x = {'chunks': []}
for i in range(1, 6):
    x["chunks"].append(content_name + "_" + str(i))
print(x)
y = json.dumps(x)

while 1:
    serverSocket.sendto(y.encode("utf-8"), serverAddress)
    time.sleep(60)

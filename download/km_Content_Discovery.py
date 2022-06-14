import os
import json
from socket import *

serverPort = 5001
directory = os.path.dirname(__file__) + "/"
os.chdir(directory)

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("Listening for chunk hosts")
contentDictionary = {}
if os.path.isfile('km_files.txt'):
    with open('km_files.txt', 'r') as json_file:
        contentDictionary = json.load(json_file)

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("received {} bytes from {}".format(len(message), clientAddress))
    modifiedMessage = json.loads(message.decode("utf-8"))

    for i in range(len(modifiedMessage['chunks'])):

        print(modifiedMessage['chunks'][i])
        if modifiedMessage['chunks'][i] not in contentDictionary:
            contentDictionary[modifiedMessage['chunks'][i]] = []

        if clientAddress[0] not in contentDictionary[modifiedMessage['chunks'][i]]:
            contentDictionary[modifiedMessage['chunks'][i]].append(clientAddress[0])

    with open('km_files.txt', 'w') as outfile:
        json.dump(contentDictionary, outfile)
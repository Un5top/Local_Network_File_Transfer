import os
import json
import sys
import time
from datetime import datetime
from socket import *


class Error(Exception):
    pass


class InvalidFile(Error):
    # Invalid file request
    pass


contentDictionary = {}
directory = os.path.dirname(__file__) + "/"
os.chdir(directory)
try:
    infile = open('km_files.txt', 'r')
    contentDictionary = json.load(infile)
except FileNotFoundError:
    print("There are no chunks available (make sure you already ran Content Discovery)")
    time.sleep(6)
    sys.exit(0)

validFile = False
while not validFile:
    try:
        filenameE = input("Enter name of desired file (File must be in the same folder as the program):")
        x = filenameE.rfind(".")
        filename = filenameE[0:x]
        for i in range(1, 6):
            if filename + "_" + str(i) not in contentDictionary:
                raise InvalidFile
        validFile = True
    except InvalidFile:
        print("No chunk for this file exists")


for i in range(1, 6):
    attempts = 0
    while attempts < len(contentDictionary[filename + "_" + str(i)]):
        try:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            serverPort = 8000
            clientSocket.connect((contentDictionary[filename + "_" + str(i)][attempts], serverPort))
            bruh = {"requested_content": filename + "_" + str(i)}
            message = json.dumps(bruh)
            clientSocket.send(message.encode("utf-8"))
            bytes_read = clientSocket.recv(1024)
            if bytes_read:
                with open(filename + "_" + str(i), "wb") as file:
                    while True:
                        if not bytes_read:
                            break
                        file.write(bytes_read)
                        bytes_read = clientSocket.recv(1024)
                clientSocket.close()
                print(filename + "_" + str(i) + " has been downloaded from " + contentDictionary[filename + "_" + str(i)][attempts])
                with open("km_dlog.txt", "a") as log:
                    log.write(
                        filename + "_" + str(i) + " " + str(
                            datetime.fromtimestamp(datetime.now().timestamp())) + " " + str(
                            contentDictionary[filename + "_" + str(i)][attempts]) + "\n")
                attempts = len(contentDictionary[filename + "_" + str(i)])
            else:
                raise IOError
        except IOError:
            if attempts + 1 == len(contentDictionary[filename + "_" + str(i)]):
                print("Could not receive " + filename + "_" + str(i) + " from any known sources\n" + filenameE + " could not be downloaded")
                time.sleep(6)
                sys.exit()
            else:
                print("Could not receive " + filename + "_" + str(i) + " from " +
                      contentDictionary[filename + "_" + str(i)][attempts] + "")
            attempts = attempts + 1

chunkNames = [filename + '_1', filename + '_2', filename + '_3', filename + '_4', filename + '_5']

with open(filenameE, 'wb') as outfile:
    for chunk in chunkNames:
        with open(chunk, 'rb') as infile:
            outfile.write(infile.read())
        infile.close()
print(filenameE + " has been downloaded")
time.sleep(3)

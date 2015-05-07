# -*- coding: utf-8 -*-

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper()
    unicodeModifiedMessage = modifiedMessage.encode('utf-8')
    serverSocket.sendto(unicodeModifiedMessage, clientAddress)

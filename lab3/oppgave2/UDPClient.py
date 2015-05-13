# -*- coding: utf-8 -*-

# This module acts like a client that
# takes the input (lowercase) and sends it to the server.
# It then recieve the uppercase version of the message
# from the server and prints it

from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message  = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

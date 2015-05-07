# -*- coding: utf-8 -*-

from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

connectionMessage = "Is connection valid?"
clientSocket.sendto(connectionMessage,(serverName, serverPort))
modifiedConnectionMessage, serverAddress = clientSocket.recvfrom(2048)

if modifiedConnectionMessage == "Yes":
	print "Connection valid"
	message  = raw_input('Input lowercase ascii letter:')
	clientSocket.sendto(message,(serverName, serverPort))
	message, serverAddress = clientSocket.recvfrom(2048)

	print modifiedMessage
else:
	clientSocket.close()

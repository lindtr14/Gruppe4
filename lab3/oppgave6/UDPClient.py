# -*- coding: utf-8 -*-

from socket import *

roman_number_1 = raw_input("Insert the first roman number > ")
operator = raw_input("Insert + for addition or - for subtraction > ")
roman_number_2 = raw_input("Insert the second roman number > ")

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(roman_number_1 ,(serverName, serverPort))
clientSocket.sendto(operator ,(serverName, serverPort))
clientSocket.sendto(roman_number_2 ,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print modifiedMessage
clientSocket.close()

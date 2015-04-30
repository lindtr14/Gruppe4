# -*- coding: utf-8 -*-

from socket import *

print "Choose your function:"
print "1: Make lowercase to uppercase"
print "2: Mathematic expression with roman numerals"

alternative = raw_input("> ")

if alternative == "1":
	message = raw_input("Insert the lowercase character: ")
	operator = ""
	roman_number_2 = ""
else:
	message = raw_input("Insert the first roman number > ")
	operator = raw_input("Insert + for addition or - for subtraction > ")
	roman_number_2 = raw_input("Insert the second roman number > ")

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message ,(serverName, serverPort))
clientSocket.sendto(operator ,(serverName, serverPort))
clientSocket.sendto(roman_number_2 ,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print modifiedMessage
clientSocket.close()

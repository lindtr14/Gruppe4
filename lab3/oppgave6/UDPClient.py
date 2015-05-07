# -*- coding: utf-8 -*-

from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2)

looping = True
sending = True
while looping:

	print "Choose your function:"
	print "1: Make lowercase to uppercase"
	print "2: Mathematic expression with roman numerals"
	print "q: Press q to quit"
	
	alternative = raw_input("> ")
	
	if alternative == "1":
		writing = True
		while writing:
			message = raw_input("Insert the lowercase letter: ")
			if message.isalpha() and message.islower():
				writing = False
			else:
				print "Please insert a lowercase letter"
		operator = ""
		roman_number_2 = ""
	elif alternative == "2":
		operating = True
		while operating:
			operator = raw_input("Insert + for addition or - for subtraction > ")
			if operator == "+" or operator == "-":
				operating = False
			else:
				print "Please insert a valid operator"
		writing = True
		while writing:
			message = raw_input("Insert the first roman number > ")
			if message.isalpha() and message.isupper():
				writing = False
			else:
				print "Please insert an uppercase roman numeral"
	
		writing2 = True
		while writing2:
			roman_number_2 = raw_input("Insert the second roman number > ")
			if roman_number_2.isalpha() and roman_number_2.isupper():
				writing2 = False
			else:
				print "Please insert an uppercase roman numeral"
	elif alternative == "q":
		looping = False
		sending = False
	
	if sending:
		clientSocket.sendto(message ,(serverName, serverPort))
		clientSocket.sendto(operator ,(serverName, serverPort))
		clientSocket.sendto(roman_number_2 ,(serverName, serverPort))
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print modifiedMessage
	else:
		clientSocket.close()

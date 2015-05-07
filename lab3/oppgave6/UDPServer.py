# -*- coding: utf-8 -*-

# Remember to have download roman.py in your directory
from socket import *
import roman

    

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve"
while 1:
    message_1, clientAddress = serverSocket.recvfrom(2048)
    operator, clientAddress = serverSocket.recvfrom(2048)
    roman_number_2, clientAddress = serverSocket.recvfrom(2048)
    if message_1[0].isupper() == True:
        if operator == '+':
            message = roman.romanAddition(message_1, roman_number_2)
        elif operator == '-':
            message = roman.romanSubtraction(message_1, roman_number_2)
    else:
        modifiedMessage = message_1.decode('utf-8').upper()
        message = modifiedMessage.encode('utf-8')
    serverSocket.sendto(message, clientAddress)

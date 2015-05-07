# -*- coding: utf-8 -*-

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve"

def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(ord(character))
    
    return outstr

def binaryChange(binary):

	listBinary = list(binary)
	listBinary[2] = "0"
	return "".join(listBinary)

def fromBinaryToText(newBinary):

	return chr(int(newBinary, 2))

def test():
	assert unicodeBin("a") == "01100001"
	assert binaryChange("01100001") == "01000001"
	assert fromBinaryToText("01000001") == "A"

	return "Testene er fullført uten feil"

print test()

loop = True

while loop:
    connectionMessage, clientAddress = serverSocket.recvfrom(2048)
    if connectionMessage == "Is connection valid?":
        positiveMessage = "Yes"
        serverSocket.sendto(positiveMessage, clientAddress)


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    binary = unicodeBin(message)
    newBinary = binaryChange(binary)
    newText = fromBinaryToText(newBinary)
    modifiedMessage = message.decode('utf-8').upper()
    unicodeModifiedMessage = modifiedMessage.encode('utf-8')
    serverSocket.sendto(newText, clientAddress)

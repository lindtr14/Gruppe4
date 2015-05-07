# -*- coding: utf-8 -*-

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve"

def asciiBin(character):

    outstr = ""
    ascii_char = bytearray(character)
    
    if len(ascii_char) > 1:
        for char in bytearray(ascii_char):
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
    assert asciiBin("a") == "01100001"
    assert binaryChange("01100001") == "01000001"
    assert fromBinaryToText("01000001") == "A"

    return "Testene er fullført uten feil"

print test()


def get_binary(number):
    return format(number, 'b').zfill(8)

def set_bit(v, index, x):
    """Set the index:th bit of v to x, and return the new value."""
    mask = 1 << index
    v &= ~mask
    if x:
        v |= mask
    return v

loop = True

while loop:
    connectionMessage, clientAddress = serverSocket.recvfrom(2048)
    if connectionMessage == "Is connection valid?":
        positiveMessage = "Yes"
        serverSocket.sendto(positiveMessage, clientAddress)
        loop = False


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    changed_bin = set_bit(ord(message), 5, 0)   # Gjør om på binærtallet, stor bokstav
    uppercase = chr(changed_bin)    # Gjør om til ascii
    serverSocket.sendto(uppercase, clientAddress)

# -*- coding: utf-8 -*-

# This module acts like the server that
# recieves a message from the client and
# processes it from lowercase to uppercase by turning the
# required bit to make it happen
# It then sends the uppercase version to the client

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve"

def get_binary(number):
    return format(number, 'b').zfill(8)

def set_bit(v, index, x):
    """Set the index:th bit of v to x, and return the new value."""
    mask = 1 << index
    v &= ~mask
    if x:
        v |= mask
    return v
    
def test():
    assert get_binary(97) == "01100001"
    assert ord("a") == 97
    assert set_bit(97, 5, 0) == 65
    assert chr(65) == "A"
    
    return "The test was successful"
    
print test()

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

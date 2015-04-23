# -*- coding: latin-1 -*-

#  IS-105 LAB1

import sys
import psutil

# Group members: 
gruppe = {  'student1': 'Andreas Kjærner-Semb', 
            'student2': 'Linda Tran', \
            'student3': 'Frank William Hansen', \
            'student4': 'Ole Aarsnes', \
            'student5': 'Mikael Kile', \
}

#  Exercise 1
def ascii_fugl():
    print"#       \/"
    print"#       \/_"
    print"#  \,   /( ,/"
    print"#   \\\\\\' ///"
    print"#    \_ /_/"
    print"#    (./"
    print"#     '`"

ascii_fugl()

#  Exercise 2
def bitAnd(x, y): 
	i = (x & y)
    	return i

#  Exercise 3
def bitXor(x, y):
	i = x ^ y
	return i

#  Exercise 4
def bitOr(x, y):
	i = x | y
	return i

#  Exercise 5
def ascii8Bin(letter):
	i = ord(letter)
    	return '{0:08b}'.format(i) 

#  Exercise 6
def transferBin(string):

	l = list(string)
	for c in l:
		ascii8Bin(c) 

#  Exercise 7
def transferHex(string):
	
	outstr = ""
    
    ord_I_Liste = list(string)
    for bokstav in ord_I_Liste:
        representasjon = ord(bokstav)
        outstr += '{0:02x} '.format(representasjon)
        
    return outstr

# Exercise 8
def unicodeBin(character):

    outstr = ""
    unicode_char = bytearray(character)
    
    if len(unicode_char) > 1:
        for char in bytearray(unicode_char):
            outstr += "{0:08b} ".format(char)
    
    else:
        outstr = "{0:08b}".format(ord(character))
    
    return outstr

# Exercise 9
def printSysInfo():
	psutil.cpu_percent(interval=3)
	psutil.cpu_count()
	psutil.disk_usage('/')
	psutil.virtual_memory()

# Tests
def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'

	assert transferHex('hei') == '68 65 69 '
	assert unicodeBin('å') == '11000011 10100101 '
	assert unicodeBin('a') == '01100001'
	
	return "Testene er fullført uten feil."

print test()

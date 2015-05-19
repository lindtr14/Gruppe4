# -*- coding: latin-1 -*-

#  IS-105 LAB1

# This module contains various functions with different purposes.
# In this module you can perform bitwise operations, 
# binary operations on both ascii and unicode characters and return the state
# of the machine through python

import sys
import psutil

# Group members: 
gruppe = {	'student1': 'Andreas Kjærner-Semb', 
			'student2': 'Linda Tran', \
			'student3': 'Frank William Hansen', \
			'student4': 'Ole Aarsnes', \
			'student5': 'Mikael Kile', \
}

#  Exercise 1
def ascii_bird():
	"""Print out a bird in ascii."""
	print"#       \/"
	print"#       \/_"
	print"#  \,   /( ,/"
	print"#   \\\\\\' ///"
	print"#    \_ /_/"
	print"#    (./"
	print"#     '`"

ascii_bird()

#  Exercise 2
def bitAnd(x, y): 
	"""Takes two numbers and returns in which position they 
	both have 1 in a binary number.
	"""
	i = (x & y)
	return i

#  Exercise 3
def bitXor(x, y):
	"""Takes two numbers and returns in which position 
	only one of them have 1 and the other 0.
	"""
	i = x ^ y
	return i

#  Exercise 4
def bitOr(x, y):
	"""Takes two numbers and returns in wich position 
	only one or both have 1 in a binary number.
	"""
	i = x | y
	return i

#  Exercise 5
def ascii8Bin(letter):
	"""Takes a letter and returns its representation in 
	the ascii table as a binary number.
	"""
	i = ord(letter)
	return '{0:08b}'.format(i) 

#  Exercise 6
def transferBin(string):
	"""Takes a word and returns the letters representation
	in the ascii table as binary numbers.
	"""
	l = list(string)
	outstr = ""
	for c in l:
		outstr += ascii8Bin(c) + " "
	return outstr

#  Exercise 7
def transferHex(string):
	"""Takes a string and returns the letters representation
	in the ascii table as hexadecimal numbers.
	"""
	outstr = ""
	
	words_in_list = list(string)
	for character in words_in_list:
		representation = ord(character)
		outstr += '{0:02x} '.format(representation)
		
	return outstr

# Exercise 8
def unicodeBin(character):
	"""Takes a letter and returns its representation in the
	operating system, and not from the ascii table.
	This works with unicode characters.
	"""
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
	psutil.disk_usage('/')
	psutil.virtual_memory()

# Tests
def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'

	assert transferBin('hei') == '01101000 01100101 01101001 '
	assert transferHex('hei') == '68 65 69 '
	assert unicodeBin('å') == '11000011 10100101 '
	assert unicodeBin('a') == '01100001'
	
	return "The tests are completed successfully"

print test()

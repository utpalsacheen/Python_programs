#!/usr/bin/python

"""
bin2dec - binary to decimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a binary string, and print its decimal equivalent
"""

def validate(binStr):
	for ch in binStr:
		if not(ch == '0' or ch == '1'):
			return False
	return True

def convert(binStr):
	dec = 0
	for i in range(len(binStr)):
		bit = binStr[i]
		if bit == '1':
			dec += 2 ** (len(binStr) -1 - i)
	return dec

def main():
	binStr = str(input('Enter a binary string: '))
	print(type(binStr))
	if not validate(binStr):
		print('Error: invalid binary string "{}"'.format(binStr))
	else:
		print('The decimal equivalent for binary "{}" is {}'.format(binStr, convert(binStr)))
		# Using built-in function int(str, radix)
		# built­in function int(str, radix) to convert a number string from the given radix to decimal
		print('The decimal equivalent for binary "{}" using built-in function is: {}'.format(binStr, int(binStr, 2)))

if __name__ == '__main__':
	main()
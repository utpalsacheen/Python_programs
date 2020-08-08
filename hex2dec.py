#!/usr/bin/python

"""
hex2dec - hexadecimal to decimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a hex string, and print its decimal equivalent.
This example illustrates for-loop with index, nested-if, string operations and
dictionary.
"""

import sys # Using sys.exit()

dec = 0 # Accumulating from each hex digit

# Look up table for hex to dec
dictHex2Dec = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

# Prompt and read user input
hexStr = input('Enter a hex string: ')

# Process each hex digit from the left (most significant digit)
for hexDigitIdx in range(len(hexStr)):
	# extract each char string
	hexDigit = hexStr[hexDigitIdx]
	hexExpFactor = 16 ** (len(hexStr) - 1 - hexDigitIdx)
	print(hexExpFactor)
	# Python supports chain comparision
	if '1' <= hexDigit <= '9':
		dec += int(hexDigit) * hexExpFactor
	elif hexDigit == '0':
		pass
	elif 'A' <= hexDigit <= 'F':
		# ord return Unicode number
		dec += (ord(hexDigit) - ord('A') + 10) * hexExpFactor

	elif 'a' <= hexDigit <= 'f':
		# look up from dictionary
		dec += dictHex2Dec[hexDigit] * hexExpFactor
	else:
		print('error: invalid hex string')
		sys.exit()

print('The decimal equivalent for hex "{}" is: {}'.format(hexStr, dec))
# Using built-in function int(str, radix)
print('The decimal equivalent for hex "{}" using built-in function is: {}'.format(hexStr, int(hexStr, 16)))

#!/usr/bin/python

"""
dec2hex - Decimal to Hexadecimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a decimal number and print its hexadecimal equivalent

You can use built­in function hex(decNumber), oct(decNumber), bin(decNunber) 
to convert decimal to hexadecimal, octal and binary, respectively
"""

hexStr = ''
hexChars = ['0','1','2','3', '4','5','6','7', '8','9','A','B', 'C','D','E','F'];

# prompt and read decimal number
dec = int(input('Enter a decimal number: '))
decSave = dec

# REpeated modulus/division and get the hex digits in reverse order
while dec > 0:
	hexDigit = dec % 16
	hexStr = hexChars[hexDigit] + hexStr
	dec  = dec // 16 

print('The hex for decimal {} is: {}'.format(decSave, hexStr))
print('The hex for decimal {} using built-in function is: {}'.format(decSave, hex(decSave)))
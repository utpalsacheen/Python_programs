#!/usr/bin/python

"""
Magic Number - Check if the given number contains a magic digit

Prompt user for a number, and check if the number contains a magic digit.
"""

#def isMagic(number:int, magicDigit:int = 8) -> bool:  # python 3 syntax
def isMagic(number, magicDigit = 8):
	"""
	Check if the given number contains the digit magicDigit.
	Arguments:
	number - positive int only
	magicDigit- single-digit int (default is 8)
	"""
	while number > 0:
		# extract and drop each digit
		if number % 10 == magicDigit:
			return True
		else:
			number //= 10

	return False

#def isMagicStr(number:str, magicDigit:str = '8') -> bool:
def isMagicStr(number, magicDigit = '8'):
	"""
	Check if the given number string contains the magicDigit
	Arguments:
	number - a number string
	magicDigit - s single-digit str (default is '8')
	""" 
	return magicDigit in number  # use built-in sequence operator 'in'

def main():
	# Prompt and read input string as int
	number = int(input('Enter a number: '))

	# Use isMagic()
	if isMagic(number):
		print('{} is a magic number'.format(number))
	else:
		print('{} is not a magic number'.format(number))

	if isMagicStr(str(number), '9'):
		print('{} is a magic number'.format(number))
	else:
		print('{} is not a magic number'.format(number))

if __name__ == '__main__':
	main()
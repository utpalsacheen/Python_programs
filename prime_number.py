#!/usr/bin/python

"""
Problem: prime numbers between 2 to 100
"""

prime_number = []

for number in range(2, 101):
	for factor in range(2, number//2+1):
		if number % factor == 0:
			#print("{} is not a prime number".format(number))
			#prime_number.append(number)
			break
	else:
		prime_number.append(number)
	#	print("{} is a prime number".format(number))


print prime_number

def fibon(n):
	a, b = 1, 1
	for count in range(n):
		print(a)
		a, b = b, a+b
	#print()

fibon(20)
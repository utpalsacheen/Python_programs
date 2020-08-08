"""
Problem: Factorial

Example: 5! = 5*4*3*2*1
"""

def factorial(n):

	if n == 1:
		return 1

	return n * factorial(n-1)

n = 5
print(factorial(n))
"""
Problem: Given a string insert a "*" after each char using recursion method
"""

def rev(str1):
	print str1

	if len(str1) == 0:
		return str1
	else:
		return rev(str1[1:]) + str1[0]

def recStar(string1):
	print string1

	if len(string1) == 0:
		return string1
	else:
		return string1[0] + "*" + recStar(string1[1:])


def iteratibve_star(str1):
	print str1

	i = 0
	n = len(str1)

	while i < n:
		print(str1[i] + "*"),
		i += 1


string1 = "shilpa"

string2 = recStar(string1)

print string2

iteratibve_star(string1)
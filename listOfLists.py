"""
List of Lists/ Matrices/ Two dimensional List

"""

a = [[1,2,3], [4,5,6]]
#print a[0]
#print a[1]

for i in range(len(a)):
	for j in range(len(a[i])):
		print a[i][j]

for row in a:
	for elem in row:
		print(elem)

# Below code prints
# 1 2 3
# 4 5 6
for row in a:
	print(' '.join([str(elem) for elem in row]))


# calculate the sum of all the numbers in the 2-dimensional list
sum = 0
for row in a:
	for elem in row:
		sum += elem
print sum

# creating nxm arrays filled with zeros
n = 3; m = 4
a = [0] * n
for i in range(n):
	a[i] = [0] * m

for row in a:
	print(' '.join(str(elem) for elem in row))

a =[]
for i in range(n):
	a.append([0] * m)

for row in a:
	print(' '.join(str(elem) for elem in row))

a = [[0] * m for i in range(n)]
for row in a:
	print(' '.join(str(elem) for elem in row))


# processing a 2D list
# an array of n rows and n columns. 
# Main diagonal element = 1
# Above main diagonal elements = 0
# Below main diagonal elements = 1
n = 3
# create n * n list of lists with fillend with elements = 0
a = [[0] * n for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))

for i in range(n):
	for j in range(n):
		if i < j:
			a[i][j] = 0
		elif i == j:
			a[i][j] = 1
		elif i > j:
			a[i][j] = 2

for row in a:
	print(' '.join([str(elem) for elem in row]))

n = 5; m = 6
a = [[0] * m for i in range(n)]

a = [[i*j for j in range(m)] for i in range(n)]

for row in a:
	print(' '.join([str(elem) for elem in row]))


# input a 2-D lists
# n = int(input())
# a = []
# for i in range(n):
# 	a.append([int(j) for j in input().split()])

#!/usr/bin/python

"""

 Porblem: Sequential Search

Complexity: O(n)

Best case: O(1)
Worst case: O(n)

"""

# unordered sequential search
def sequentialSearch(array, num):
	found = False
	for i in range(len(array)):
		if array[i] == num:
			found = True
			return found

	return found

# ordered sequential search
def orderedSequentialSearch(array, item):
	pos = 0
	found = 0
	stop = 0

	while pos < len(array) and not found and not stop:
		if array[pos] == item:
			found = True
			stop = True
		else:
			pos += 1

	return found

"""
def sequentialSearch(arr, num):
	pos = 0
	found = False

	while pos < len(arr) and not found:
		if arr[pos] == item:
			found = True
		else:
			pos += 1

	return found
"""

# main
arr = [2,5,1,6,3,9,8,10]
found = sequentialSearch(arr, 4)
assert found == False, "4 is not in the array"

found = sequentialSearch(arr, 10)
assert found == True, "10 is in in the array"
#!usr/bin/python

"""
Problem: Binary Search

Complexity: Olog(n)

The maaximum number of comparisions is logarithmic with respect to the 
number of items in the list. Therefor the binary search is Olog(n)
"""

def BinarySearch(array, item):

	found = False
	low = 0
	high = len(array) - 1

	while low <= high and not found:
		mid = (low + high) // 2
		print("low: %d mid: %d high: %d" % (low,mid,high))

		if array[mid] == item:
			print(array[mid])
			print("Found: %s" %found)
			found = True
		else:
			if item < array[mid]:
				high = mid - 1
			else:
				low = mid + 1

	return found


# Recursive solution
def recursiveBinarySearch(array, item):
	if len(array) == 0:
		return False
	else:
		mid = len(array) // 2
		if array[mid] == item:
			return True
		else:
			if item < array[mid]:
				return recursiveBinarySearch(array[:mid-1], item)
			else:
				return recursiveBinarySearch(array[mid+1:], item)



# main
array = [1,2,3,4,5,6,7,8,9,10]
found = BinarySearch(array, 8)
assert found == True, "Binary Search found 8 in the array"

found = BinarySearch(array, 0)
assert found == False, "Binary Search  did not find 0 in the array"

found = recursiveBinarySearch(array, 10)
assert found == True, "Binary Search  found 10 in the array"

found = recursiveBinarySearch(array, 0)
assert found == False, "Binary Search  did not find 0 in the array"
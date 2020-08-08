#!/usr/bin/python

"""
Problem: QuickSort

Divide and Conquer rule like MergeSort without using additional Storage

Quick Sort selects a value, which is called a Pivot value. 
Many different ways to select a pivot value but in this case
will select the first element.
Role of Pivot value is to assit with splitting the list.
The actual position where the pivot value belongs in the final sorted list,
is commonly called the split point, will be used to divide the list for subsequent 
calls to the quick sort.

Analysis:
For a list of length n, if the partition always occurs in the middle of
the list, there will again be log n divisions. In order to find the split point, 
each of the n items need to be checked against the pivot value. The result is
n log n. In addition there is no need for additional memory as in the merge sort process.

In the worst case, the split points may not be in the middle and can be very skewed
to the left or the right, leaving a very uneven division. In this case sorting a list
of n items divides into sorting a list of 0 items and a list of n -1 items. Then 
sorting a list of n -1 divides into a list of size 0 and list of size n-2 and so on.
The resultis an O(n^2) sort with all the overhead that recursion requires.

"""




def QuickSort(arr):
	last = len(arr) - 1
	quickSortHelper(arr, 0, last)


def quickSortHelper(alist, first, last):
	if first < last:
		splitpoint = partition(alist, first, last)

		quickSortHelper(alist, first, splitpoint-1)
		quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):

	done = False
	leftmark = first+1
	rightmark = last
	pivot = alist[first]

	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivot:
			leftmark += 1
		while rightmark >= leftmark and alist[rightmark] >= pivot:
			rightmark -= 1

		if leftmark > rightmark:
			done = True
		else:
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

	alist[first], alist[rightmark] = alist[rightmark], alist[first]

	return rightmark



"""
def QuickSort(arr):
	last = len(arr) - 1
	quickSortHelper(arr, 0, last)

def quickSortHelper(alist, first, last):
	if first < last:
		splitpoint = partition(alist, first, last)

		quickSortHelper(alist, first, splitpoint-1)
		quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
	pivot = alist[first]

    # leftmark is after the pivot value
	leftmark = first + 1
	rightmark = last

	done = False

	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivot:
			leftmark += 1

		while rightmark >= leftmark and alist[rightmark] >= pivot:
			rightmark -= 1

		if rightmark < leftmark:
			done = True
		else:
			#temp = alist[leftmark]
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
			#alist[rightmark] = temp

	#temp = alist[first]
	alist[first], alist[rightmark] = alist[rightmark], alist[first]
	#alist[rightmark] = temp

	return rightmark


"""


# main
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
QuickSort(arr)
print(arr)
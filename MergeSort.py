#!/usr/bin/python
	
"""
Problem: Merge Sort
Divide and Conquer stratergy

Merge Sort is a recursive Algorithm that continually splits
a list in half. 
If the list is empty or has one item, it is sorted by definition (the base case)
If the list has more than one item, we split the list and
recursively invoke a merge sort on both halves.
Once the two halves are sorted, the fundamental operation, called Merge is performed.
Merging is the process of taking two sorted lists and combining them together into a 
single, sorted, new list.

Complexity:
To analyse the Merge Sort function, we need to consider two distinct process
 that make up the implementation.
 First, the list is split into halves, we can divide a list in half logn times 
 where n is the length of the list.
 Second process is the merge. Each item in the list will eventually be processed 
 and placed on the sorted list. so the merge operation which results in a list of size n
 requires n operations.
 The result of this analysis is that log n splits, each of which costs n for the total 
 of n log n operations. A MergeSort is an O(n log n) algorithm

 Recall that the slicing operator is O(k) where k is the size of the slice. In order to 
 gaurentee that MergeSort will be O(n log n) we will need to remove the slice operator.
 Again, this is possible if we simply pass the starting and ending indices along the list
 when we make the recursive call. 

 It is important to notice that this sorting algorithm requires extra spacing to hold the
 two halves as they are extracted with the slicing operations. This additional space
 can be critical factor if the list is large and can make the sort problematic when 
 working on a large data sets.

"""

def MergeSort(arr):
	print("Splitting: " , arr)


	if len(arr) > 1:
		# split the list into two halves
		mid = len(arr) // 2
		# lefthalf is the left half of the arr list
		lefthalf = arr[:mid]
		# righthalf is the right half of the arr list
		righthalf = arr[mid:]

		# split the lefthalf and the righthalf by recursivley
		# calling MergeSort
		MergeSort(lefthalf)
		MergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k] = lefthalf[i]
				i += 1
			else:
				arr[k] = righthalf[j]
				j += 1
			k += 1

		# copy the remaining elements of the lefthalf of the list 
		# , if there is any to the array
		while i < len(lefthalf):
			arr[k] = lefthalf[i]
			i += 1
			k += 1

		# copy the remaining elements of the righthalf of the list 
		# , if there is any to the array
		while j < len(righthalf):
			arr[k] = righthalf[j]
			j += 1
			k += 1

	print("Merging: ", arr)


"""
Try MergeSort in Python without using splice

def Merge(arr, leftIndex, mid, rightIndex):
	# Merge two subarrays of arr[]
	# First subarray is arr[l..m]
	# Second subarray is arr[m+1..r]
	i = 0
	j = 0
	k = 0
	lefthalf = arr



def tMergeSort(arr, leftIndex, rightIndex):

	print("Splitting: ", arr)

	if leftIndex < rightIndex:
		mid = leftIndex + (rightIndex - leftIndex) // 2
		tMergeSort(arr, leftIndex, mid)
		tMergeSort(arr, mid, rightIndex)

		Merge(arr, leftIndex, mid, rightIndex)

	print("merging: ", arr)


"""



arr = [3,1,8,4,0,2,6]
sorted_arr = MergeSort(arr)
print sorted_arr
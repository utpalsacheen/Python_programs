#!/usr/bin/python

"""
Problem: Selection Sort
The selection sort improves on the bubble sort by making only one exchange for 
every pass through the list. To do this, selection sort looks for the largest 
value as it makes a pass and, after completing the pass, places it in the proper
location.

Notice that selection sort makes the same number of comparisions as the bubble sort
and is therefore also O(n^2)
However because of the reduction in the number of exchanges, selection sort typically
executes faster in benchmark studies.

"""

def SelectionSort(arr):
	n = len(arr) 
    # traverse through all array elements
	for i in range(n):
		# Find the minimum element in remaining unsorted array
		min_indx = i
		for j in range(i+1, n):
			if arr[min_indx] > arr[j]:
				min_indx = j

		# swap the found minimun element with the first element
		arr[i], arr[min_indx] = arr[min_indx], arr[i]

	return arr


# main
arr = [3,1,8,4,0,2,6]
sorted_arr = SelectionSort(arr)
print sorted_arr

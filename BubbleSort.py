#!/usr/bin/python

"""
Problem: Bubble Sort

Analysis:
The total number of comparisions is the sum of the first n-1 integers. 
the sum of the first n-1 integers is (1/2)n^2 + (1/2)n - n, which is (1/2)n^2 - (1/2)n
This is still O(n^2) comparisions.

Best Case: Array already sorted
Worst case: every comparision will cause an exchange

Note: Bubble sort often considered most inefficient sorting method since it must
exchange items before the final location is known.

Check ShortBubble 

"""

def bubbleSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				print("swaping %d and %d" %(arr[j], arr[j+1]))
				#temp = arr[j]
				#arr[j] = arr[j+1]
				#arr[j+1] = temp
				arr[j], arr[j+1] = arr[j+1], arr[j]


	return arr

arr = [3,1,8,4,0,2,6]
sorted_arr = bubbleSort(arr)
print sorted_arr
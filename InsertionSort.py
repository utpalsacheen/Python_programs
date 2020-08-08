
#!/usr/bin/Python

"""
Problem: Insertion Sort
Insertion sort always maintains a sorted sublist in the power positions of the list.
Each new item is then inserted back into the previous sublist such that the 
sorted sublist is one item larger.

One note about shifting versus exchanging is also important. In general, 
a shift operation requires approximately a third of the processing work
of an exhange since only one assignment is performed. 

Complexity:
Runtime Complexity : O(n^2) 
"""
def InsertionSort(arr):
	# traverse through 1 to len(arr)
	for i in range(1, len(arr)):
		currentValue = arr[i]
		# move elements of arr[0..i-1], that are greater then 
		# key, to one position ahead of their current position
		j = i-1
		while j >= 0 and currentValue < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = currentValue

	return arr


arr = [3,1,8,4,0,2,6]
sorted_arr = InsertionSort(arr)
print sorted_arr
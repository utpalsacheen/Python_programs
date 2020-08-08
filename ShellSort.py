#!/usr/bin/python

"""
Problem: Shell Short

Shell sort sometimes called the "diminishing increament sort" improves
on the insertion sort by breaking the original list into a number of smaller
sublists, each of which is sorted using an insertion sort. 
The unique ways that these sublists are chosen is the key to the shell sort. Instead
of breaking the list into sublists of contiguous items, the shell sort uses an
increment i, sometimes called the gap, to create a sublist by choosing all items
that are i items apart.

Analysis:
The complexity falls somewhere between O(n) and O(n^2).
"""

def ShellSort(alist):

	# start with a big gap, then reduce the gap
	n = len(alist)
	gap = n // 2

	# Do a gapped insertion sort for this gap size.
	# the first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire
	# array is gap sorted
	while gap > 0:
		for i in range(gap,n):
			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = alist[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and alist[j-gap] > temp:
				alist[j] = alist[j-gap]
				j -= gap

			# put temp (the original a[i] in its correct location)
			alist[j] = temp

		gap //= 2





# main
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ShellSort(arr)
print arr
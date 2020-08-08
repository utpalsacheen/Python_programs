#!/usr/bin/python

""" Given a sorted array of integers find low and high index of the given key """
""" Runtime Complexity - Logarithmic, O(logn) """
""" Memory Complexity - Contant, O(1) """

def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high/2

    while low <= high:
        mid_elem = arr[mid]
        if mid_elem < key:
            low = mid + 1
        else:
            high = mid -1

        mid = low + (high - low) // 2

    if arr[low] == key:
        return low

    return -1

def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high/2

    while low <= high:
        mid_elem = arr[mid]
        if mid_elem <= key:
            low = mid + 1
        else:
            high = mid -1
        mid = low + (high - low) // 2

    if arr[high] == key:
        return high

    return -1

# main
arr = [1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,6]
key = 5
low = find_low_index(arr, key)
high = find_high_index(arr, key)
assert 15 == low, "Invalid Low Value"
assert 17 == high, "Invalid High Value"
print("Low index of " + str(key) + " : " + str(low))
print("High index of " + str(key) + " : " + str(high))

key = 2 
low = find_low_index(arr, key)
high = find_high_index(arr, key)
assert 3 == low, "Invalid Low Value"
assert 7 == high, "Invalid High Value"
print("Low index of " + str(key) + " : " + str(low))
print("High index of " + str(key) + " : " + str(high))

#!/usr/bin/python

""" Binary Search Algorithm - Recursive Solution """
""" Runtime Complexity - logarithmic O(logn) """
""" Memory Complexity - Logarithmic O(logn) """

import random

def binary_search_rec(arr, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if key == arr[mid]:
        return mid
    elif arr[mid] > key:
        return binary_search_rec(arr, key, low, mid-1)
    else:
        return binary_search_rec(arr, key, mid+1, high)

def binary_search(arr, key):
    return binary_search_rec(arr, key, 0, len(arr) -1)

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
       

def test_binary_search(arr, key, expected):
    arr.sort()
    i = binary_search(arr, key)
    j = linear_search(arr, key)
    print(str(i), str(j))

    assert i == j
    if expected == True:
        assert(i >= 0)
    else:
        assert(i == -1)

    print("Found the key at position : " +  str(i))
    print("Found the key at position : " +  str(j))


def main():
    arr = [10,20,34,56,78,80,90]
    test_binary_search(arr, 20, True)
    test_binary_search(arr, 90, True)
    test_binary_search(arr, 18, False)
    #a = []
    #for x in range(20):
    #    a.append(random.randint(1,20))
    #test_binary_search(a, 1, True)

main()

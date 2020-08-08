#!/usr/bin/python

""" Binary Search Algorithm - Iterative Solution """
""" Runtime Complexity - Logrithemic O(logn) """
""" Memory Complexity - Constant O(1) - better memory complexity than recursive solution """

def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1


    return -1

def test_binary_search(arr, key, expected):
    arr.sort()
    i = binary_search_iterative(arr, key)
    if expected == True:
        assert(i >= 0)
    else:
        assert(i == -1)

    print("Found Key at position: " + str(i))

def main():
    arr = [12, 23,45,67,78,89,90]
    test_binary_search(arr, 45, True)
    test_binary_search(arr, 90, True)
    


main()


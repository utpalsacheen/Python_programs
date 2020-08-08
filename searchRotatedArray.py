#!/usr/bin/python

""" Search Rotated Array """
""" Runtime Complexity - logarithmic O(logn) """
""" Memory Complexity - logarithmic O(logn) """
""" Memory Complexity - iterative gets contstant memory complexity """



def binary_search_rotated(arr, key):
    st = 0
    end = len(arr) - 1

    if st > end:
        return -1

    while st <= end:
        mid = st + (end - st // 2)
        if arr[mid] == key:
            return mid

        if (arr[st] < arr[mid] and
              key >= arr[st] and
              key < arr[mid]):
            end = mid -1
        elif ( arr[end] > arr[mid] and
              key > arr[mid] and
              key <= arr[end]):
            st = mid + 1
        elif arr[st] > arr[mid]:
            end = mid - 1
        elif arr[mid] < arr[end]:
            st = mid + 1

def linear_search(a, key):
    for x in range(0,len(a) - 1):
        if key == a[x]:
            return x
    return -1


def main():
    arr = [6,7,8,9,1,2,3,4,5]
    print("Key: 3 for binary search found at position: " + str(binary_search_rotated(arr, 3)))
    print("Key: 3 for linear search found at position: " + str(linear_search(arr, 3)))

    arr1 = [4,5,6,1,2,3]
    print("Key :6 for binary search found at position: " + str(binary_search_rotated(arr1, 6)))
    print("Key :6 for linear search found at position: " + str(linear_search(arr1, 6)))

main()

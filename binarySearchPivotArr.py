# Search an element in a sorted and rotated array
# Device a way to find an element in the rotated array in O(log n) time

# The main idea for finding pivot is - for a sorted and pivoted array, pivot element is the only element
# for which next element to it is smaller than it
# for instance arr = 1 2 3 4 5 might become 3 4 5 1 2 
# so the pivot here is 5 because the next element is 1 which is smaller to it


# searches an element key in a pivoted sorted array 
def pivotedBinarySearch(arr, n, key):
    pivot = findPivot(arr, 0, n-1)

    # if we did not find a pivot, then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)

    # if we found pivot, then first compare the key with the pivot and
    # then search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    else:
        return binarySearch(arr, pivot+1, n, key)


def findPivot(arr, l, r):
    # base cases
    if r < l: return -1
    if r == l: return l

    mid = (r+l)/2 # this is same as l + (r - l)/2
    
    if mid < r and arr[mid] > arr[mid+1]:
        return mid
    elif mid > l and arr[mid] < arr[mid-1]:
        return mid-1
    elif arr[l] >= arr[mid]:
        return findPivot(arr, l, mid-1)
    else:
        return findPivot(arr, mid+1, r)


def binarySearch(arr, l, r, key):

    if r < l:
        return -1

    mid = (r+l)/2

    if key == arr[mid]:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, 0, mid-1, key)
    else:
        return binarySearch(arr, mid+1, r, key)

# main

arr = [3,4,5,6,7,1,2]
n = len(arr)
element = 2 

print "Index: %d\n" % pivotedBinarySearch(arr, n, element)

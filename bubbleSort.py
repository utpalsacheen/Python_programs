# Bubble sort - repeatedly swaps the adjacent elements if they are in wrong order

def bubbleSort(arr, n):
    for i in range(n):
        for j in range(0, n-i-1):
             if arr[j] > arr[j+1]:
                 arr[j] , arr[j+1] = arr[j+1], arr[j]


# main

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

bubbleSort(arr, n)
print "Sorted array: \n"
print arr
for i in range(len(arr)):
    print ("%d" %arr[i],)

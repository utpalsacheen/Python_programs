# Insertion Sort:

def insertionSort(arr, n):

     for i in range(n):
         key = arr[i]
         j = i-1
         while j>=0 and arr[j] > key:
             arr[j+1] = arr[j]
             j = j-1
         arr[j+1] = key


# main

arr = [12, 11, 13, 5, 6]
n = len(arr)

insertionSort(arr, n)
print "Insertion sort:\n"
for i in range(n):
    print"%d" %arr[i]

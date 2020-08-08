def QuickSort(a):
    last = len(a)-1
    helper(a, 0, last)

def helper(a, first, last):
    if first < last:
        splitpoint = partition(a, first, last)
        helper(a, first, splitpoint-1)
        helper(a, splitpoint+1, last)

def partition(a, first, last):
    pivot = a[first]
    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while (leftmark <= rightmark and a[leftmark] <= pivot):
            leftmark += 1
        while (rightmark >= leftmark and a[rightmark] >= pivot):
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            a[leftmark], a[rightmark] = a[rightmark], a[leftmark]

    a[first], a[rightmark] = a[rightmark], a[first]
    print rightmark
    print a
    return rightmark

def merge_sort(a):
    n = len(a)
    if n > 1:
        mid = n //2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i += 1
            else:
                a[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            a[k] = righthalf[j]
            j += 1
            k += 1



a = [9, 4, 7, 0, 1, 6, 2, 4]

QuickSort(a)
print a

b = [9, 3, 7, 4, 8, 2, 0, 5, 1]
merge_sort(b)

print b

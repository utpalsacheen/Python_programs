#!/usr/bin/python

l1 = [1,2,0,6,9]

# Bubble sort - O(n^2)
for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] > l1[j]:
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp
print(l1)

# selection sort
s = [1,2,0,6,9]
for i in range(len(s)):
    min_idx = i
    for j in range(i+1, len(s)):
        if s[min_idx] > s[j]:
            min_idx = j
    s[i], s[min_idx] = s[min_idx], s[i]
print(s)

# insertion sort
a = [1,2,0,6,9]
for i in range(1, len(a)):
    cur_val = a[i]
    j = i-1
    while j >= 0 and cur_val < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = cur_val
print(a)


# Shell Sort


#!/usr/bin/python

""" Find smallest common number in multiple arrays """
""" Runtime Complexity - Linear, O(n) """
""" Memory Complexity  - Contant, O(1) """

def find_least_common_number(a, b, c):
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):
        # find the smallest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1

    return -1


def find_max_common_number(a, b, c):
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    print(a)
    print(b)
    print(c)

    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):
        # find the biggest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        if a[i] >= b[j] and a[i] >= c[k]:
            i += 1
        elif b[j] >= a[i] and b[j] >= c[k]:
            j += 1
        elif c[k] >= a[i] and c[k] >= b[j]:
            k += 1

    return -1 
        

    



v1 = [1, 6, 10, 14, 50]
v2 = [-1, 6, 7, 8, 50]
v3 = [0, 6, 7, 10, 25, 30, 50]

result = find_least_common_number(v1, v2, v3)
print("The least common number is : " + str(result))

x1 = [1, 6, 10, 14, 50, 78, 79, 90]
x2 = [-1, 6, 7, 8, 50, 54, 76, 89, 99]
x3 = [0, 6, 7, 10, 25, 30, 50, 65, 76, 79, 80, 85, 100]
result1 = find_max_common_number(x1, x2, x3)
print("The maximum common number is : " + str(result1))

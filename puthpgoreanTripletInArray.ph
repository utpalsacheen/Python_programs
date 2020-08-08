# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

def pythoTriplet(arr):

    n = len(arr)
    t = False 
    c = list()

    for i in range(0, n):
        for j in range(1, n):
            for k in range(2, n):
                if arr[i]**2 + arr[j]**2 == arr[k]**2:
                    c.append(list((arr[i], arr[j], arr[k])))
                    t = True
    
    if t:
        print "There is a Pythogorean triplets", c
    else:
        print "There is no Pythogorean triplet"

arr = [3, 1, 4, 6, 5]
print arr
pythoTriplet(arr)

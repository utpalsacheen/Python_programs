#!/usr/bin/python

""" Move Zeros to left """
""" Given an integer array, move all elements containing '0' to the left while 
    maintaining the order of other elements in the array"""
""" Runtime Complexity - Linear, O(n) """
""" Memory Complexity  - Contant, O(1) """

def move_zeros_to_left(arr):
    if len(arr) < 1:
        return 1

    read_index = len(arr) - 1
    write_index = len(arr) - 1

    while read_index >= 0:
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index -= 1
        read_index -= 1

    while write_index >= 0:
        arr[write_index] = 0
        write_index -= 1


v = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]

move_zeros_to_left(v)

for i in xrange(0, len(v)):
    if( i == len(v) - 1):
        print str(v[i])
    else:
        print str(v[i]) + ", "

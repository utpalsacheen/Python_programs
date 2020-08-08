#!/usr/bin/python

from collections import deque

""" Find maximum number in the sliding window """
""" Given large array of integers and a window of size 'w', 
find the current maximum in the window as the window slides through the entire array """
""" Runtime Complexity :  """
""" Memory Complexity  :  """

def find_max_sliding_window(arr, win_size):
    # return if window size is greater than the length of the array
    if win_size > len(arr):
        return

    # dequeue is a list-like container with fast appends and pop at either ends
    window = deque()

    # find out the max for first window
    for i in xrange(0, win_size):
        #print("arr[window[-1]] : " + str(arr[window[-1]]))
        while window and arr[i] >= arr[window[-1]]:
            window.pop() # pop the item if less than arr[i]
        window.append(i)

    print(arr[window[0]])

    for i in xrange(win_size, len(arr)):
        # remove all the numbers that are smaller than the current number
        # from the tail of the list
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window anymore
        if window and (window[0] <= i - win_size):
            window.popleft()

        window.append(i)
        print(arr[window[0]])

def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print "Input array: ", arr
    print("Window size:  4")
    find_max_sliding_window(arr, 4)
    array = [1, 2, 3, 4, 3, 2, 1, 2, 5]
    find_max_sliding_window(array, 5)


main()

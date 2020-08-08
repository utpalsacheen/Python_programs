def longestString(inputArray):
    m = max([len(i) for i in inputArray])
    return [i for i in inputArray if len(i)==m]

    #return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

"""
    print(arr)
    larr = []
    larr.append(arr[0])
    for n in range(1, len(arr)):
        print(larr)
        if len(arr[n]) > len(larr[0]):
            del larr[0]
            larr.append(arr[n])
        elif len(arr[n]) == len(larr[0]):
            larr.append(arr[n])

    return larr
"""

arr = ["aba", "aa", "ad", "vcd", "aba"]
arr1 = longestString(arr)
print(arr1)

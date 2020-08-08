def shapeArea(n):
    if n == 1:
        return

    return shapeArea((n-1) + 4 * (n-1))

#n = shapeArea(3)
#print(n)


def makeArrayConsecutive2(statues):
    
    for n in range(0,len(statues)-1):
        if statues[n+1] < statues[n]:
            tmp = statues[n+1]
            statues[n+1] = statues[n]
            statues[n] = tmp

    reqStatues = []
    for n in range(0,len(statues) -1):
        val = statues[n]
        nextVal = statues[n+1]
        tmp = val
        while nextVal != tmp+1:
            tmp += 1
            reqStatues.append(tmp)

    return len(reqStatues)


arr = [6,2,3,8]

#size = makeArrayConsecutive2(arr)
#print(size)


def test(sequence):
    print("Length: of the array: " + str(len(sequence)))
    if len(sequence) <=2:
        return True

    for n in range(1, len(sequence)-1):
        print(str(sequence[n-1]) + " " + str(sequence[n]) + " " + str(sequence[n+1]))
        if sequence[n-1] >= sequence[n] and sequence[n] < sequence[n+1]:
            print("deleting 1st: " + str(sequence[n-1]))
            del sequence[n-1]
            break
        elif sequence[n-1] < sequence[n] and sequence[n] > sequence[n+1]:
            if sequence[n-1] < sequence[n+1]:
                del sequence[n]
            elif sequence[n-1] >= sequence[n+1]:
                del sequence[n+1]
            break
    

    print(sequence)
    for n in range(0, len(sequence) - 1):
        if sequence[n] >= sequence[n+1]:
            return False

    return True

arr = [1, 3, 2] 
print(arr)
assert test(arr) == True, "Should return True"

arr1 = [1, 2, 3, 4, 3, 6] 
print(arr1)
assert test(arr1) == True, "Should return True"

arr2 = [40, 50, 60, 10, 20, 30]
print(arr2)
assert test(arr2) == False, "Should return Fasle"

arr3 = [1, 2, 3, 4, 5, 3, 5, 6] 
print(arr3)
assert test(arr3) == True, "Should return True"

arr4 = [1, 2, 1, 2]
print(arr4)
assert test(arr4) == True, "Should return True"

arr5 = [10, 1, 2, 3, 4, 5]
print(arr5)
assert test(arr5) == True, "Should return True"

arr6 =[1, 2, 5, 3, 5]
print(arr6)
assert test(arr6) == True, "Should return true"

arr7 = [1, 2, 3, 4, 99, 5, 6]
print(arr7)
assert test(arr7) == True, "Should return True"

arr8 = [123, -17, -5, 1, 2, 3, 12, 43, 45] 
print(arr8)
assert test(arr8) == True, "Should return True"

arr9 = [3, 5, 67, 98, 3] 
print(arr9)
assert test(arr9) == True, "Should return True"
